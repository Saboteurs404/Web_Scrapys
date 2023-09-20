[TOC]


- 文档：scrapy document

# 一、创建一个scrapy爬虫

首先我们打算爬取** IT新闻 - 博客园 (news.cnblogs.com) **该网站的新闻页
![](https://www.showdoc.com.cn/server/api/attachment/visitFile?sign=b7ca699bdc5cecfaced71eb255c5a2ec&file=file.png)

然后在cmd窗口中进入用来存储新建爬虫项目的文件夹，我们要在“E:\Project\python\Web_scrapy”目录中创建一个爬虫项目文件cnblogs_spider

具体操作如下：

- 1、使用cmd进入后执行以下该命令创建一个scrapy爬虫项目：

```C
scrapy startproject cnblogs_spider
```

![](https://www.showdoc.com.cn/server/api/attachment/visitFile?sign=08a0f843e1d531003ab736963b3d5106&file=file.png)


- 2、然后使用如下命令创建爬取博客园（news.cnblogs.com）的scrapy爬虫：

**注意：爬虫名字不能和项目名称一致**

```C

//scrapy genspider 爬虫名称 "域名"   
// 注意：爬虫名字不能和项目名称一致。

// 创建爬取博客园的爬虫
scrapy genspider cnblogs news.cnblogs.com
//www不用写
```
![](https://www.showdoc.com.cn/server/api/attachment/visitFile?sign=7f47db097683e72297f5d26309287d24&file=file.png)

pycharm截图：
![](https://www.showdoc.com.cn/server/api/attachment/visitFile?sign=3b7d8f4f2f9c7a62222ba38560940c23&file=file.png)
















