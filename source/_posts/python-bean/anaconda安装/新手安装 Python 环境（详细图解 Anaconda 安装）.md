---
title: 新手安装 Python 环境（详细图解 Anaconda 安装）
date: 2021-02-17
modified: 2021-02-17
permalink: python-install
tags:
 - python
 - install
category: Python
author: Dormouse Young
summary: Python Install
---

# 关于新手 Python 环境的选择 

Linux 操作系统和 MAC 一般是自带 Python 的，可以直接使用 Python 。而 Windows 操作一般是不带 Python 的。所以，在 Windows 中，必须先安装安装 Python 环境才能学习和使用 Python 。针对不同的需求，不同的环境，Python 环境的搭建方式是多种多样。对于新手来说，我觉得 Anaconda 是一个相当好的选择。 Anaconda 是一个 Python 发行套装。现在（2021年2月17日），最新版本的 Anaconda 包含 Python 3.8 和其他丰富的用于科学计算的包（conda, numpy, scipy, ipython notebook等）。 Anaconda 有以下主要特点：
1. 开源
2. 安装过程简单
3. 高性能使用Python和R语言
4. 免费的社区支持
5. 支持 Windows 、Linux 和 MAC 。

<!-- more -->

# 下载 Anaconda
Anaconda 的官方下载地址是：https://www.anaconda.com/products/individual#Downloads ，
在这个页面点击 Python 3.8 64-Bit Graphical Installer (457 MB) 即可下载。
对于国内用户来说，官方下载地址的下载速度可能有些慢，我们可以在国内的镜像源来下载，比如清华大学开源软件镜像站：
https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/
Anaconda3-2020.11-Windows-x86_64.exe

# 安装 Anaconda
双击 Anaconda3-2020.11-Windows-x86_64.exe 会出现安装界面，点击 Next：
![Anaconda 安装1](https://img-blog.csdnimg.cn/20210217163952667.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21vdXNlMjAxOA==,size_16,color_FFFFFF,t_70)
点击 I Agree ：
![Anaconda 安装2](https://img-blog.csdnimg.cn/20210217164133751.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21vdXNlMjAxOA==,size_16,color_FFFFFF,t_70)
这里选择第二个， All Users ：
![Anaconda 安装3](https://img-blog.csdnimg.cn/20210217164243462.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21vdXNlMjAxOA==,size_16,color_FFFFFF,t_70)
然后点击 Next ：
![Anaconda 安装4](https://img-blog.csdnimg.cn/20210217164338661.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21vdXNlMjAxOA==,size_16,color_FFFFFF,t_70)
点击 Next ：
![Anaconda 安装5](https://img-blog.csdnimg.cn/20210217164338674.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21vdXNlMjAxOA==,size_16,color_FFFFFF,t_70)
把两个勾选框都选上：
![Anaconda 安装5](https://img-blog.csdnimg.cn/20210217164338687.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21vdXNlMjAxOA==,size_16,color_FFFFFF,t_70)
然后点击 Install ：
![Anaconda 安装6](https://img-blog.csdnimg.cn/20210217164338696.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21vdXNlMjAxOA==,size_16,color_FFFFFF,t_70)
程序开始安装：
![Anaconda 安装7](https://img-blog.csdnimg.cn/20210217164338700.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21vdXNlMjAxOA==,size_16,color_FFFFFF,t_70)
安装完成，点击 Next ：
![Anaconda 安装8](https://img-blog.csdnimg.cn/20210217164338702.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21vdXNlMjAxOA==,size_16,color_FFFFFF,t_70)
点击 Next ：
![Anaconda 安装9](https://img-blog.csdnimg.cn/20210217164338712.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21vdXNlMjAxOA==,size_16,color_FFFFFF,t_70)
点击 Finish，安装结束：
![Anaconda 安装10](https://img-blog.csdnimg.cn/20210217164338740.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21vdXNlMjAxOA==,size_16,color_FFFFFF,t_70)
在 Windows 的形如菜单可以看到，最近添加里有两个新项目，一个是 Anaconda Powershell Prompt ，还有一个是 Jupyter Notebook 。
![Anaconda 安装11](https://img-blog.csdnimg.cn/20210217164338753.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21vdXNlMjAxOA==,size_16,color_FFFFFF,t_70)

我们打开 Anaconda Powershell Prompt ，输入：
`>>> Python -V`
如果显示：
`Python 3.8.5` ，那么就表示安装成功。
![Anaconda 安装12](https://img-blog.csdnimg.cn/2021021716593014.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21vdXNlMjAxOA==,size_16,color_FFFFFF,t_70)

