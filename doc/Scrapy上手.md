## Scrapy上手

### 基本架构

![Scrapy流程](C:\Users\NINGMEI\Desktop\Scrapy流程.png)

- **Scrapy Engine(引擎)**:负责Spider、Itempipeline、Downloader、Scheduler中间的通讯，信号，传递
- **Scheduler(调度器)**：负责接收引擎发送过来的Request请求，并按照一定的方式进行整理排列、入列，当引擎需要时，再次还给引擎
- **Downloader(下载器)**:负责下载Engine发送过来的所有Request请求，并将其获取到的Response交还给Engine，由引擎交给Spider来处理
- **Spider(爬虫)**:负责处理所有的Response，从中分析提取数据，获取item字段需要的数据，并将需要跟进的URL提交给引擎，再次进入Scheduler
- **Itempipeline(管道)**:负责处理Spider中获取到的item，并进行后期处理（详细分析、过滤、存储）
- **DownloaderMiddlewares(下载中间件)**：当作一个可以自定义扩展下载功能的组件
- **SpiderMiddlewares(Spider中间件)**:当作一个可以自定义扩展和操作引擎的Spider中间通信的功能组件（比如进入Spider的Response，和从Spider出去的Request）

### 爬虫流程

1. 创建Scrapy项目
   `scrapy startproject projectname`
2. 明确目标
   编写`items.py`，明确抓取目标
3. 制作爬虫
   `spiders/xxspider.py`，制作爬虫爬取网页
4. 存储内容
   `pipelines.py`，设计管道存储爬取内容

### 结构文件

##### items.py

`items.py`定义结构化数据字段，用来保存爬取的数据

创建一个`scrapy.Item`类，并且定义类型为`scrapy.Field`的类属性来定义一个Item

```python
import scrapy

class ItcastItem(scrapy.item):
    name = scrapy.Field()
    title = scrapy.Field()
    info = scrapy.Field()
```

##### spiders/itcastSpiders.py

爬虫功能分两步：

1. 爬数据

建立爬虫文件并制定爬虫名和爬取域

```python
scrapy genspider itcast "itcast.cn"
```

目录`spiders`下生成`itcast.py`文件，自动生成以下代码

```python
import scrapy

class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ["http://www.itcast.cn/channel/teacher.shtml"]

    def parse(self, response):
        pass
```

建立一个spider必须创建一个`scrapy.Spider`的**子类**，并确定**三个强制属性**和**一个方法**

- `name = ''`：这个是爬虫的识别名称，用来识别项目中的爬虫
- `allow_domains = []：搜索的域名范围，也就是爬虫的约束区域，爬虫只爬取这个域名下的网页
- `start_urls = ()`：爬取的URL元组/列表，必须为可迭代形式。爬虫从这里抓取数据，第一次爬取会从这个URL开始，后续会从它的子URL中继承性生成
- `parse(self, response)`：解析的方法，每个初始URL完成下载后调用，调用后传入从每一个URL得到的Response对象作为唯一参数，主要作用：
  - 负责解析返回的`response.body`数据，提取结构化数据并生成item
  - 生成需要下一页的URL请求

2.取数据

xpath规则提取response对象数据

常用规则

- `//ul`：全局选择所有`<ul>`元素
- `//div[@class='mine']`：全局选择具有`class='mine'`属性的`div`元素

将建立好的`items.py`模型文件导入，pycharm需要将项目文件夹设置为资源文件夹

![image-20210909193056781](https://raw.githubusercontent.com/windsoul124/blogPic/main/img/image-20210909193056781.png)

```python
from tutorial.items import ItcastItem
```

将得到的数据封装到`items.py`定义的对象中，保存老师的每个属性

```python
import scrapy
from tutorial.items import ItcastItem

class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.com']
    start_urls = ["http://www.itcast.cn/channel/teacher.shtml"]

    def parse(self, response):
        # 存放老师信息的集合
        items = []
        for each in response.xpath("//div[@class='li_txt']"):
            #  信息封装到对象中
            item = ItcastItem()
            #  extract()返回的都是unicode字符串
            name = each.xpath("h3/text()").extract()
            title = each.xpath("h4/text()").extract()
            info = each.xpath("p/text()").extract()

            #  xpath返回的是包含一个元素的列表
            item['name'] = name[0]
            item['title'] = title[0]
            item['info'] = info[0]

            items.append(item)
        return items
```

scrapy保存信息的最简单的方法主要是四种， -o输出制定格式的文件：

##### json格式，默认为Unicode编码

`scrapy crawl itcast -o teachers.json`

##### json lines格式，默认为Unicode编码

`scrapy crawl itcast -o teachers.jsonl`

##### csv逗号表达式，可用Excel打开

`scrapy crawl itcast -o teachers.csv`

##### xml格式

`scrapy crawl itcast -o teachers.xml`