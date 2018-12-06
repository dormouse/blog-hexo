---
title: 使用 Sphinx 生成 PDF 文件
date: 2013-01-27 21:42:37
modified: 2018-12-06 14:25:49
tags:
 - sphinx
 - xetex
 - pdf
 - reStructuredText
 - markdown
category: software
slug: rst-sphinx-pdf
author: Dormouse Young
summary: 如何通过使用 Sphinx 把 reStructuredText （或者 markdown ）生成 PDF 文件。
---

# 简介

本文主要说明如何通过使用 Sphinx 把 reStructuredText （或者 markdown ）生成 PDF 文件。 Sphinx 是一个可以把一系列 reStructuredText 格式文档转换为多种不同格式文档的工具。它具有自动解决交叉引用和编制目录等功能。 Sphinx 支持 html 、 LaTeX 、 ePub 等多种输出格式。现在 Sphinx 已支持 Markdown 格式的源文件。
<!-- more -->

# 安装编译环境

本文的测试环境为 macOS Sierra 10.12.6, Python 3.6.1 。

- 因为 Sphinx 需要 Python 2.7 或者 Python 3.4 以上版本的 Python ，所以首先要检查系统的 Python 是否安装， Python 的版本是否符合要求。如果想要使用 Python3 ，  macOS 下建议使用 brew 安装， Linux 下建议使用 Anaconda 。
- 首先我们创建并激活一个 Python3 虚拟环境。打开终端，输入如下命令：

```shell
$ python3 -m venv rst_pdf
$ cd rst_pdf
$ source bin/activate
```

   激活虚拟环境后提示符最前面会出现 ``(rst_pdf)`` 字样。

- 安装 Sphinx-doc ：

    `pip install -U Sphinx`

- 安装 LaTeX 支持。 macOS 下建议安装 MacTeX ，安装命令为 ``brew cask install mactex`` ，或者到   https://www.tug.org/mactex/mactex-download.html 下载 MacTeX.pkg 后运行安装。注意这个安装包在大小约有 3.14 G 。Linux 下建议安装  [Tex Live](https://tug.org/texlive/)。

# 编写文档

首先使用 ``sphinx-quickstart`` 命令创建一个 Sphinx 项目。这个命令会提出一系列的问题来帮助我们进行项目的设置，每个问题都有默认答案，如果想使用默认答案或者不知道如何回答，那么直接按回车键就可以了。不用担心回答错误，以后可以通过修改配置文件来变更相关设置。以下就是问题示例：

```
Welcome to the Sphinx 1.6.4 quickstart utility.

Please enter values for the following settings (just press Enter to
accept a default value, if one is given in brackets).

Enter the root path for documentation.
> Root path for the documentation [.]:

You have two options for placing the build directory for Sphinx output.
Either, you use a directory "_build" within the root path, or you separate
"source" and "build" directories within the root path.
> Separate source and build directories (y/n) [n]: y
说明：因为我们使用了 Python3 虚拟环境，所以这里我们选择把源文件单独存放在一个目录中。

Inside the root directory, two more directories will be created; "_templates"
for custom HTML templates and "_static" for custom stylesheets and other static
files. You can enter another prefix (such as ".") to replace the underscore.
> Name prefix for templates and static dir [_]:

The project name will occur in several places in the built documentation.
> Project name: rst_pdf
> Author name(s): Dormouse Young

Sphinx has the notion of a "version" and a "release" for the
software. Each version can have multiple releases. For example, for
Python the version is something like 2.5 or 3.0, while the release is
something like 2.5.1 or 3.0a1.  If you don't need this dual structure,
just set both to the same value.
> Project version []:
> Project release []:

If the documents are to be written in a language other than English,
you can select a language here by its language code. Sphinx will then
translate text that it generates into that language.

For a list of supported codes, see
http://sphinx-doc.org/config.html#confval-language.
> Project language [en]: zh_CN

The file name suffix for source files. Commonly, this is either ".txt"
or ".rst".  Only files with this suffix are considered documents.
> Source file suffix [.rst]:

One document is special in that it is considered the top node of the
"contents tree", that is, it is the root of the hierarchical structure
of the documents. Normally, this is "index", but if your "index"
document is a custom template, you can also set this to another filename.
> Name of your master document (without suffix) [index]:

Sphinx can also add configuration for epub output:
> Do you want to use the epub builder (y/n) [n]:

Please indicate if you want to use one of the following Sphinx extensions:
> autodoc: automatically insert docstrings from modules (y/n) [n]:
> doctest: automatically test code snippets in doctest blocks (y/n) [n]:
> intersphinx: link between Sphinx documentation of different projects (y/n) [n]:
> todo: write "todo" entries that can be shown or hidden on build (y/n) [n]:
> coverage: checks for documentation coverage (y/n) [n]:
> imgmath: include math, rendered as PNG or SVG images (y/n) [n]:
> mathjax: include math, rendered in the browser by MathJax (y/n) [n]:
> ifconfig: conditional inclusion of content based on config values (y/n) [n]:
> viewcode: include links to the source code of documented Python objects (y/n) [n]:
> githubpages: create .nojekyll file to publish the document on GitHub pages (y/n) [n]:

A Makefile and a Windows command file can be generated for you so that you
only have to run e.g. `make html' instead of invoking sphinx-build
directly.
> Create Makefile? (y/n) [y]: y
> Create Windows command file? (y/n) [y]: n

Creating file ./source/conf.py.
Creating file ./source/index.rst.
Creating file ./Makefile.

Finished: An initial directory structure has been created.

