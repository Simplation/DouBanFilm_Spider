# DouBanFilm_Spider
采用 Scrapy 爬取豆瓣电影 top250 的数据， 并将数据保存为 CSV 格式。
--------------------------------------------------------------

## 1、首先是安装 scrapy，直接使用 pip 进行安装即可。
    pip install scrapy   
    
## 2、使用 scrapy 创建项目
    scrapy srartproject xxx(项目名)
    
## 3、生成配置文件
    scrapy genspider xxx(项目名) + 域名(要爬取网站的域名)
    
## 4、scrapy 创建的项目结构描述
- scrapy.cfg: 项目的配置文件。
- douban_spider/: 该项目的python模块。之后您将在此加入代码。
- douban_spider/items.py: 项目中的item文件。
- douban_spider/pipelines.py: 项目中的pipelines文件。
- douban_spider/settings.py: 项目的设置文件。
- douban_spider/spiders/: 放置spider代码的目录。

## 5、运行 scrapy 项目
    scrapy crawl xxx(项目名)
    
## 6、数据的保存格式
- 保存 json 文件
    scrapy crawl xxx(项目名) -o xxx(文件名).json
    
- 保存 csv 文件
    scrapy crawl xxx(项目名) -o xxx(文件名).csv
    
## 7、遇到的问题
- xpath 一定要匹配正确，否则无法获取到想要的信息
- 无法获取到数据的原因：settings 没有设置 Item_Piplines
- 存储本地数据库显示乱码：数据库的文件编码没有设置为 ‘utf8’
- 伪装中间件的两种方法：①、设置代理 Ip； ②、设置随机的 User-Agent
- 中间件定义后，千万记住在 settings 中启用，否则无效
- 爬虫的文件名和爬虫名称不能一致，否则会掉坑
