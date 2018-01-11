# Linux

## Linux의 역사

UNIX의 탄생(1965) : 데니스 리치, 켄 톰슨 (C를 제작), AT&T Bell 연구소에서 UNIX OS를 개발

C 기반의 UNIX(1973) : 데니스 리치, 켐 톤슨가 C를 개발한 뒤 UNIX 다시 제작

GNU 프로젝트(1984) : 리차드 스톨먼이 오픈 소프트웨어 자유성 확보, But 중요한 Kernel이 존재하지 않는다. 

Linux의 탄생 : 리누스 토발즈가 MINIX를 개조하여 Kernel를 개발하여 오픈 OS 제작



### Linux

리누스 토발즈가 작성한 GNU 프로젝트 라이브러리와 도구가 포함된 운영체제

Redhat, Debian, Ubuntu, Android, CentOS 존재

## Shell

운영체제의 커널과 사용자를 이어주는 소프트웨어



### 종류

- sh(Bourne Shell) : AT&T Bell 연구소의 스티븐 본이 작성한 유닉스 쉘
- csh : 버클리 Bill Joy가 작성한 유닉스 쉘
- bash(Bourne Agian Shell) : Brain Fox가 작성한 유닉스 쉘 (가장 기본적인 쉘)
- zsh : Paul Falstad가 작성한 유닉스 쉘
  - sh 확장형 



### Shell Command

#### 파일 이동 관련 명령어

- cd : 이동
- cd .. : 상위 폴더 이동
- cd ~ : 최상위 폴더 이동


- cd ./ : 현재 폴더를 다시 방문
- cd / : 최상위 폴더 이하의 것



#### 폴더 관련 명령어

- mkdir : 디렉토리 생성
- rmdir : 디렉토리 삭제
- ls : 파일리스트 확인 (-a:모든 내용확인, -l:자세한 내용출력)



#### 파일 관련 명령어

- touch : 새 파일 생성 (숨김 파일: 파일 앞에 '.' 붙인다
  - 원하는 위치에서 빠르게 파일을 생성할 수 있다.
- rm : 파일 삭제  (-r : 반복적으로 안에 내용 삭제, -f: 강제 삭제)


- mv : 파일 이동 및 이름 변경
- cp :  파일 복사



#### 쉘 관련 명령어

- clear : 현재 위치를 최상위로 올려준다.


- exit : Shell 종료
- sudo : 관리자 권한으로 변환



### 파일 권한 변경

Cloud Service 접속할 때, 권한이 어렵다.

- chmod : 

  `chmod [옵션] (8진수) (파일명)`

  drwxr-xr-x

  (user)(group)(other)

  d : directory or file

  r : read

  w : write

  x : execute

  ​

## Vim

텍스트 에디터 (<-> Emacs)

`vi readme.txt` : 실행

- 모드 : 
  - Read : 'ESC' 모드 탈출하기
  - Insert : 'i' 내용 수정하기
  - Visual : 'v' 블록 설정
- 단축키 
  - 'd' : 자르기
  - 'p' : 붙이기
  - 'y' : 복사하기
  - 'u' : 전 작업내용으로 이동하기
  - 'r' : replace
  - '$' : move end of line
  - '^' : move start of line
  - ':' : 메뉴모드
  - ':10' :해당 줄로 이동
  - ':q' : 종료
  - ':wq' : 저장하고 종료
  - ':q!' : 수정한 내용 저장하지 않고 종료
  - ':w' : 중간 내용 저장



## Macro

qa : a라는 매크로 생성

커서이동까지 기록한다.

q : 매크로 종료

@a : a 매크로 실행

10@a : a 매크로 10번 실행

*Shell 이 켜져 있는 동안 매크로 저장.

