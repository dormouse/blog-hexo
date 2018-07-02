---
title: Write blog with Hexo
date: 2018-06-29 14:32:24
tags:
- hexo
- write
---

I used to write with Sphinx doc. And I'd like to write a blog with some real blog system. Here I choosed Hexo. I almost use Python, so why Hexo? Because I need simply, beautiful, functional.

Here is some note about how to install and use Hexo.

<!-- more -->

# Installation

## Install Node.js

``` bash
$ curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.2/install.sh | bash
$ source .bashrc
$ nvm install stable
```

## Install Hexo

``` bash
$ npm install -g hexo-cli
```

# Create a new blog

``` bash
$ hexo init blog-hexo
$ cd blog-hexo
$ npm install
```

# Quick start
## Create a new post

``` bash
$ hexo new "My New Post"
```

More info: [Writing](https://hexo.io/docs/writing.html)

## Run server

``` bash
$ hexo server
```

More info: [Server](https://hexo.io/docs/server.html)

## Generate static files

``` bash
$ hexo generate
```

More info: [Generating](https://hexo.io/docs/generating.html)

## Deploy to remote sites

``` bash
$ hexo deploy
```

More info: [Deployment](https://hexo.io/docs/deployment.html)

# Theme
## NexT [Reloaded]
next theme now is in new palace:https://github.com/theme-next/hexo-theme-next
Install by following command:
``` bash
$ cd your-hexo-path
$ git clone https://github.com/theme-next/hexo-theme-next themes/next
```
Set theme in main hexo root config ``_config.yml`` file:
```
theme: next
```

next theme docs: https://github.com/theme-next/hexo-theme-next/tree/master/docs/

# Deploy
## Git
Install hexo-deployer-git:
```
$ npm install hexo-deployer-git --save
```
Add folling line in your config file:
```
deploy:
  type: git
  repo: git@github.com:your/repo.github.io.git
```
Then use ``hexo deploy`` to deploy the blog.


# Search

## Install search plugin

``` bash
npm install hexo-generator-search  --save
npm install hexo-generator-searchdb --save
```

## Add following line to `_config.yml` :

```
search:
  path: search.xml
  field: post
  format: html
  limit: 10000
```
## Modify config file (`your-blog-path/themes/next/_config.yml`) of next theme, enable `local_search` :
```
local_search:
  enable: true
  trigger: auto
  top_n_per_article: 1
```

Now start the server, can see the serach button.

# Tags

Create new page use command:

``` bash
$ hexo new page "tags"
```

Now can find a new file named ``your-blog-path/source/tags/index.md``,
change the content to:

```
---
title: tags
date: 2018-07-02 10:18:58
type: "tags"
comments: false
---
```

Modify the Hexo config:
```
menu:
  home: /
  archives: /archives
  tags: /tags
```

Modify the theme config:
```
theme_config:
  menu:
    home: / || home
    tags: /tags/ || tags
```


# Add source file to git
```
git init
git add .
git commit -m "first commit"
git remote add origin git@github.com:your/repo.git
git push -u origin master
```

# REF

* [Hexo docs](https://hexo.io/docs/)
* [hexo-theme-next](https://github.com/theme-next/hexo-theme-next/)
* [Hexo enable local search](https://www.jianshu.com/p/519b45730824)
