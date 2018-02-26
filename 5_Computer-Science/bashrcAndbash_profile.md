# .bashrc와 .bash_profile 차이

### Login Shell과 Non-Login Shell

- `Login Shell` : 계정과 암호를 입력해서 Shell이 실행
  - ssh 접속, GUI 접속
- `Non Login Shell` : 로그인 없이 Shell 실행
  - ssh 접속 후 bash 실행, GUI 세션에서 터미널 실행



### .bashrc와 .bash_profile

- `.bashrc` : 이미 로그인 상태에서 새 터미널 실행시 (non-login shell)
- `.bash_profile` : 시스템 로그인 할 때 실행 (login shell)