You should now populate your master file ./source/index.rst and create other documentation
source files. Use the Makefile to build the docs, like so:
   make builder
where "builder" is one of the supported builders, e.g. html, latex or linkcheck.
```



你会发现目录中生成了两个目录和一个文件。
``build`` 目录用于存放输出的内容，比如我们以后要生成的 PDF 文件。
``source`` 目录用于存放用户的源文件。
``Makefile`` 是项目工程文件，方便我们以后生成各种格式的文件。

``source`` 目录下有以下两个目录和两个文件。
``_static`` 目录用于存放用户自定义样式表或者其他静态文件。
``_templates`` 目录用于存放用户自定义的模版。
``conf.py`` 是项目配置文件，以后可以通过修改其中的内容来配置我们的项目。
``index.rst`` 是项目的索引文件，每个 sphinx-doc 项目都至少有一个索引文件。

为了能够正确的生成中文 PDF 文件，我们需要修改 ``conf.py`` 的 ``Options for LaTeX output`` 一节中的 ``latex_elements`` 变量，修改为以下内容：

```
latex_elements = {
    'papersize': 'a4paper',
    # Additional stuff for the LaTeX preamble.
    'preamble': '''
\usepackage{xeCJK}
\usepackage{indentfirst}
\setlength{\parindent}{2em}
\setCJKmainfont[BoldFont=STFangsong, ItalicFont=STKaiti]{STSong}
\setCJKsansfont[BoldFont=STHeiti]{STXihei}
\setCJKmonofont{STFangsong}
''',
}
```

现在可以在 ``source`` 目录下添加我们自己的 reStructuredText 文件。例如本文的源文件就是 ``rst-sphinx-pdf.rst`` 文件。写完后要修改 ``index.rst`` 文件，把新添加的 ``rst-sphinx-pdf.rst`` 文件加入目录树。例如本文的``index.rst`` 内容为：

```
Welcome to rst_pdf's documentation!
===================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   rst_pdf
```

这里扩展名可以省略。

# 生成 PDF 文件

在项目根目录下使用 ``make latex`` 命令生成 tex 文件，最后在 ``build/latex/`` 目录下运行 **两遍** ``xelatex rst_pdf.tex`` 命令即可生成 PDF 文件。

# 一些 Tips

## 让 Sphinx 支持 markdown

Sphinx 是可以支持 markdown 的。要让 Sphinx 支持 markdown ，需要按如下方法操作：

- 安装 recommonmark ：

```
pip install recommonmark
```

- 在 Sphinx 配置文件中的 ``source_parsers`` 变量中添加 Markdown 解析器：

```
source_parsers = {
   '.md': 'recommonmark.parser.CommonMarkParser',
}
```

`.md` 表示 Markdown 文件的扩展名，你可以替换为其他的扩展名。

- 把 Markdown 文件的扩展名添加到配置文件的 ``source_suffix`` 变量中：

```
source_suffix = ['.rst', '.md']
```

- CommonMark 支持添加自定义 Markdown 语法，详见[recommonmark 文档](http://recommonmark.readthedocs.io/en/latest/auto_structify.html)。

## Linux 下安装 TeX Live

- 方法一

使用 ``apt-get install texlive-full`` 命令安装。

- 方法二

去 tex 的 [老家](http://www.tug.org/texlive/acquire-netinstall.html) 下载[install-tl-unx.tar.gz](http://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz) 。解压缩后，运行

```bash
sudo ./install-tl --gui=wizard
```

如果没有安装 wget ，则运行

```bash
sudo apt-get install wget
```

安装输出大致如下

```
输入 “In” 开始安装，一共有2599个项目......
Actions:
<I> start installation to hard disk
<H> help
<Q> quit

Enter command: i
Installing to: /usr/local/texlive/2012
Installing [0001/2599, time/total: ??:??/??:??]: 12many [376k]
Installing [0002/2599, time/total: 00:09/10:05:07]: 2up [66k]
Installing [0003/2599, time/total: 00:10/09:32:46]: Asana-Math [458k]
Installing [0004/2599, time/total: 00:12/05:36:55]: ESIEEcv [137k]
Installing [0005/2599, time/total: 00:15/06:05:39]: FAQ-en [5765k]
......

See /usr/local/texlive/2012/index.html
for links to documentation.  The TeX Live web site
contains updates and corrections: http://tug.org/texlive.

TeX Live is a joint project of the TeX user groups around the world;
please consider supporting it by joining the group best for you. The
list of user groups is on the web at http://tug.org/usergroups.html.
```

```
Add /usr/local/texlive/2012/texmf/doc/man to MANPATH, if not dynamically determined.
Add /usr/local/texlive/2012/texmf/doc/info to INFOPATH.

Most importantly, add /usr/local/texlive/2012/bin/x86_64-linux
to your PATH for current and future sessions.
```

设置路径，把以下内容放在 .bash_profile 中，然后运行 . ~/.bash_profile(ubuntu 下是 ~/.bashrc)

```bash
PATH=$PATH:$HOME/.local/bin:$HOME/bin
PATH=/usr/local/texlive/2012/bin/x86_64-linux:$PATH; export PATH
MANPATH=/usr/local/texlive/2012/texmf/doc/man:$MANPATH; export MANPATH
INFOPATH=/usr/local/texlive/2012/texmf/doc/info:$INFOPATH; export INFOPATH
```

## 如何查看系统中的字体

在 macOS 中可以使用“字体册”应用来查看字体名称。在 Linux 中可以用 ``fc-list`` 命令来获得字体名称。