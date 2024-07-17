# 关于 Linux shell 你必须知道的技巧

<p align='center'>
<a href="https://github.com/labuladong/fucking-algorithm" target="view_window"><img alt="GitHub" src="https://img.shields.io/github/stars/labuladong/fucking-algorithm?label=Stars&style=flat-square&logo=GitHub"></a>
<a href="https://labuladong.online/algo/" target="_blank"><img class="my_header_icon" src="https://img.shields.io/static/v1?label=精品课程&message=查看&color=pink&style=flat"></a>
<a href="https://www.zhihu.com/people/labuladong"><img src="https://img.shields.io/badge/%E7%9F%A5%E4%B9%8E-@labuladong-000000.svg?style=flat-square&logo=Zhihu"></a>
<a href="https://space.bilibili.com/14089380"><img src="https://img.shields.io/badge/B站-@labuladong-000000.svg?style=flat-square&logo=Bilibili"></a>
</p>

![](https://labuladong.online/algo/images/souyisou1.png)

**通知：[新版网站会员](https://labuladong.online/algo/intro/site-vip/) 即将涨价；已支持老用户续费~另外，建议你在我的 [网站](https://labuladong.online/algo/) 学习文章，体验更好。**



**-----------**

我个人很喜欢使用 Linux 系统，虽然说 Windows 的图形化界面做的确实比 Linux 好，但是对脚本的支持太差了。一开始有点不习惯命令行操作，但是熟悉了之后反而发现移动鼠标点点点才是浪费时间的罪魁祸首。。。

**那么对于 Linux 命令行，本文不是介绍某些命令的具体用法，而是结合使用场景说明一些容易让人迷惑的细节问题和能够提升效率的小技巧**。

1、标准输入和命令参数的区别。

2、在后台运行命令在退出终端后也全部退出了。

3、单引号和双引号表示字符串的区别。

4、有的命令和`sudo`一起用就 command not found。

5、避免输入重复的文件名、重复的路径、重复的命令的方法，以及一些其他小技巧。

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

前文 [Linux文件描述符](https://labuladong.online/algo/other-skills/linux-process/) 说过，管道符和重定向符是将数据作为程序的标准输入，而`$(cmd)`是读取`cmd`命令输出的数据作为参数。

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

![](https://labuladong.online/algo/images/linuxshell/1.png)

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

### 五、输入相似文件名太麻烦

用花括号括起来的字符串用逗号连接，可以自动扩展，非常有用，直接看例子：

```shell
$ echo {one,two,three}file
onefile twofile threefile

$ echo {one,two,three}{1,2,3}
one1 one2 one3 two1 two2 two3 three1 three2 three3
```

你看，花括号中的每个字符都可以和之后（或之前）的字符串进行组合拼接，**注意花括号和其中的逗号不可以用空格分隔，否则会被认为是普通的字符串对待**。

这个技巧有什么实际用处呢？最简单有用的就是给 `cp`, `mv`, `rm` 等命令扩展参数：

```shell
$ cp /very/long/path/file{,.bak}
# 给 file 复制一个叫做 file.bak 的副本

$ rm file{1,3,5}.txt
# 删除 file1.txt file3.txt file5.txt

$ mv *.{c,cpp} src/
# 将所有 .c 和 .cpp 为后缀的文件移入 src 文件夹
```

### 六、输入路径名称太麻烦

**用 `cd -` 返回刚才呆的目录**，直接看例子吧：

```shell
$ pwd
/very/long/path
$ cd # 回到家目录瞅瞅
$ pwd
/home/labuladong
$ cd - # 再返回刚才那个目录
$ pwd
/very/long/path
```

**特殊命令 `!$` 会替换成上一次命令最后的路径**，直接看例子：

```shell
# 没有加可执行权限
$ /usr/bin/script.sh
zsh: permission denied: /usr/bin/script.sh

$ chmod +x !$
chmod +x /usr/bin/script.sh
```

**特殊命令 `!*` 会替换成上一次命令输入的所有文件路径**，直接看例子：

```shell
# 创建了三个脚本文件
$ file script1.sh script2.sh script3.sh

# 给它们全部加上可执行权限
$ chmod +x !*
chmod +x script1.sh script2.sh script3.sh
```

**可以在环境变量 `CDPATH` 中加入你常用的工作目录**，当 `cd` 命令在当前目录中找不到你指定的文件/目录时，会自动到 `CDPATH` 中的目录中寻找。

比如说我常去 `/var/log` 目录找日志，可以执行如下命令：

```shell
$ export CDPATH='~:/var/log'
# cd 命令将会在 ～ 目录和 /var/log 目录扩展搜索

$ pwd
/home/labuladong/musics
$ cd mysql
cd /var/log/mysql
$ pwd
/var/log/mysql
$ cd my_pictures
cd /home/labuladong/my_pictures
```

这个技巧是十分好用的，这样就免了经常写完整的路径名称，节约不少时间。

需要注意的是，以上操作是 bash 支持的，其他主流 shell 解释器当然都支持扩展 `cd` 命令的搜索目录，但可能不是修改 `CDPATH` 这个变量，具体的设置方法可以自行搜索。

### 七、输入重复命令太麻烦

**使用特殊命令 `!!`，可以自动替换成上一次使用的命令**：

```shell
$ apt install net-tools
E: Could not open lock file - open (13: Permission denied)

$ sudo !!
sudo apt install net-tools
[sudo] password for fdl:
```

有的命令很长，一时间想不起来具体参数了怎么办？

**对于 bash 终端，可以使用 `Ctrl+R` 快捷键反向搜索历史命令**，之所以说是反向搜索，就是搜索最近一次输入的命令。

比如按下 `Ctrl+R` 之后，输入 `sudo`，bash 就会搜索出最近一次包含 `sudo` 的命令，你回车之后就可以运行该命令了：

```shell
(reverse-i-search)`sudo': sudo apt install git
```

但是这个方法有缺点：首先，该功能似乎只有 bash 支持，我用的 zsh 作为 shell 终端，就用不了；第二，只能查找出一个（最近的）命令，如果我想找以前的某个命令，就没办法了。

对于这种情况，**我们最常用的方法是使用 `history` 命令配合管道符和 `grep` 命令来寻找某个历史命令**：

```shell
# 过滤出所有包含 config 字段的历史命令
$ history | grep 'config'
 7352  ./configure
 7434  git config --global --unset https.proxy
 9609  ifconfig
 9985  clip -o | sed -z 's/
/,
/g' | clip
10433  cd ~/.config
```
你使用的所有 shell 命令都会被记录，前面的数字就表示这是第几个命令，找到你想重复使用的命令后，也不需要复制粘贴该命令，**只要使用 `!` + 你想重用的命令编号即可运行该命令**。

拿上面的例子，我想重新运行 `git config` 那条命令，就可以这样：

```shell
$ !7434
git config --global --unset https.proxy
# 运行完成
```

我觉得 `history` 加管道加 `grep` 这样打的字还是太多，可以在 你的 shell 配置文件中（`.bashrc`，`.zshrc` 等） 中写这样一个函数：

```shell
his()
{
    history | grep "$@"
}
```

这样就不需要写那么多，只需要 `his 'some_keyword'` 即可搜索历史命令。

我一般不使用 bash 作为终端，我给大家推荐一款很好用的 shell 终端叫做 zsh，这也是我自己使用的 shell。这款终端还可以扩展各种插件，非常好用，具体配置方法可自行搜索。

### 其他小技巧

**1、`yes` 命令自动输入字符 `y` 进行确认**：

我们安装某些软件的时候，可能有交互式的提问：

```shell
$ sudo apt install XXX
...
XXX will use 996 MB disk space, continue? [y/n]
```

一般情况下我们都是一路 y 到底，但如果我们想自动化一些软件的安装就很烦，遇到这种交互式提问就卡住了，还得手动处理。

`yes` 命令可以帮助我们：

```shell
$ yes | your_cmd
```

这样就会一路自动 `y` 下去，不会停下让我们输入了。

如果你读过前文 [Linux 文件描述符](https://labuladong.online/algo/other-skills/linux-process/)，就知道其原理很简单：

你单独运行一下 `yes` 命令，发现它就是打印出一大堆字符 y，通过管道把输出和 `your_cmd` 的标准输入相连接，如果 `your_cmd` 又提出无聊的问题，就会从标准输入读取数据，也就会读取到一个 y 和换行符，和你手动输入 y 确认是一个效果。

**2、特殊变量 `$?` 记录上一次命令的返回值**。

在 Linux shell 中，遵循 C 语言的习惯，返回值为 0 的话就是程序正常退出，非 0 值就是异常退出出。读取上一次命令的返回值在平时使用命令行时感觉没什么用，但是如果你想编写一些 shell 脚本，知道返回值非常有用。

**举个实际的例子**，比如我的 Github 仓库 fucking-algorithm ，我需要给其中所有 markdown 文件最下方添加上一篇、下一篇、目录三个页脚链接，有的文章已经有了页脚，大部分都没有。

为了防止重复添加，我必须知道一个 md 文件下方是否已添加，这时候就可以使用 `$?` 变量配合 `grep` 命令做到：

```shell
#!/bin/bash
filename=$1
# 查看文件尾部是否包含关键词
tail | grep '下一篇' $filename
# grep 查找到匹配会返回 0，找不到则返回非 0 值
[ $? -ne 0 ] && { 添加页脚; }
```

**3、特殊变量 `$$` 记录当前进程的 PID**。

这个功能可能在平时使用时也不怎么用，但是在写 shell 脚本时也非常有用，比如说你要在 `/tmp` 创建临时文件，给文件起名字一直都是非常让人费脑子的，这时候可以使用 `$$` 变量扩展出当前进程的 PID 作为临时文件名，PID 在计算机中都是唯一的，所以绝不会重复，也不需要你记住临时文件的名字。

好了，今天就分享这些技巧吧，如果大家对 Linux 有兴趣，可以点在看分享，数据不错的话下次再写点。



<hr>
<details class="hint-container details">
<summary><strong>引用本文的文章</strong></summary>

 - [Linux 管道符的坑](https://labuladong.online/algo/other-skills/linux-pipeline/)

</details><hr>





**＿＿＿＿＿＿＿＿＿＿＿＿＿**

**《labuladong 的算法笔记》已经出版，关注公众号查看详情；后台回复「**全家桶**」可下载配套 PDF 和刷题全家桶**：

![](https://labuladong.online/algo/images/souyisou2.png)

======其他语言代码======
