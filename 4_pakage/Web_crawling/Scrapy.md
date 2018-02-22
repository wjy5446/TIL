# Scrapy

### Srapy 순서

1. Srapy 프로젝트 생성
2. Item 정의
3. spider 작성하고 Item 추출
4. 저장할 Item의 pipeLine 작성



### Creating a project

`scarpy startporject crawler`



##### 프로젝트의 구조

```
├── gb_crawler
│   ├── __init__.py
│   ├── __pycache__
│   ├── items.py
│   ├── middlewares.py
│   ├── pipelines.py
│   ├── settings.py
│   └── spiders
│       ├── __init__.py
│       └── __pycache__
└── scrapy.cfg
```



- `spider` : 각 웹페이지 어떤 부분을 스크래핑 할 것인지 명시하는 클래스
- `Selector` : HTML Element를 선택하는 메커니즘을 구현한 클래스, Xpath를 사용을 권장
- `items.py` : 스크랩을 저장할 때 사용하는 사용자 정의 자료 구조 클래스 (데이터 형태 지정)
- `pipeline.py` : 가공하거나 다양한 형태로 저장할 수 있는 클래스 (데이터 변형 지정)
- `settings.py` : 세부적인 설정 사항 지재
  - ROBOTSTXT_OBEY = True : 허락되는 곳만 가져온다.




### Define Item

**Item** : 스크랩된 데이터를 담고 있는 컨테이너



##### scrapy 클래스 선언

```
import scrapy

class DmozItem(scraoy.Item):
  title = scrapy.Field()
  link = scrapy.Field()
  desc = scrapy.Field()
```



##### Field 

Field를 이용해 속성을 정의



### Make Spider

스파이더 : URL 링크를 어떻게 따라 갈지 어떻게 Parse할 지 정의



```
import scrapy

class DmozSpider(scrapy.Spider):
  name = "dmoz"
  allowed_domains = ["dmoz.org"]
  start_urls = ["http://www.naver.com"]
  
  def parse(Self, response):
  	filename = response.url.split()
```

- `name` : spider 이름 정의
- `start_url` : 처음 크롤링할 url의 위치  
- `parse()` : start_url에서 가져온 response 데이터를 파싱하고 데이터 추출하고 다음에 올 url 추출.




##### Scrapy Engine의 동작 방법

1. start_urls에 있는 URL의 scrapy.Request 객체 생성
2. 콜백함수로써 parse() 메세드 할당
3. parse() 메세드를 통해 scrapy.http.Response 객체 반환




##### Selector 기본 메소드

- `xpath("xpath")` : 셀렉터 리스트 반환 (xpath 표현에 의해 선택된 노드)
- `css("css")` : 셀렉트 리스트 반환 (css 표현에 의해 선택된 노드)
- `extract()` : 선택된 데이터를 가진 유니코드 string를 반환
- `re(""re)` : 주어진 정규 표현식을 적용하여 리스트 반환



### Crawling

`scrapy crawl dmoz` : 추가한 dmoz 스파이더 실행



##### Following link

```
def parse(self, response):
  for href in reponse.xpath():
    url = response.urljoin(href.extract())
    yeild scrapy.Request(url, callback=self.parse_dir)
    
def par_dir(self, reponse):
  for sel in response.xpath():
    item = DmozItem()
    item['title'] = sel.xpath().extract()
    yeild item
```



### Storing the scrap data

`scrapy crawl dmmoz -0 items.json`



##### Pipeline

```
import csv

class GbCrawlerPipeline(object):

    def __init__(self):
        self.csvwriter = csv.writer(open("GmarketBestsellers.csv", "w"))
        self.csvwriter.writerow(["title","o_price","s_price","discount_rate"])

    def process_item(self, item, spider):
        row = []
        row.append(item["title"])
        row.append(item["o_price"])
        row.append(item["s_price"])
        row.append(item["discount_rate"])
        self.csvwriter.writerow(row)
        return item
```





========================================

### 파이썬으로 scrapy 사용

##### 선언

```
import requests
from scrapy.http import TextResponse
```



##### Xpath를 이용한 스크래핑

```
req = requests.get('http://www.naver.com)
response = TextResponse(req.url, body=req.text, encoding='utf-8')
```



**Xpath 텍스트 가져오기**

`response.xpath("xPath/text()").extract()` : text()를 추가



**Xpath 텍스트 여러개 가져오기**

`response.xpath(xPath/text()).extract()`

