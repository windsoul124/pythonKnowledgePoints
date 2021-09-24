Scrapy的request的meta参数

- `scrapy.Request`和`scrapy.FormRequest`都可以传入`meta`参数，是为了将数据传递给回调函数。
- `meta`为字典形式，须自己构建键值对
- 回调函数中获取数据`response.meta['data']`

主要应用场景为同一个`item`需要多次解析才能填充完整。或者解析函数需要用到重写后的请求函数中的参数。

```python
# POST请求需要重写请求函数
def start_requests(self):
    # FormRequest为POST请求
    yield scrapy.FormRequest(self.start_url, 
                            headers=headers, 
                            callback=self.parse,
                            meta={'data':self.start_url})
    
def parse(self, response):
    data = response.meta['data']
```

