# DataBase

데이터의 집합



### DBMS(DataBase MAnagement System)

데이터 베이스를 관리하는 미들웨어 시스템



### 종류



##### 1. RDBMS (Relational Database Management System)

- 데이터 테이블 사이 키값으로 관계를 가지는 데이터베이스
- Oracle(유료, 기술 지원), Mysql(무료), Postgresql(파이썬), Sqlite(인베디드용)
- 장점 : 
  - 데이터 분류, 정렬, 탐색속도가 빠름, 
  - 신뢰성 높음
- 단점 :
  -  스키마 수정이 어려움
- 구조

> Server > DataBase > Table > row > value

- `Table` : row와 column으로 이루어진 데이터 베이스의 기본 단위

- `row` : 테이블의 가로축 데이터 (Tuple, Recode)

- `column` : 테이블의 세로축 데이터 (Field, Attribute)

- `value` : 행과 열에 포함되는 데이터

- `key` : 행의 식별자

- Relationship : 1:1, 1:n, n:n 

  - `Schema` : 데이터베이스의 구조를 만드는 디자인

- Example

  ```
  user table 
  ID	name
  1	JY
  2	TH
  ---------------------------------
  car table
  ID	car
  1	car1
  2	car2
  ```

  - 1:1

  ~~~
  ID	name	Car
  1	JY		car1
  2	TH		car2
  ~~~

  - 1:n

  ```
  ID	name	Car
  1	JY		car1
  1	JY		car2
  ```

  - n:n

  ```
  ID	name	Car
  1	JY		car1
  2	TH		car1
  1	JY		car2
  2	TH		car2
  ```

  ​

##### 2. NoSQL(Not only SQL)

- 데이터 테이블 관계 없이 JSON 형태로 저장하는 데이터베이스
- Mongodb, Hbase, Cassandra
- 장점 : 
  - 확장성이 좋음(분산처리 용이`shading`), 
  - 데이터 저장이 유연(구조 변경 불필요),
  -  Insert가 빠르다.(대용량 데이터 베이스 사용)
- 단점 :
  -  select가 RDBMS보다 느림,
  - 모든 데이터가 들어가 있어야 함,
  - Join, Schema 없음 
  - 트랜젝션이 지원되지 않음.
    - Transaction(동시 수정을 가능하게 해주는 기능)
- 구조

> Server > Database > Collection > Document > key:value