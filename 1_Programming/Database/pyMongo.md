# pyMongo

### Import 

`import pymongo`



### 준비

`client 연결 -> DB 선택 -> Collection 선택`

##### Client 연결

`client = pymongo.MongoClient('mongodb://localhost:27017/')`



##### 데이터 베이스 선택

`db = client.dss`



##### Collection 리스트 확인

`db.collection_names()`



##### 컬렉션 선택

`collection = db.info` 



### Find

- `document = collection.find_one({"subject":"python"})` : 한개의 document 가져오기
- `documents = collection.find()` : 모든 document 가져오기 (cursor 리턴)
- `documents.count()` : 도큐먼트의 갯수를 가져온다.
- `documents = collection.find({"level":{"$lte":3}}).sort("level", pymongo.DESCENDING)` : 내림차순 정렬
- `collection.find({}).count()` : document 데이터 수 확인



### insert

`result = collection.insert_one(data)` : 데이터 하나 추가

`result = collection.insert_many(data)` : 데이터 여러개 추가

`result.inserted_ids` : insert_id 확인