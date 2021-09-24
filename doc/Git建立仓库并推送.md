## Git建立仓库并推送

1. 安装Git

2. 在Github中新建仓库

   <img src="https://raw.githubusercontent.com/windsoul124/blogPic/main/img/image-20210908093854722.png" alt="image-20210908093854722" style="zoom: 67%;" />

   3.记录仓库地址

   <img src="https://raw.githubusercontent.com/windsoul124/blogPic/main/img/image-20210908094215742.png" alt="image-20210908094215742" style="zoom:67%;" />

   4.在本地项目文件夹中打开Git bash

   5.进行项目初始化和同步

   ```
   #  初始化后会在本地文件夹中创建.git文件
   git init 
   #  把文件夹中所有文件加载
   git add . 
   #  还可以单个加载
   git add index.html
   #  提交文件，创建时间点注释
   git commit -m "init commit"  
   #  随时可以查看git状态
   git status  
   #  将代码库地址添加到本地配置， origin可变
   git remote add origin https://github.com/...  
   #  推送代码
   git push --set-upstream origin master
   ```

   6.Token设置

   Git操作需要Token授权，进入Github个人主页获取Token。选中repo。

   <img src="https://raw.githubusercontent.com/windsoul124/blogPic/main/img/image-20210908095406499.png" alt="image-20210908095406499" style="zoom:67%;" />



注意事项：

1. 在Github中创建项目的默认branch为`main`，如果在push代码时用`master`，则会新建一个分支，想更改需要在`master`分支中的setting中更改为`default`。

2. 或者将Github默认分支名字更改为`master`。

3. 如果将已存在的项目上传，第一次push会提示在线版本和本地版本不同

   

![image-20210924163930100](https://raw.githubusercontent.com/windsoul124/blogPic/main/img/image-20210924163930100.png)

​	解决方案：强制合并两个分支，允许不相关历史提交。

`git pull origin master --allow-unrelated-histories`



