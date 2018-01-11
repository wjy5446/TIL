# Git

##  VCS (Version Control System) 이란?

버전 관리 시스템 : 개발의 로그를 저장하는 시스템 

< SCM (Software Configuration Management) : 모든 자원을 관리하는 시스템

리누스 토발즈가 Sub를 사용하다가 2주만에 개발 ;;



- 특징
  - 빠른 속도 
  - 분산형 저장소 지원 (오프라인, 원격 사용도 가능)
  - 비선형적 개발 가능 (브랜치가 가능, 즉 한 시점에서 여러 개발하고 하나로 합친다.) 
- 목적
  - 소스코드를 주고 받는 것 없이 동시 작업 가능
  - 보안도 좋다
  - 수정 내용은 commit으로 관리 가능.
  - 원하는 시점으로 이동 가능 (Checkout 가능)
  - Branch로 실험이 가능, 개발이 완료되면 Merge로 반영
  - 오픈 소스 프로젝트 확인 가능
- Git의 내부
  - Blob : 모든 파일이 Blob이라는 단위로 구성
  - Tree : Blob을 모은 것
  - Commit : 파일에 대한 정보를 모은 것



- github vs git

  - git : VCS 으로 bash 내에서 동작하는 것

  - github : git을 이용한 웹 서비스

    ​

## Git의 절차

- workspace -> index -> local repository -> remote repository(샌프란시스코)

- 올리는 명령어 순서 : add -> commit -> push




## Git 초기 설정

### config 설정

```
git config --global user.name "username"
git config --global user.email "email address"
git config --list
```

* 초기 한번만 설정 (편지로 치면 ''보내는 이' 설정) --global 모든 쉘에 적용!



### Local repository 생성

```
git init
```



### Remote repository 연결

```
git remote add orgin https://github.com/bal
```

* Local repo와 Remote repo를 연결(편지로 치면 "받는 이" 설정)



## Workspace 에서 Remote repository 까지

### index 추가

```
git add *.txt
```



### Local repository에 commit

```
git commit -m "message"
```



### Local repository -> Remote repository

```
git push origin master
```



## 그 밖에 명령어

### 로그 확인

지금까지 했던 작업을 확인(로그)

```
git log
```



### 원격에서 로컬로 받아오기

```
git pull origin master
```



### 차이 알아보기

현재 수행하고 있는 브랜치의 차이

HEAD : 현재 작업하고 있는 브랜치의 포인터

```
git diff HEAD
```

stage area에서 차이 보기

```
git diff --staged
```



### 파일 Unstage 하기

```
git reset octofamily/octodog.txt
```



### Undo하기

```
git checkout -- octocat.txt
```

마지막 commit으로 되돌아 가기



### 파일 삭제하기

실제 파일도 제거하고 stage에 있는 파일도 삭제한다.

```
git rm '*.txt'
```



### Merge branch

```
git merge clean_up
```



### branch 삭제

```
git branch -d clean_up
```



