# Mongodb update

- **형태**

`db.collection.update( query, update 내용, { upset : <bool>, multi:<bool>})`

- upset : 데이터가 없으면 insert한다는 의미, update + insert


- multi : 여러개의 dacument 수정

ex )

`db.collection.update({"subject":"css"}, {"subject":"sass", "level":2}, {"upset":true}})`



### set / unset

set, unset은 document 필드를 수정하거나 제거할 때 사용.

- set : `db.info.update({subject:"python"}, {$set : {level:4}}, {multi:true})`


- unset : `db.info.update({subject:"java"}, {$unset:{level:1}})`



### push / each

배열의 값을 추가할 때 사용.  `push`는 하나의 배열을 추가, `each`는 여러개 배열 추가

- `db.info.update({subject:"java"}, {$push: {"comment" : {"name":"peter"}})`
- `db.info.update({subject:"java"}, {$push:{"comment" : {$each : [{"name" : "jin", "msg" : "echo jin"}, {"name":"alice", "msg" L "alice"}]}}})`



### pull, in

배열의 값을 제거할 때 사용.  `pull`은 하나의 배열을 삭제, `in`은 여러개 배열 삭제

- `db.info.update({subject:"java"}, {$pull:{"comments":{"name":"po"}}})`
- `db.info.update{subject:"java"}, {$pull:{"comment":{$in:[{"name":"po"}, {"name":"alice"}]}}}`



### function 사용

javascript 문법으로 함수 사용이 가능

`var showSkip = function(start){return db.info.find().skip(start)}`

`showSkip(3)`

