# Database Basic Syntax

## 1. create

### 1-1. Database

- `CREATE DATABASE test` : 데이터 베이스 생성
- `use test` : 데이터 베이스 선택
- `SELECT DATABASE()` : 데이터 베이스 확인



### 1-2. Table

- `CREATE TABLE user1(name Varchar(20), age int(3))` : 제약조건 없는 테이블 생성
- `CREATE TABLE user1(name Varchar(20) not null, age int default 30)` : 제약조건 있는 테이블 생성



## 2. Alter

### 2-1. Database

- `ALTER DATABASE test CHARACTER SET = ascii` : 데이터 베이스 인코딩
- `show variables like "character_set_database"` : 데이터 인코딩 변경 확인



### 2-2. Table

- `ALTER TABLE user2 ADD tmp TEXT` : text 데이터 타입을 가지는 tmp 컬럼 추가
- `ALTER TABLE user2 MODIFY COLUMN tmp INT(3)` : int 타입을 가지는 tmp 컬럼으로 수정
- `ALTER TABLE user2 DROP tmp`  



## 3. DROP

- `DROP DATABASE tmp` : tmp 데이터 베이스 삭제
- `DROP TABLE tmp` : tmp 테이블 삭제



## 4. INSERT

- `INSERT INTO user1(user_id, name) VALUES(1, "jin");` : user1 테이블에 데이터 입력



## 5. SELECT

- `SELECT * FROM user1` : 전체 컬럼 데이터 조회 (기본)



### 5-1. ALIAS

- `SELECT user_id as "아이디" FROM user1` : 컬럼명 변경



### 5-2. DISTINCT

- `SELECT DISTINCT(name) FROM user1` : 중복된 데이터 제거



### 5-3. WHERE

- `SELECT * FROM user1 WHERE age >= 30` : 숫자를 조건문으로 비교
  - `=`는 같다라는 표시.
- `SELECT * FROM user1 WHERE rdate >= "2016-01-01"` : 날짜를 조건문으로 비교
- `SELECT * FROM user1 WHERE rdate >= "2010" AND rdate <="2017"` : 날짜 사이 존재
-  `SELECT * FROM user1 WHERE rdate BETWEEN "2010" AND "2017"` : **between**을 사용해 기간 조회



### 5-4. ORDER BY

- `SELECT * FROM user1 ORDER BY age ASC` : 오름차순 정렬

- `SELECT * FROM user1 ORDER BY age DESC` : 내림차순 정렬

- `SELECT * FROM user1 ORDER BY age DESC, rdate ASC` : age는 내림차순 정렬, rdate는 오름차순 정렬

   

### 5-5. CONCAT

- `SELECT CONCAT(name, "(", age, ")") AS "name_age" FROM user1` : 여러 컬럼을 합쳐 새로운 컬럼을 보여주는 것
  - alias가 없다면 컬럼명으로 이상한 값이 들어가기 때문에 alias로 간략한 컬럼명을 적어준다.



### 5-6. LIKE

- `SELECT * FROM user1 WHERE email LIKE "%gmail%"`  : 해당 문자열이 있는 지 확인, `%` 는 어떤 문자가 와도 된다는 의미
  - `NOT LIKE` : 특정문자가 들어가지 않았을 때 넣어준다.



### 5-7. IN

- `SELECT * FROM user1 WHERE name IN ("peter", "alice")` : peter와 alice가 데이터 프래임에 존재하는 지 확인 할 때 사용



### 5-8. LIMIT

- `SELECT * FROM user1 LIMIT 1, 3` : 두번째에서 세개의 데이터만 조회
  - 숫자하나만 썼을 때에는 처음부터 데이터 조회



## 6. UPDATE

- `UPDATE user1 SET age=20 WHERE name="jin"` : jin이란 조건에서 age컬럼을 20으로 지정한다.
  - update을 사용할 때에는 전체 데이터를 날릴 수 있기 때문에 조심해야 된다.!!!!
  - 반드시 select * from 으로 데이터를 한번 조회하거나 `LIMIT`을 이용해 일부만 변경 될 수 있도록 한다. 
  - **반드시 조건문이 있는 지 확인!!**



### 7. DELETE

- `DELETE FROM user1 WHERE rdate < "2016-01-01"` : 특정 조건 데이터 삭제



