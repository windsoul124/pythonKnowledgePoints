## Docker容器修改端口映射



> 服务器更换内网IP地址之后，连接Mysql失败。进入容器确定Mysql服务没有问题之后，有以下两种思路排查：

**方式一**：修改指定容器的映射端口（用此办法解决）

**查看docker正在运行的容器**

`docker ps -a`

**查看容器运行的端口**

`docker port 容器ID`

**查看容器的完整ID**

`docker inspect 容器ID |grep Id`

若docker还在运行，**在容器外关闭容器**

`docker stop 容器ID`

**停止docker服务**

`systemctl stop docker`

进入`/var/lib/docker/containers`找到该容器ID的文件夹，修改其中的`config.v2.json`和`hostconfig.json`文件

`config.v2.json`

![image-20211129173908833](https://raw.githubusercontent.com/windsoul124/blogPic/main/img/image-20211129173908833.png)

在`ExposedPorts`中修改或增加宿主机开放的端口，注意不要端口冲突

`hostconfig.json`

![image-20211129174121562](https://raw.githubusercontent.com/windsoul124/blogPic/main/img/image-20211129174121562.png)

在`PortBindings`中修改或增加宿主机开放的端口

改动完成后启动docker

`system start docker`

启动容器

`docker start 容器ID`

**方式二**：将现有的容器打包成镜像，使用新的镜像运行容器时重新制定要映射的端口

**停止现有容器**

`docker stop 容器ID`

**将容器commit成为一个镜像**

`docker commit 容器ID 新的镜像名`

**用新镜像运行容器**

`docker run -it -d --name 容器ID -p p1:p2 -p p2:p2 新的镜像名`

**检查服务是否正常**

`ps -ef|grep docker`

检查`/usr/bin/docker-proxy`下是否有设置映射的端口，存在则docker成功启动

