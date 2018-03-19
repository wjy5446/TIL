# MySQL 명령어 

### System

- `mysql -u root -p` : mySQL 실행
- `help` : 명령어 리스트 확인
- `status` : 현재 상태 보기
- `exit, quit` : mysql 접속 종료
- `ALTER USER 'root'@'localhost'IDENTIFIED BY 'asd1256'`



### Database

- `show databases` : DB 목록 보기
- `create database test` : test이름의 database 생성
- `use test` : DB 접속
- `select database()` : 현재 DB 확인
- `drop database test` : DB 삭제



### Table

- `show tables` : 테이블 목록 확인
- `create table user(name char(20), age int(3))` : user 테이블 생성
  - 자료형 default는 11byte
- `desc user ` : 테이블 구조 확인
- `rename table user to dss` : 테이블 이름 변경
- `drop table dss` : 테이블 삭제



### 데이터 입력

- `insert into dss(name, age) values("alice", 23)` : 데이터 입력
- `select * from dss` : 추가 데이터 확인