# Elastic search 기본 개념

미리 분류와 색인을 만들어 빠르게 검색 (쉽게 이해 :  색인 기능이 추가된 NoSQL DBMS)

- keyword를 이용해 document를 검색



### 기본 개념/용어

- 인덱스, 타입, 문서 : 엘라스틱 서치의 데이터 계층
- 필드 : JSON의 프로퍼티
- indexing : 색인 데이터를 만드는 작업
- cluster/node : 여러 서버를 구동하기 위한 개념, Node : 한 서버, Cluster : 서버의 묶음
- Shard/replica : 여러개의 저장공간을 나누거나 복사하는 것
  - shard : 물리적으로 공간을 나누어 저장
  - replica : 노드를 복제(백업)해 두는 작업
  - QueryDSL : 엘라스틱 검색 문법



### 관계형 데이터와의 비교

| Elastic Search | 관계형 데이터  |
| :------------: | :------: |
|     Index      | Database |
|      Type      |  Table   |
|    Document    |   Row    |
|     Field      |  Column  |
|    Mapping     |  Schema  |

| Elastic Search | 관계형 데이터 |
| :------------: | :-----: |
|      GET       | Select  |
|      PUT       | Update  |
|      POST      | Insert  |
|     DELETE     | Delete  |

