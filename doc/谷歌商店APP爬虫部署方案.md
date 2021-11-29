## 谷歌商店APP爬虫部署方案

1. 项目文件

   针对四个国家的爬虫项目

   `app_from_nga`

   `app_from_ken`

   `app_from_vn`

   `app_from_ph`

2. 项目依赖

   `python3`

   其他需要的包在每个项目中的`requirements.txt`文件中

3. 部署流程

   进入任意一个项目目录，执行：

   `pip install -r requirements`安装项目依赖包

   四个爬虫需要分别进入项目目录启动，运行其中的`start_<国家名>`文件

   例：`python start_ken`

   四个爬虫同时启动对于网络和系统压力较大，运行时间：

   `app_from_ken`<`app_from_nga`<`app_from_ph`<`app_from_vn`

4. 测试流程

   注释掉每个项目中`settings`文件的

   ```
   # ITEM_PIPELINES = {
   #    'app_from_ken.pipelines.AppFromKenPipeline': 300,
   # }
   ```

   测试成功后注释回来就会写入`adb`

   

   2021.11.22

   

   

   

