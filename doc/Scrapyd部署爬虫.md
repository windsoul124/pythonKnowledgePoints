Scrapyd部署爬虫

服务端：scrapyd

客户端：scrapyd-client



1. 服务端搭建

   测试环境为Windows，生产坏境为Linux，安装方式相同。

   `pip install scrapyd`

   修改scrapyd配置

   Windows：`./Anaconda3/Lib/site-packages/scrapyd/default_scrapyd.conf`

   Linux: 

   查找scrapyd的路径

   `find / -name scrapyd`

   修改scrapyd的配置，暴露端口可远程访问

   `/root/anaconda3/lib/python3.8/site-packages/scrapyd/default_scrapyd.conf`

   ```python
   # 暴露端口 
   bind_address = 0.0.0.0
   ```

2. 客户端搭建

   `pip install scrapyd-client`

   