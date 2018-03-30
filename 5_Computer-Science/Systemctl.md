# Systemctl

RedHat에서 개발한 서비스 관리 애플리케이션 (systemd 내부에서 )

=> 백그라운드 프로그램

- 비슷한 프로그램 : `service`, `chkconfig`



### 백그라운드 프로그램 ?

사용자가 직접적으로 제어하지 않고 백그라운드를 돌면서 여러 작업을 하는 프로그램 (예를 들어 Daemon)



### 주요 명령어

- `systemctl start <서비스 이름>` : 서비스 시작
- `systemctl restart <서비스 이름>` : 재시작
- `systemctl stop <서비스 이름>` : 중지



- `systemctl enable <서비스 이름>` : 부팅시 자동 실행
- `systemctl disable <서비스 이름>` : 자동 실행 취소



- `systemctl list-units` : 서비스 목록 보기
- `systemctl list-unit-files` : 설치된 unit 파일 보기



- `systemctl status <서비스 이름>` : 서비스 구동 여부 확인
- `systemctl list-units --type=service --state=running` : running 목록 확인
- `systemctl is-active <서비스 이름>` : 특정 서비스 active 상태 조회
- `systemctl is-enabled <서비스 이름>` : 특정 서비스 enable 상태 조회