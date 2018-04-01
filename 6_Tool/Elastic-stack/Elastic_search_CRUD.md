# Elastic_search_CRUD

REST Api를 이용해 데이터 입력 조회및 삭제

- `Create` : `PUT`
- `READ` : `GET`
- `Update` : `POST`
- `Delete` : `Delete`




### Verify Index

- `curl -XGET http://localhost:9200/classes` : 결과 확인
- `curl -XGET http://localhost:9200/classes?pretty` : JSON 형태로 결과 확인




### Create Index

- `curl -XPUT http://localhost:9200/classes` 




### Delete Index

- `curl -XDELETE http://localhost:9200/classes`




### Create Document

- `curl -XPOST http://localhost:9200/classes/class/1/1 -d '{"title" : "Algorithm", "name" : "John"}'` 
  - Index가 없어도 생성 가능
- `curl -XPOST http://localhost:9200/classes/class/1/1-d @oneclass.json` : 파일로 저장




### Update

- `curl -XPOST http://localhost:9200/classes/class/1/_update -d '{"doc":{{"unit":1}}}'`



- `curl -XPOST http://localhost:9200/classes/class/1/_update -d  '{"script":"ctx_source.unit +=5"}'` : script를 이용해서 업데이트



- `curl -XPOST http://localhost:9200/_bulk?pretty --data-binary @classes.json ` : bulk file로 update



### Search

- `curl -XGET localhost:9200/basketball/record/_search` : 데이터 확인


- `curl -XGET localhost:9200/basketball/record/_search?q=points:30&pretty` : query를 이용해 데이터 검색


- `curl -XGET localhost:9200/basketball/record/_search -d  '{"query" : {"term":{"point":30}}}'` : request body를 이용한 검색
  - -d : direct의 준말