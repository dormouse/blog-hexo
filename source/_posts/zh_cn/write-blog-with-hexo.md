---
title: 使用 Hexo 写博客
date: 2018-06-29 14:32:24
modified: 2021-02-28
tags:
 - hexo
 - write
---

原来一直使用 Sphinx 写东西， 2018 年想开始使用一个真正的博客系统来写一些博客，于是选用了 Hexo 。我主要使用 Python 进行开发，那么为什么不选用 Pelican 之类的以 Python 为基础的博客系统呢？因为不够好看，不够方便。下面是我在安装及使用 Hexo 过程中的一些笔记。

<!-- more -->

# 快速开始

## 安装 Hexo

### Install Git

- Windows: Download & install [git](https://git-scm.com/download/win).
- Mac: Install it with [Homebrew](http://mxcl.github.com/homebrew/), [MacPorts](http://www.macports.org/) or [installer](http://sourceforge.net/projects/git-osx-installer/).
- Linux (Ubuntu, Debian): `sudo apt-get install git-core`
- Linux (Fedora, Red Hat, CentOS): `sudo yum install git-core`

### Install Node.js

The best way to install Node.js is with [Node Version Manager](https://github.com/creationix/nvm).
Thankfully the creators of nvm provide a simple script that automatically installs nvm:

cURL:

```bash
$ curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.11/install.sh | bash
```

Wget:

```
$ wget -qO- https://raw.githubusercontent.com/creationix/nvm/v0.33.11/install.sh | bash
```

Once nvm is installed, restart the terminal and run the following command to install Node.js:

```bash
$ nvm install stable
```

Alternatively, download and run [the installer](http://nodejs.org/).

### Install Hexo

Once all the requirements are installed, you can install Hexo with npm:

```bash
$ npm install -g hexo-cli
```


## 创建一个新的博客

``` bash
$ hexo init blog-hexo
$ cd blog-hexo
$ npm install
```

## 创建一个新的博客帖子

``` bash
$ hexo new "My New Post"
```


## 运行服务器

``` bash
$ hexo server
```

这样在浏览器中访问 `http://localhost:4000/` ，就可以看到博客了。

# 获得帮助

Hexo 的官方帮助文档：[英文版](https://hexo.io/docs/)，[中文版](
https://hexo.io/zh-cn/docs/)。

# 如何发布博客
##  生成静态文件

发布博客之前首先要生成静态文件

``` bash
$ hexo generate
```

## 发布到 Git Pages

安装 hexo-deployer-git 插件：

``` bash
$ npm install hexo-deployer-git --save
```

在站点配置文件中加入以下内容：

```
deploy:
  type: git
  repo: git@github.com:your/repo.github.io.git
```

使用 ``hexo deploy`` 命令来发布博客。

更多内容参见： [发布](https://hexo.io/docs/deployment.html)


# Theme

## NexT [Reloaded]

next theme 已经移到[新的地址](https://github.com/theme-next/hexo-theme-next)
通过以下命令安装：

``` bash
$ cd your-hexo-path
$ git clone https://github.com/next-theme/hexo-theme-next themes/next
```

在配置文件中设置 theme 的名称：

```
theme: next
```

把 theme 配置文件中的所有设置提制到站点配置文件的 theme_config 下：
例如：

```
theme_config:
  # Allow to cache content generation. Introduced in NexT v6.0.0.
  cache:
    enable: true
```

更多内容参见 [next theme 文档](https://github.com/theme-next/hexo-theme-next/tree/master/docs/)。

# 本地搜索

## 安装搜索插件

``` bash
npm install hexo-generator-search  --save
npm install hexo-generator-searchdb --save
```

## 修改站点配置文件

```
search:
  path: search.xml
  field: post
  format: html
  limit: 10000
theme_config:
  local_search:
    enable: true
    trigger: auto
    top_n_per_article: 1
```

# Categories

创建 categroies 文件：

``` bash
$ hexo new page categories
```
以上命令会创建一个名为 ``your-blog-path/source/categories/index.md`` 的文件，
把文件内容修改为：
```
---
title: categories
date: 2021-02-28 22:25:30
type: "categories"
comments: false
---
```


# Tags

创建 tags 文件：

``` bash
$ hexo new page "tags"
```

以上命令会创建一个名为 ``your-blog-path/source/tags/index.md`` 的文件，
把文件内容修改为：

```
---
title: tags
date: 2018-07-02 10:18:58
type: "tags"
comments: false
---
```

修改站点配置文件：
```
menu:
  home: /
  archives: /archives
  tags: /tags
theme_config:
  menu:
    home: / || home
    tags: /tags/ || tags
```

# 写作
## 只显示摘要

要实现摘要，只需要在文章开头写好摘要后，另起一行键入 ``<!−− more −−>`` 即可，就像这样：

```
这是摘要
<!-- more -->
这是正文
```

如果不想显示“Read More”而显示别的文字比如“阅读更多”，打开主题的配置文件，按如下设置：

```
excerpt_link: Read More
改为：
excerpt_link: 阅读更多
```

# 把源文件加入 git
```
git init
git add .
git commit -m "first commit"
git remote add origin git@github.com:your/repo.git
git push -u origin master
```

# 参考

* [Hexo 文档](https://hexo.io/docs/)
* [hexo-theme-next 文档](https://github.com/theme-next/hexo-theme-next/)
* [Hexo开启站内搜索功能](https://www.jianshu.com/p/519b45730824)
* [Hexo主页显示摘要](https://ohmyarch.github.io/2014/12/24/Hexo%E4%B8%BB%E9%A1%B5%E6%98%BE%E7%A4%BA%E6%91%98%E8%A6%81/)
