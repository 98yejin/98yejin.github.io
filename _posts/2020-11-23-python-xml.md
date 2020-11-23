---
layout: post
title: 파이썬으로 xml파일 자동 생성 도구를 만들면서 있었던 시행착오
tags: [python, xml, data scraping]
comments: true
---

### 대충 어떤 도구?

1. xml 파일 작성 자동화 -> script 작성 후 exe 파일 생성(사용자가 라이브러리를 설치할 필요없도록) 
2. xml 파일 내용에는 웹에서 가져오는 정보도 포함 -> Web scraping(crawl + parse)
3. 업무 관련자에게 공유 -> email 전송 기능 

### 무슨 라이브러리를 사용했나?

```python
from xml.etree.ElementTree import Element, SubElement, ElementTree, dump
```

python으로 xml 파일을 작성할 때 사용하는 기본 라이브러리

```python
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from bs4 import BeautifulSoup
```

웹에서 데이터를 크롤링하고 bs4로 원하는 정보를 추출

```python
import os
from datetime import datetime as dt
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
```

이메일 전송 시 필요한 라이브러리들

os, datetime은 폴더 생성 용, 그 외에는 이메일 전송을 위해서 사용했다.


### 웹 크롤링 할 때 백그라운드에서 돌아가게 하기

```python
	profile = webdriver.FirefoxProfile()
	options = webdriver.FirefoxOptions()
	options.headless = True
	binary = FirefoxBinary('C:\\Program Files\\Mozilla Firefox\\firefox.exe')
	driver = webdriver.Firefox(executable_path=driver_path, firefox_profile=profile, firefox_options=options, firefox_binary=binary)
```

options.headless = True로 하면 백그라운드에서 크롤링이 된다.

### XML파일 보기좋게 만들기

```python
def indent(elem, level=0):
	i = "\n" + level*"    "
	if len(elem):
		if not elem.text or not elem.text.strip():
			elem.text = i + "    "
		if not elem.tail or not elem.tail.strip():
			elem.tail = i
		for elem in elem:
			indent(elem, level + 1)
		if not elem.tail or not elem.tail.strip():
			elem.tail = i
	else:
		if level and (not elem.tail or not elem.tail.strip()):
			elem.tail = i
```

### Selenium과 BS4를 사용해서 표 스크랩하기

```python
	html = driver.page_source
	soup = BeautifulSoup(html, 'html.parser')
	table = soup.find('table', {'class': 'table'})
	spans = table.find_all('span')
```

### UTF-8 한국어 안깨지게 하기, short empty elements 사용안하기(<dev /> 말고 <dev></dev>로 작성되게 하기!), declaration 선언부 추가하기

```python

	tree.write(filename, encoding = "UTF-8", xml_declaration=True, short_empty_elements=False)	
```

write 할 때 encoding을 해주고, declaration = True 해주고, short_empty_elements=False 라고 해주면 문제 해결!
구글링 엄청 많이 했는데 ㅎㅎ 답은 언제나 교과서에 있다..!

