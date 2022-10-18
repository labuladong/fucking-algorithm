# Redis 入侵

<p align='center'>
<a href="https://github.com/labuladong/fucking-algorithm" target="view_window"><img alt="GitHub" src="https://img.shields.io/github/stars/labuladong/fucking-algorithm?label=Stars&style=flat-square&logo=GitHub"></a>
<a href="https://appktavsiei5995.pc.xiaoe-tech.com/index" target="_blank"><img class="my_header_icon" src="https://img.shields.io/static/v1?label=精品课程&message=查看&color=pink&style=flat"></a>
<a href="https://www.zhihu.com/people/labuladong"><img src="https://img.shields.io/badge/%E7%9F%A5%E4%B9%8E-@labuladong-000000.svg?style=flat-square&logo=Zhihu"></a>
<a href="https://space.bilibili.com/14089380"><img src="https://img.shields.io/badge/B站-@labuladong-000000.svg?style=flat-square&logo=Bilibili"></a>
</p>

![](https://labuladong.github.io/algo/images/souyisou1.png)

**通知：[数据结构精品课](https://aep.h5.xeknow.com/s/1XJHEO) 已更新到 V2.0；[第 12 期刷题打卡](https://mp.weixin.qq.com/s/eUG2OOzY3k_ZTz-CFvtv5Q) 最后一天报名；点击这里体验 [刷题全家桶](https://labuladong.gitee.io/algo/images/others/%E5%85%A8%E5%AE%B6%E6%A1%B6.jpg)。另外，建议你在我的 [网站](https://labuladong.gitee.io/algo/) 学习文章，体验更好。**



**-----------**

好吧，我也做了回标题党，像我这么细心的同学，怎么可能让服务器被入侵呢？

其实是这样的，昨天我和一个朋友聊天，他说他自己有一台云服务器运行了 Redis 数据库，有一天突然发现数据库里的**数据全没了**，只剩下一个奇奇怪怪的键值对，其中值看起来像一个 RSA 公钥的字符串，他以为是误操作删库了，幸好自己的服务器里没啥重要的数据，也就没在意。

经过一番攀谈交心了解到，他跑了一个比较古老已经停止维护的开源项目，安装的旧版本的 Redis，而且他对 Linux 的使用不是很熟练。我就知道，他的服务器已经被攻陷了，想到也许还会有不少像我这位朋友的人，不重视操作系统的权限、防火墙的设置和数据库的保护，我就写一篇文章简单看看这种情况出现的原因，以及如何防范。

> PS：这种手法现在已经行不通了，因为新版本 Redis 都增加了 protect mode，增加了安全性，我们只能在本地简单模拟一下，就别乱试了。

### 事件经过

其实这种攻击手法都是 2015 年的事了，那时候 Redis 的安全保护机制比较差，只能靠运维人员来合理配置以保证数据库的安全。有段时间，全球几万个 Redis 节点遭到了攻击，出现了上述奇怪的现象，所有数据被清空，只剩一个键叫 `crackit`，它的值形似 RSA 公钥的字符串。

后来查证，攻击者利用 Redis 动态设置配置和数据持久化的功能，把自己的 RSA 公钥写入到了被攻击服务器的 `/root/.ssh/authored_keys` 这个文件，从而可以用私钥直接登录对方的 root 用户，侵入对方系统。

沦陷的服务器安全防护做的很不好，具体如下：

1、Redis 的端口是默认端口，而且可以从公网访问。

2、Redis 还没设密码。

3、Redis 进程是由 root 用户启动的。

以上每个点都是比较危险的，合在一起，那真是很致命了。且不说别人把公钥写到你的系统里，就说连上你的数据库然后删库，那损失都够大了。那么具体的流程是什么呢，下面我在本地回环地址上简单演示一下。

### 本地演示

Redis 监听的默认端口是 6379，我们设置它接收网卡 127.0.0.1 的连接，这样我从本地肯定可以连接 Redis，以此模拟「从公网可以访问 Redis」这一条件。

现在我是名叫 fdl 的普通用户，我想用 ssh 登录我系统上的 root 用户，要输入 root 的密码，我不知道，所以没办法登录。

除了密码登录之外，还可以使用 RSA 密钥对登录，但是必须要把我的公钥存到 root 的家目录中 `/root/.ssh/authored_keys`。我们知道 `/root` 目录的权限设置是不允许任何其他用户闯入读写的：

![](https://labuladong.github.io/algo/images/redis入侵/1.png)

但是，我发现自己竟然可以直接访问 Redis：

![](https://labuladong.github.io/algo/images/redis入侵/2.png)

如果 Redis 是以 root 的身份运行的，那么我就可以通过操作 Redis，让它把我的公钥写到 root 的家目录中。Redis 有一种持久化方式是生成 RDB 文件，其中会包含原始数据。

我露出了邪恶的微笑，先把 Redis 中的数据全部清空，然后把我的 RSA 公钥写到数据库里，这里在开头和结尾加换行符目的是避免 RDB 文件生成过程中损坏到公钥字符串：

![](https://labuladong.github.io/algo/images/redis入侵/3.png)

命令 Redis 把生成的数据文件保存到 `/root/.ssh/` 中的 `authored_keys` 文件中：

![](https://labuladong.github.io/algo/images/redis入侵/4.png)

现在，root 的家目录中已经包含了我们的 RSA 公钥，我们现在可以通过密钥对登录进 root 了：

![](https://labuladong.github.io/algo/images/redis入侵/5.png)

看一下刚才写入 root 家的公钥：

![](https://labuladong.github.io/algo/images/redis入侵/6.png)

乱码是 GDB 文件的某种编码吧，但是中间的公钥被完整保存了，而且 ssh 登录程序竟然也识别了这段被乱码包围的公钥！

至此，拥有了 root 权限，就可以为所欲为了。。。

### 吸取教训

虽然现在基本不会受到这种攻击（新版本的 Redis 没有密码时默认不对外网开放），但是对于系统的安全性是每个人都应该重视的。

我们自己折腾东西，用个低配云服务器，为了省事儿一般也不认真配置防火墙，数据库不设密码或者设成 admin、root 这样简单的密码，反正也没啥数据。这样肯定不是个好习惯。

现在我们的计算机系统越来越完善，每个成熟的项目都由最优秀的一帮人维护，从技术上说应该算是无懈可击了，那么唯一可能出问题的地方就在于使用它们的人。

就像经常看到有人的 QQ 被盗，我相信盗号的人肯定不是跑到腾讯的数据库里盗号，肯定是 QQ 号主安全防范意识差，在哪个钓鱼网站输入了自己的账号密码，导致被盗。我基本没见过微信被盗的，可能是微信弱化密码登录，改用二维码扫描登录的原因。这应该也算是一种安全方面的考量吧，毕竟微信是有支付功能的。

上面这种骗局对于技术人来说，看看 url，浏览器分析一下网络包就很容易识别出来，但是你还别不信，一般人真的搞不明白怎么识别钓鱼网站和官方网站。就像我真没想到都 2020 年了，还有人在找 Redis 的这个漏洞，而且还有人中招。。。

那么说回 Redis 数据库的使用，在官网上明确写出了安全防护的建议，我简单总结一下吧：

1、不要用 root 用户启动 Redis Server，而且一定要设置密码，而且密码不要太短，否则容易被暴力破解。

2、配置服务器防火墙和 Redis 的 config 文件，尽量不要让 Redis 与外界接触。

3、利用 rename 功能伪装 flushall 这种危险命令，以防被删库，丢失数据。





**＿＿＿＿＿＿＿＿＿＿＿＿＿**

**《labuladong 的算法小抄》已经出版，关注公众号查看详情；后台回复关键词「**进群**」可加入算法群；回复「**全家桶**」可下载配套 PDF 和刷题全家桶**：

![](https://labuladong.github.io/algo/images/souyisou2.png)

======其他语言代码======