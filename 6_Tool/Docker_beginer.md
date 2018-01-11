# Docker

컨테이너 기반의 오픈소스 가상화 플랫폼



## 역사

2013년 Pycon Conference 에서 dotCloud의 창업자 솔로몬 하이케스가 제작

2013년 10월 Docker 회사가 설립

2016년 6월 Docker 1.0 발표



## Container

격리된 공간에서 프로세스가 동작하는 기술



- 패키지 설치, 사용자 추가, 호스트의 특정 디렉토리 사용 가능



### Docker vs VM

- VM : Full virtualization

  - 방식 : HostOS -> Hypervisor -> GuestOS -> bins, libs -> app
  - OS 전체를 가상화하기에 무겁고 느리다.

-  Docker : paravirtualization

  - 방식 : HostOS -> Docker Engine -> bins, libs -> app
  - 부분만 가상화 하기 때문에 가볍다.
  - 프로세스를 격리시킴, 즉 , 필요한 CPU나 메모리 만큽 할당시킨다.

  ​

## Image

컨테이너 실행에 필요한 파일과 설정값을 포함. (immutable 변하지 않는다.)

ex) Ubuntu 이미지 : Ubuntu 실행에 필요한 이미지, MySQL 이미지 : MySQL실행에 필요한 이미지



## 레이어 저장 방식

이미지내 여러개의 레이어를 이용한다.

Ubuntu + nginx + web app 환경의 이미지를 이용할 때, Ubuntu layer, nuginx layer, web app layer의 조합으로 이미지 구성. 



- 이 방식의 장점 : web app의 소스가 수정되었다면, 기존의 레이어를 제외하고 해당 레이어만 수정해 효율적으로 이미지를 관리할 수 있다. 