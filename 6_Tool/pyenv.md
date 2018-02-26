# pyenv

### pyenv

하나의 시스템 안에서 여러개의 python 버전을 효율적으로 관리



##### pyenv 설치

1. 우분투 패키지 업그레이드

```
sudo apt-get update
sudo apt-get upgrade
```

2. 의존성 파일 설치

```
sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
xz-utils tk-dev
```

3. git & pyenv 설치

```
sudo apt-get install git
curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash
```

4. .bash_profile 설정

```
/home/ubuntu$ vi .bash_profile
```

* `.bashrc` : 이미 로그인 한 상태에서 터미널 열 때 마다 실행
* `.bash_profile` : 시스템에 로그인 할 때마 실행

```
export PATH="/home/ubuntu/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

```
$ source .bash_profile
```



##### pyenv 명령어

- `pyenv install 3.6.4` : 파이썬 설치
- `pyenv install --list` : 버전에 대한 정보 확인
- `pyenv versions` : 현재 설치 및 사용된 버전 확인
- `pyenv shell 3.6.4` : 버전 변경
- `pyenv global 3.6.4` : 디폴트 버전 설정



### virtualenv

같은 파이썬으로 여러개의 가상 환경을 설정하여 관리



##### virtualenv 설치

```
sudo apt-get install pyenv-virtualenv
sudo apt-get install python-virtualenv
```



##### virtualenv 명령어

- `pyenv virtualenv 3.6.4 python3[이름]` : 버전에 해당되는 가상환경 생성
- `pyenv shell python3[이름]` : 가상환경 선택
- `pyenv uninstall python3[이름]` : 가상환경 삭제



### autoenv

특정 디렉토리에 자동으로 python 환경 설정



##### autoenv 설치

```
$ git clone git://github.com/kennethreitz/autoenv.git ~/.autoenv
$ echo 'source ~/.autoenv/activate.sh' >> ~/.bash_profile
$ source .bash_profile # bash_profile 에 입력
```



##### autoenv 명령어

- `pyenv activate python3[이름]`  : python 환경 실행

- `pyenv deactivate` : python 환경 나오기

  ​

- 특정 디렉토리에 `.env` 파일을 생성해 위 명령 추가 !!

