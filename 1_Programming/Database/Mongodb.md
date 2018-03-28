# Mongodb

MongoDB는 C++로 작성된  Nosql 데이터 베이스

- 고정 스키마, JOIN이 존재하지 않음



### 1. MAKE

##### make databases

`use dss` : DB 생성

##### make collection

`db.createCollection(name, [option])` : Collection 생성

- option
  - capped : collection의 최대 용량 설정, 오래된 데이터 자동 삭제
  - autoIndexId : _id에 index  자동 생성
  - size : collection 최대 사이즈 지정
  - max : document 최대 갯수 설정

`db.articles.insert()`

##### make document

`db.user.insert({"name":"alice", "age":20, "email":"glice@gmaiul.com"})`



### 2. DELETE

##### Delete Database

`db.dropDatabase()` : 선택된 database 삭제

##### Delete collection

`db.articles.drop()`

##### Delete document

`db.collection_name.remove({level:2})` 



### 3. SHOW

##### database 확인

`show dbs`

##### collection 확인

`show collections`

##### document 확인

`db.collection_name.find()`



### 4. FIND

##### document 찾기

`db.collection.find(query, projection)`

##### 4-1. query

- `db.info.find({"subject":"python"})`  : 특정 컬럼에 해당되는 값 확인

(1) 비교연산자

- `db.info.find({"level":{$lte:2}})` : 이하 값 출력
- `db.info.find({"level":{$gte:3}})` : 이상 값 출력
- `db.info.find({"subject":{$in:["java", "python"]}})` : 리스트 값이 포함되는 document 조회

(2) 논리 연산자

- `db.info.find({$and : [{"subject" : "python"}, {"level":{$gte:4}}]})` : and
- `db.info.find({$nor : [{"subject" : "python"}, {"level" : {$gte:4}}]})` : nor
- `db.info.find("level":{$not:{$gt:2}})` : not

(3) where 연산자 : javascript 연산자 사용 가능

- `db.info.find({$where:"this.comments.length==0"})` : 갯수가 0인 document 확인 

(4) elemMatch 연산자 : JSON 안 JSON 파일 확인

- `db.info.find({"comment":{$elemMatch:{"name":"alice"}}})` : comment의 alice확인
- `db.info.find({"comments.name":"alice"})` : find로도 가능

(5) exists 연산자 : 존재하는 값만 출력

- `db.info.find({"level":{$exists:false}})`



##### 4-2. projection

보여질 필드 정의

(1) basic

- `db.info.find({}, {"_id": false, "level":false})`
- 조건에 false와 true가 섞이지 않게 한다.
- false : 보이지 않게, true : 보이게

(2) slice

출력 갯수 설정

- `db.info.find({}, {"comments":{$slice:1}})`

(3) elemMatch

- `db.info.find({"comments":{$elemMatch:{"name":"alice"}}}, {"subject":true, "comments":{$elemMatch:{"name":"alice"}}})`



##### 4-3. find method

(1) sort

- `db.info.find().sort({"level":-1, "_id":1})` 
- -1 : 내림차순, 1 : 오름차순

(2) limit

- `db.info.find().limit(5)` 

(3) skip

- `db.info.find().skip(2)` : 두번째부터 출력