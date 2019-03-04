Python Note 100 - File
**********************

:date: 2017-02-13
:modified: 2017-02-13
:slug: python-note-100-file
:tags: python, note, file
:category: Development
:author: Dormouse Young
:summary: Python note series 100 - file


打开文件
========

打开文件示例::

    with open("/tmp/foo.txt") as file:
        data = file.read()

    with open('examples/favorite-people.txt', encoding='utf-8') as a_file:
        for a_line in a_file:
            line_number += 1
            print('{:>4} {}'.format(line_number, a_line.rstrip()))

使用字符串的 format() 方法可以打印出行号和行自身。格式说明符 {:>4} 的意思是
“使用最多四个空格使之右对齐，然后打印此参数。”变量 a_line 是包括回车符等在
内的完整的一行。字符串方法rstrip()可以去掉尾随的空白符，包括回车符。

写入文件
========

写入文件示例::

    with open(csvfile, 'w') as f:
        f.writelines(linelist)
    f.close()

关于 open 模式
==============

open 的模式如下表：

==== ==============================================
命令 说明
==== ==============================================
 r   以读方式打开
 w   以写方式打开
 a   以追加模式打开 (从 EOF 开始, 必要时创建新文件)
 r+  以读写模式打开
 w+  以读写模式打开 (参见 w )
 a+  以读写模式打开 (参见 a )
 rb  以二进制读模式打开
 wb  以二进制写模式打开 (参见 w )
 ab  以二进制追加模式打开 (参见 a )
 rb+ 以二进制读写模式打开 (参见 r+ )
 wb+ 以二进制读写模式打开 (参见 w+ )
 ab+ 以二进制读写模式打开 (参见 a+ )
==== ==============================================

相关函数
========

* fp.read([size]) #size为读取的长度，以byte为单位
* fp.readline([size]) #读一行，如果定义了size，有可能返回的只是一行的一部分
* fp.readlines([size]) #把文件每一行作为一个list的一个成员，并返回这个list。其实它的内部是通过循环调用readline()来实现的。如果提供size参数，size是表示读取内容的总长，也就是说可能只读到文件的一部分。
* fp.write(str) #把str写到文件中，write()并不会在str后加上一个换行符
* fp.writelines(seq) #把seq的内容全部写到文件中(多行一次性写入)。这个函数也只是忠实地写入，不会在每行后面加上任何东西。
* fp.close() #关闭文件。python会在一个文件不用后自动关闭文件，不过这一功能没有保证，最好还是养成自己关闭的习惯。  如果一个文件在关闭后还对其进行操作会产生ValueError
* fp.flush() #把缓冲区的内容写入硬盘
* fp.fileno() #返回一个长整型的”文件标签“
* fp.isatty() #文件是否是一个终端设备文件（unix系统中的）
* fp.tell() #返回文件操作标记的当前位置，以文件的开头为原点
* fp.next() #返回下一行，并将文件操作标记位移到下一行。把一个file用于for … in file这样的语句时，就是调用next()函数来实现遍历的。
* fp.seek(offset[,whence]) #将文件打操作标记移到offset的位置。这个offset一般是相对于文件的开头来计算的，一般为正数。但如果提供了whence参数就不一定了，whence可以为0表示从头开始计算，1表示以当前位置为原点计算。2表示以文件末尾为原点进行计算。需要注意，如果文件以a或a+的模式打开，每次进行写操作时，文件操作标记会自动返回到文件末尾。
* fp.truncate([size]) #把文件裁成规定的大小，默认的是裁到当前文件操作标记的位置。如果size比文件的大小还要大，依据系统的不同可能是不改变文件，也可能是用0把文件补到相应的大小，也可能是以一些随机的内容加上去。

shutil 操作
===========

复制文件：

* shutil.copyfile("oldfile","newfile") oldfile 和 newfile 都只能是文件。
* shutil.copy("oldfile","newfile") oldfile 只能是文件夹， newfile 可以是文件，
  也可以是目标目录

复制文件夹：

* shutil.copytree("olddir","newdir") olddir和newdir都只能是目录，且newdir必须不存在

移动文件（目录）：

* shutil.move("oldpos","newpos")

删除目录：

* shutil.rmtree("dir")    空目录、有内容的目录都可以删

os 和 os.path 模块
==================

* os.mkdir("file")：创建目录
* os.rmdir("dir")：只能删除空目录
* os.listdir(dirname)：列出dirname下的目录和文件
* os.getcwd()：获得当前工作目录
* os.curdir：返回当前目录（'.')
* os.chdir(dirname)：改变工作目录到dirname
* os.remove("file")：删除文件
* os.rename("oldname","newname")：重命名文件（目录），文件或目录都是使用这条命令
* os.path.isdir(name)：判断name是不是一个目录，name不是目录就返回false
* os.path.isfile(name)：判断name是不是一个文件，不存在name也返回false
* os.path.exists(name)：判断是否存在文件或目录name
* os.path.getsize(name)：获得文件大小，如果name是目录返回0L
* os.path.abspath(name)：获得绝对路径
* os.path.normpath(path)：规范path字符串形式
* os.path.split(name)：分割文件名与目录（事实上，如果你完全使用目录，它也
  会将最后一个目录作为文件名而分离，同时它不会判断文件或目录是否存在）
* os.path.splitext()：分离文件名与扩展名，返回一个tuple：("aaa",".txt")
* os.path.join(path,name)：连接目录与文件名或目录
* os.path.basename(path)：返回文件名
* os.path.dirname(path)：返回文件路径

获得同一后缀名的文件
====================

示例::

    import glob
    for filename in glob.glob("*.xls"):
         print filename

获得文件的权限
==============

示例::

    >>>import stat
    >>>import os
    >>>oct(stat.S_IMODE(os.lstat("soft").st_mode))
    '0755'

    >>>oct(os.stat("soft")[stat.ST_MODE])
    '040755'

    >>>oct(os.stat("soft").st_mode & 0777)
    '0755'

常用常数::

    S_IRWXU 00700   mask for file owner permissions
    S_IRUSR 00400   owner has read permission
    S_IWUSR 00200   owner has write permission
    S_IXUSR 00100   owner has execute permission
    S_IRWXG 00070   mask for group permissions
    S_IRGRP 00040   group has read permission
    S_IWGRP 00020   group has write permission
    S_IXGRP 00010   group has execute permission
    S_IRWXO 00007   mask for permissions for others (not in group)
    S_IROTH 00004   others have read permission
    S_IWOTH 00002   others have write permission
    S_IXOTH 00001   others have execute permission

