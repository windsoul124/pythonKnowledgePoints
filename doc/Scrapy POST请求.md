## Scrapy POST请求

##### Google Play：

三个关键参数：

1. 接口
   

   ![](https://raw.githubusercontent.com/windsoul124/blogPic/main/img/image-20210913185841145.png)

2. 参数类型
   

   ![image-20210913185853213](https://raw.githubusercontent.com/windsoul124/blogPic/main/img/image-20210913185853213.png)

3. 参数形式

   

   ![image-20210913190045806](https://raw.githubusercontent.com/windsoul124/blogPic/main/img/image-20210913190045806.png)

   

POST需重写`start_request(self)`函数：

```python
    def start_requests(self):

        data = {
            'f.req': '[[["xdSrCf","[[null,[\\"com.sc.scorecreator\\",7],[]]]",null,"1"]]]',
           
        }
        for url in self.start_urls:
            yield scrapy.FormRequest(url, headers={"content-type": "application/x-www-form-urlencoded"}, formdata=data, callback=self.parse)
```

`FormRequest()`发起`POST`请求，`headers`中加入传参类型，`formdata`中为传递数据，`callback`则为回调函数。



