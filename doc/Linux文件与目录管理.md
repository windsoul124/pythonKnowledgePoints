Linux文件与目录管理

​	Linux的目录结构为树状结构，最顶级的目录为根目录`/`。其他目录通过挂载可以将他们添加到树中，通过解除挂载可以移除他们。

- 绝对路径：

  由根目录`/`写起，例如`/home/python/doc`

- 相对路径：

  不是由`/`写起，例如由`/home/python/doc`到`/home/python/pic`就可以输入`cd ../`

#### 处理目录的常用命令

- `ls`(list files)：列出目录和文件名
- `cd`(change directory)：切换目录
- `pwd`(print work directory)：显示目前的目录
- `mkdir`(make directory)：创建一个新的目录
- `rmdir`(remove directory)：删除一个空的目录
- `cp`(copy file)：复制文件或目录
- `rm`(remove file)：删除文件或目录
- `mv`(move file)：移动文件或目录，或修改文件与目录的名称

##### ls（列出目录）

参数：

- `-a`：全部的文件，连同隐藏文件（开头为`.`的文件）一起列出来
- `-d`：仅列出目录本身，而不是列出目录内的文件数据
- `-l`：长数据串列出，包含文件的属性与权限等数据

将家目录下的所有文件列出来（含属性与隐藏档）

`ls -al ~`

##### cd（切换目录）

```python
# 使用绝对路径
cd /home/python
# 使用相对路径
cd ./python
# 回到自己的家目录
cd ~
# 回到上一级目录
cd ..
```

##### pwd（显示目前所在的目录）

`pwd`是Print Working Directory的缩写，也就是显示当前目录的命令。

参数：

- `-p`显示出确实的路径，而非使用连结（link）路径。
- 