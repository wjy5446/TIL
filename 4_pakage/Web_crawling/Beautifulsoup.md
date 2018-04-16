# Beautifulsoup

HTML혹은 XML를 파싱하는데 사용하는 Python 라이브러리



`from bs4 import BeautifulSoup`

`import requests`



### BeautifulSoup 선언

`response = requests.get('http://www.naver.com')` : html 가져오기

`dom = BeautifulSoup(response.content, "html.parser")` : html으로 파싱



#### 데이터가져오기

`dom.select(".ar_roll .ah_l .ah_item")` : 여러 개 가져오기

`dom.select_one(".ah_r")` : 하나의 데이터만 가져오기

`dom.select_one(".ah_r").text` : 데이터 글자로 가져오기