# 关于 Linux shell 你必须知道的技巧

<p align='center'>
<a href="https://github.com/labuladong/fucking-algorithm" target="view_window"><img alt="GitHub" src="https://img.shields.io/github/stars/labuladong/fucking-algorithm?label=Stars&style=flat-square&logo=GitHub"></a>
<a href="https://appktavsiei5995.pc.xiaoe-tech.com/index" target="_blank"><img class="my_header_icon" src="https://img.shields.io/static/v1?label=精品课程&message=查看&color=pink&style=flat"></a>
<a href="https://www.zhihu.com/people/labuladong"><img src="https://img.shields.io/badge/%E7%9F%A5%E4%B9%8E-@labuladong-000000.svg?style=flat-square&logo=Zhihu"></a>
<a href="https://space.bilibili.com/14089380"><img src="https://img.shields.io/badge/B站-@labuladong-000000.svg?style=flat-square&logo=Bilibili"></a>
</p>

![](https://labuladong.github.io/algo/images/souyisou1.png)

**通知：[数据结构精品课](https://aep.h5.xeknow.com/s/1XJHEO) 已更新到 V2.0；[第 12 期刷题打卡](https://mp.weixin.qq.com/s/eUG2OOzY3k_ZTz-CFvtv5Q) 最后一天报名；点击这里体验 [刷题全家桶](https://labuladong.gitee.io/algo/images/others/%E5%85%A8%E5%AE%B6%E6%A1%B6.jpg)。另外，建议你在我的 [网站](https://labuladong.gitee.io/algo/) 学习文章，体验更好。**



**-----------**

我个人很喜欢使用 Linux 系统，虽然说 Windows 的图形化界面做的确实比 Linux 好，但是对脚本的支持太差了。一开始有点不习惯命令行操作，但是熟悉了之后反而发现移动鼠标点点点才是浪费时间的罪魁祸首。。。

**那么对于 Linux 命令行，本文不是介绍某些命令的用法，而是说明一些简单却特别容易让人迷惑的细节问题**。

1、标准输入和命令参数的区别。

2、在后台运行命令在退出终端后也全部退出了。

3、单引号和双引号表示字符串的区别。

4、有的命令和`sudo`一起用就 command not found。

### 一、标准输入和参数的区别

这个问题一定是最容易让人迷惑的，具体来说，就是搞不清什么时候用管道符`|`和文件重定向`>`，`<`，什么时候用变量`$`。

比如说，我现在有个自动连接宽带的 shell 脚本`connect.sh`，存在我的家目录：

```shell
$ where connect.sh
/home/fdl/bin/connect.sh
```

如果我想删除这个脚本，而且想少敲几次键盘，应该怎么操作呢？我曾经这样尝试过：

```shell
$ where connect.sh | rm
```

实际上，这样操作是错误的，正确的做法应该是这样的：

```shell
$ rm $(where connect.sh)
```

前者试图将`where`的结果连接到`rm`的标准输入，后者试图将结果作为命令行参数传入。

**标准输入就是编程语言中诸如`scanf`或者`readline`这种命令；而参数是指程序的`main`函数传入的`args`字符数组**。

前文 [Linux文件描述符](https://labuladong.github.io/article/fname.html?fname=linux进程) 说过，管道符和重定向符是将数据作为程序的标准输入，而`$(cmd)`是读取`cmd`命令输出的数据作为参数。

用刚才的例子说，`rm`命令源代码中肯定不接受标准输入，而是接收命令行参数，删除相应的文件。作为对比，`cat`命令是既接受标准输入，又接受命令行参数：

```shell
$ cat filename
...file text...

$ cat < filename
...file text...

$ echo 'hello world' | cat
hello world
```

**如果命令能够让终端阻塞，说明该命令接收标准输入，反之就是不接受**，比如你只运行`cat`命令不加任何参数，终端就会阻塞，等待你输入字符串并回显相同的字符串。

### 二、后台运行程序

比如说你远程登录到服务器上，运行一个 Django web 程序：

```shell
$ python manager.py runserver 0.0.0.0
Listening on 0.0.0.0:8080...
```

现在你可以通过服务器的 IP 地址测试 Django 服务，但是终端此时就阻塞了，你输入什么都不响应，除非输入 Ctrl-C 或者 Ctrl-/ 终止 python 进程。

可以在命令之后加一个`&`符号，这样命令行不会阻塞，可以响应你后续输入的命令，但是如果你退出服务器的登录，就不能访问该网页了。

如果你想在退出服务器之后仍然能够访问 web 服务，应该这样写命令 `(cmd &)`：

```shell
$ (python manager.py runserver 0.0.0.0 &)
Listening on 0.0.0.0:8080...

$ logout
```

**底层原理是这样的**：

每一个命令行终端都是一个 shell 进程，你在这个终端里执行的程序实际上都是这个 shell 进程分出来的子进程。正常情况下，shell 进程会阻塞，等待子进程退出才重新接收你输入的新的命令。加上`&`号，只是让 shell 进程不再阻塞，可以继续响应你的新命令。但是无论如何，你如果关掉了这个 shell 命令行端口，依附于它的所有子进程都会退出。

而`(cmd &)`这样运行命令，则是将`cmd`命令挂到一个`systemd`系统守护进程名下，认`systemd`做爸爸，这样当你退出当前终端时，对于刚才的`cmd`命令就完全没有影响了。

类似的，还有一种后台运行常用的做法是这样：

```shell
$ nohup some_cmd &
```

`nohub`命令也是类似的原理，不过通过我的测试，还是`(cmd &)`这种形式更加稳定。

### 三、单引号和双引号的区别

不同的 shell 行为会有细微区别，但有一点是确定的，**对于`$`，`(`，`)`这几个符号，单引号包围的字符串不会做任何转义，双引号包围的字符串会转义**。

shell 的行为可以测试，使用`set -x`命令，会开启 shell 的命令回显，你可以通过回显观察 shell 到底在执行什么命令：

![](https://labuladong.github.io/algo/images/linuxshell/1.png)

可见 `echo $(cmd)` 和 `echo "$(cmd)"`，结果差不多，但是仍然有区别。注意观察，双引号转义完成的结果会自动增加单引号，而前者不会。

**也就是说，如果 `$` 读取出的参数字符串包含空格，应该用双引号括起来，否则就会出错**。

### 四、sudo 找不到命令

有时候我们普通用户可以用的命令，用 `sudo` 加权限之后却报错 command not found：

```shell
$ connect.sh
network-manager: Permission denied

$ sudo connect.sh
sudo: command not found
```

原因在于，`connect.sh` 这个脚本仅存在于该用户的环境变量中：

```shell
$ where connect.sh 
/home/fdl/bin/connect.sh
```

**当使用 `sudo` 时，系统会使用 `/etc/sudoers` 这个文件中规定的该用户的权限和环境变量**，而这个脚本在 `/etc/sudoers` 环境变量目录中当然是找不到的。

解决方法是使用脚本文件的路径，而不是仅仅通过脚本名称：

```shell
$ sudo /home/fdl/bin/connect.sh
```



<hr>
<details>
<summary><strong>引用本文的文章</strong></summary>

 - [Linux 管道符原理大揭秘](https://labuladong.github.io/article/fname.html?fname=linux技巧3)

</details><hr>





**＿＿＿＿＿＿＿＿＿＿＿＿＿**

**《labuladong 的算法小抄》已经出版，关注公众号查看详情；后台回复关键词「**进群**」可加入算法群；回复「**全家桶**」可下载配套 PDF 和刷题全家桶**：

![](https://labuladong.github.io/algo/images/souyisou2.png)


======其他语言代码======
