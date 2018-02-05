# Web

## Server & Client

- Client : 브라우저를 통해 서버에 데이터를 요청 (repuest)
- Server : 데이터를 요청하면 요청에 따라 데이터 전송 (response)



### 데이터 전송 방식

- Pooling : request, response을 통해 이루어지는 데이터 전송 방식
  - 연결이 되지 않아도 가능
- Socket : 일방적으로 server에서 client에 데이터를 전송할 때 쓰는 방식
  - Server와 Client간의 연결이 필요
  - 일반적인 채팅에 사용
  - Nose.js가 소켓통신에 최적화



## URL (Uniform Resource Locator)

```
http://news.naver.com/main/read.nhn?mode=1&mid=shm#da_727145
```

- 프로토콜 : http://, https://, ftp:// 통신할 때 쓰이는 규약 
  - http:// 와 https://의 차이
  - https://는 SSL방식을 이용해 패킷을 암호화해 Router에서 발생하는 snipping을 방지해준다. 단점으로 http://보다 시간이 더 오래걸린다.
- Sub domain(new.) : domain안에 서브 도메인
- Domain(naver.com) : host업체에서 지정해준 이름
- Path/directory(/main/) : 서버내 디렉토리
- page(read.nhn) : 디렉토리 안에 코드가 들어있는 파일
- port : 도메인을 세부적으로 구분하기 위해 사용하는 것(몇몇 port는 지정되어 있다.)
  - 80 : http
  - 3306 : MySQL
  - 443 : SSL
- Query(?mode=LSD&sid1=105) : URL를 이용해 서버에 요청할 데이터를 적는 곳
  - '?'는 파일과 Query를 구분하기 위해 사용
  - '&'는 쿼리간 구분하기 위해 사용
- Fragment(#da_727145) : 특정위치를 브라우저 최상단에 나타내기 위해서 사용 



## Get & Post

- Get 방식 
  - 보낼 데이터가 URL에 포함되고 있는 방식
  - 길이 제한이 있음 (브라우저마다 그 길이가 다름)
- Post 방식
  - HTML Body에 데이터가 포함되는 방식
  - 데이터를 숨길수 있다.



## Internet

인터넷은 컴퓨터로 연결하여 TCP/IP 프로토콜을 이용해 정보를 주고받는 컴퓨터 네트워크

- FastCampus에서 미국 서버까지 연결 : 노트북 -> 무선 -> 공유기 -> 유선(backbone) -> 부산 -> 해저케이블 -> 미국



## OSI 7 Layer

Open Systems Interconnection Reference Model



- 구조
  - Application
  - Presentation
  - Session
  - Transport : TCP(신뢰도가 있는 규약, 재전송 요청) / UDP(신뢰도가 없음, 실시간 데이터 전송에 유리)
  - Network : IP를 이용해 Router에서 패킷을 어떻게 전송할지에 대한 규약
  - Data Link : MAC 주소를 이용해 여러 컴퓨터가 어떻게 선을 공유할 지에 대한 규약
  - Physical : 비트 전송과 관련된 규약(유선, 무선)
- 상위로 갈수록 페이로드(Header)가 점점 많아 진다.
- Client와 Server는 모든 페이로드를 다 해석한다.
- Router는 Network까지 데이터층만 해석



## Cookie & Session & Cache

- Cache

  - 데이터를 빠르게 가져오기 위한 임시 데이터 저장소

  - RAM에 저장

  - Client, Server 모두 가지고 있다.

    ​

- Cookie

  - Client에 저장하는 문자열 데이터

  - Cache의 일종

  - 로그인 정보, 팝업 다시보기 저장

  - 클라이언트당 300, 도메인 20 저장

  - ROM에 저장(비휘발성)

    ​

- Session

  - Server에 저장하는 객체 데이터
  - RAM에 저장 
  - Session ID를 저장해 로그인 연결 유지
  - 브라우저마다 다른 Session ID 부여



## HTTP Status Code

서버와 클라이언트가 데이터를 주고 받은 결과를 나타내는 코드

- 종류
  - 2xx - Success
  - 3xx - redirection (bowser cache)
  - 4xx - request error (server를 찾지 못함)
  - 5xx - server error (server를 찾았지만 에러발생)



## Web Language & Framework

- Client
  - HTML, CSS(less, sass), Javascript(vue.js, react.js, angelar.js)
- Server(언어 - 프래임워크)
  - python - Django, Flask
  - Java - spring
  - Ruby - Rails
  - Javascript - Nodejs
  - Scala - Play



- Framework : 웹 개발에 사용되는 모듈을 모아둔 것



## Scraping & Crawling & Spider & Bot

- Scraping : 데이터를 모으는 작업
- Crawling : 여러 페이지의 특정 데이터를 수집하고 분류하는 작업
- Spider or Web crawling : 웹 데이터를 수집하는 소프트웨어
- Bot : 인터넷 에서 자동화 작업을 실행하는 소프트웨어