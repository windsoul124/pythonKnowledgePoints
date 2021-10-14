## 更改pip国内镜像源

注意开启代理时无法通过国内镜像源获取包。

1. Windows更改pip镜像源

   - 进入 `C:\Users\Administrator\AppData\Roaming` 路径下

   - 找到`pip`文件夹，更改其中的`pip.ini`文件。如果没有文件夹则新建同名文件夹和同名配置文件。

     ```
     [global]
     timeout = 6000
     index-url = https://pypi.tuna.tsinghua.edu.cn/simple
     trusted-host = https://pypi.tuna.tsinghua.edu.cn/simple
     ```

   

2. 更改pip源

   - 在用户的家目录下创建名为`.pip`文件夹

   - 在.pip文件夹中创建名为`pip.con`f的文件

   - 在`pip.conf`文件中输入以下内容

     ```
     [global]
     timeout = 6000
     index-url = https://pypi.tuna.tsinghua.edu.cn/simple
     trusted-host = https://pypi.tuna.tsinghua.edu.cn/simple
     ```

   

3. 镜像源

   - 中国科学技术大学 https://pypi.mirrors.ustc.edu.cn/simple
   - 清华 https://pypi.mirrors.ustc.edu.cn/simple
   - 阿里云 https://pypi.mirrors.ustc.edu.cn/simple
   - 豆瓣 https://pypi.mirrors.ustc.edu.cn/simple

