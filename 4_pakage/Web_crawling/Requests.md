# Requests

Python을 이용해 HTTP 요청을 보내어 응답을 받게 도와주는 모듈



### 기본적인 사용방법

`response = requests.get(URL)` : 해당 URL을 requests하고 해당 자료를 reponse 객체를 받는 작업



- GET방식으로 parameter 전달

  ```
  - url : www.naver.com/?key1=val1&key2=val2
  params= {'key1':'val1', 'key2':'val2'}
  res = requests.get(URL, params=param)
  ```

- Post방식으로 data 전달

  ```
  data = {'key1' : 'val1', 'key2' : 'val2'}
  res = requests.post(URL, data=json.dumps(data))
  ```




### response

`response.status_code` : 상태 코드

`response.text` : 응답받은 자료를 text형태로 출력

`response.url` : 요쳥한 url 확인

`response.content` : 이진 데이터 가져오기



`.json()` : json reponse인 경우 딕셔너리 타입으로 변환