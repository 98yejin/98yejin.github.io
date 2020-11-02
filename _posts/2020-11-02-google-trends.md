---
layout: post
title: Python scrapy, beautifulsoup(bs4) 구글 트렌드 데이터 스크래핑, 언어별 API
subtitle: python, scrapy, bs4
tags: [python, scrapy, bs4, google trends]
comments: true
---

## 1. Google Trends🍳?

![google-trends](https://github.com/98yejin/98yejin.github.io/blob/master/assets/img/1102/googletrends.PNG?raw=true)

> Google Trends is a website by Google that analyzes the popularity of top search queries in Google Search across various regions and languages.

Google 트렌드는 다양한 지역과 언어에서 Google 검색의 인기 검색어의 인기를 분석하는 Google 웹 사이트입니다. 웹 사이트는 그래프를 사용하여 시간에 따른 여러 검색어의 검색 량을 비교합니다.

- 위키백과(https://en.wikipedia.org/wiki/Google_Trends)

## 2. Scraping vs Crawling🍟

[웹 크롤링과 웹 스크래핑의 차이점]()

## 3. (예시)Google Trends 를 사용해서 할 수 있는 것 🌭

![corona-virus01](https://github.com/98yejin/98yejin.github.io/blob/master/assets/img/1102/trend2.PNG?raw=true)

이렇게 국가별, 지역별 코로나 바이러스 검색량도 볼 수 있고,

![corona-virus02](https://github.com/98yejin/98yejin.github.io/blob/master/assets/img/1102/trend3.PNG?raw=true)

특정 기간의 검색량도 볼 수 있다.

코로나 바이러스는 단순한 예시일 뿐이고, 이외에도 다양한 키워드를 검색하고 분석할 수 있다.

그외에도

![search](https://github.com/98yejin/98yejin.github.io/blob/master/assets/img/1102/trend4.PNG?raw=true)

이렇게 일별 인기 급상승 검색어도 볼 수 있다. 네이버 실시간 검색어가 보기 불편해진만큼, 구글의 일별 인기 급상승 검색어를 꽤 유용하게 쓰고 있다.

약간 아쉬운 점은 한국에서는 실시간 검색어를 지원하지 않는다는 것 정도..?

참고로 일별 인기 급상승 검색어는 html 로 바로 가져올 수 있게 지원해준다. 
```
<script type="text/javascript" src="https://ssl.gstatic.com/trends_nrtr/2213_RC01/embed_loader.js"></script> <script type="text/javascript"> trends.embed.renderWidget("dailytrends", "", {"geo":"KR","guestPath":"https://trends.google.com:443/trends/embed/"}); </script> 
```

구글 트렌드는 이 외에도 다양한 기능을 제공한다.

## 4. Scrapy로 일별 인기 급상승 검색어 스크랩🍱

```python
import scrapy

class ScrapeSpider(scrapy.Spider):
    name = 'scrape-trends'
    allowed_domains = ['https://trends.google.com/trends/trendingsearches/daily/rss?geo=KR']
    start_urls = ['https://trends.google.com/trends/trendingsearches/daily/rss?geo=KR']
 
    def start_requests(self):
        urls = [
            'https://trends.google.com/trends/trendingsearches/daily/rss?geo=KR',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
 
    def parse(self, response):
        for post in response.xpath('//channel/item'):
            yield {
                'title' : post.xpath('title//text()').extract_first(),
                'link': post.xpath('link//text()').extract_first(),
                'pubDate' : post.xpath('pubDate//text()').extract_first(),
            }
            
```

## 5. BeautifulSoup으로 일별 인기 급상승 검색어 스크랩🍗

```python
import time
import re
import requests
from bs4 import BeautifulSoup

# https://codereview.stackexchange.com/questions/208277/web-scraping-google-trends-in-python
def fetch_xml(country_code):
    url = f"https://trends.google.com/trends/trendingsearches/daily/rss?geo={country_code}"
    start = time.time()
    response = requests.get(url)
    response_time = time.time() - start
    print(f"The request took {response_time}s to complete.")
    return response.content

def trends_retriever(country_code):
    xml_document = fetch_xml(country_code)
    soup = BeautifulSoup(xml_document, "lxml")
    titles = soup.find_all("title")
    approximate_traffic = soup.find_all("ht:approx_traffic")
    return {title.text: re.sub("[+,]", "", traffic.text)
            for title, traffic in zip(titles[1:], approximate_traffic)}


if __name__ == '__main__':
    trends = trends_retriever("KR")
    print(trends)
```

bs4 스크랩은 [여기](https://codereview.stackexchange.com/questions/208277/web-scraping-google-trends-in-python)코드를 사용해서 했다.


## 6. API🍨

하지만 이렇게 코드를 하나하나 작성 할 필요 없이, 좋은 API들이 많이 존재한다.

물론 자기가 원하는 정보만을 뽑아내거나 특정 프로그램을 만드는 등 직접 코드를 작성하는게 좋지만..

집단지성이라는 말이 있듯이.. 많은 좋은 API가 존재한다.

#### (1) rss-parser

> You can parse RSS from a URL (parser.parseURL) or an XML string (parser.parseString). Both callbacks and Promises are supported.

[깃허브로 이동!](https://github.com/rbren/rss-parser)

#### (2) google-trends-api(in node)

> This library provides an API layer to google trends data. Due to CORS restrictions, this library is intended to be used in node. It is constantly being expanded and improved so please check back frequently. Also, please feel free to contribute to make the library even better! 🐶

[상세 설명 페이지로 이동!](https://www.npmjs.com/package/google-trends-api)

#### (3) pytrends(in python)

> Allows simple interface for automating downloading of reports from Google Trends. Only good until Google changes their backend again :-P. When that happens feel free to contribute!

[깃허브로 이동!](https://github.com/GeneralMills/pytrends)


#### (4) Java Google Trends API, Java Google Trends Client (in java)

> j-google-trends-api is a Java based implementation of Unofficial Google Trends API.

[깃허브로 이동!](https://github.com/elibus/j-google-trends-api)

> j-google-trends-client is a Java based implementation of Unofficial Google Trends cli based client.

[깃허브로 이동!](https://github.com/elibus/j-google-trends-client)

