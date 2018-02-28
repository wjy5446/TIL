# AWS

### 실행

- *.pem가 있는 곳에서 git bash 실행
- `ssh -i *.pem ubuntu@외부ip `
  - 외부 ip는 실행할 때마다 달라진다.
- 쉽게 명령어 실행하는 방법
  - `history |grep ssh`
  - `!503` : 해당 라인 실행

### 종료

- `exit`



### 주피터 노트북

##### 설정 방법

- 노트북 설정파일 생성
- `notebook.auth` 이용해 패쓰워드 생성(`sha1`)
  - 보통 `sha256` 를 이용, 계정 관리시 sha1를 이용해 저장
- `openssl`를 이용해 `*.pem` 파일 생성
  - 원래는 인증센터에서 키를 발급해 준다. 하지만 openssl은 인증센터 없이 생성(안정하지 않는 사이트)
  - SSH(secure Shell) : 다른 네트웨크에 로그인하거나 원격 시스템 명령을 실행할 때 사용하는 응용프로그램
- 노트북 설정파일 수정
  - ip, open_browser, password, certfile, port



##### 주피터 실행

- foreground : 하나만 실행 (실행시 bash 이용 불가)
- background : 여러개 실행 가능 (bash 이용 가능)
  - `jupyter notebook &`



##### 주피터 종료

- `ps -e | grep` : 실행중인 프로세스 확인
- `kill -9 pid(입력)` : 특정 프로세스 종료



### cyberduck

- ftp(file transport protocol) 를 이용해 파일을 주고 받을 수 있는 프로그램



### crontab

특정 시간에 특정한 작업을 할 때 사용하는 스케쥴러



##### crontab 명령어

- `crontab -e` : 크론탭 실행 리스트 입력
- `crontab -l` : 크론탭 스케쥴 확인



##### 주기 설정

```
*분(0-59) *시간(0-23) *일(1-31) *월(1-12) *요일(0-7)
```

- `* * * * * python /home/ubuntu/slack.py` : 파일 실행(home)에서 부터 입력
- `*/1 * * * * ` : 1분마다 실행
- `10 * * * * ` : 10분에 실행
- `10,20 * * * * ` : 10, 20분에 실행
- `*/5 5-10 * * *` : 5시에서 10시까지 5분마다 실행



- `*/5 * * * * python /home/time.py >> time.txt` : 실행결과 time.txt에 저장
  - `> `: overwrite 저장, `>>` : 이어서 저장



### phantomJS와 xvfb

window가 없는 환경에서 selenuim을 가능하게 해주는 패키지

- phantomJS : 브라우저를 띄우지 않는 Headless 브라우저를 사용해 웹크롤링

`driver = webdriver.PhantomJS()`



- xvfb : 메모리에 가상 브라우저를 띄어서 웹크롤링

`from pyvirtualdisplay import Display`

```
display = Display(visible=0, size=(800, 600))
display.start()

/**해당 내용 입력**/

driver.quit()
```

