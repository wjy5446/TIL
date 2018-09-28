# spark 

- Apache Spark : 인메모리 기반 클러스터 컴퓨터 엔진
- 분산 메모리 기반의 분산 병렬 처리
- 범용 엔진 Apache Hadoop 호환

## hadoop의 한계
- replication, serialization, disk IO로 인해 속도 저하
- 반복할 때마다 disk read/write가 실행
- Interactive algorithm, data mining 이 부족



## Spark 특징

- Unfied Engine : end to end application
- High level API : 사용이 쉽고, 최적화되어 있음 
- Integrate Broadly : Storage systems, librataties

- In-memory 기반 컴퓨팅
- RDD 데이터 모델
- Scala, Java, Python 지원
- Interactive shell 지원
- 하나의 어플리케이션에 배치, SQL 쿼리, 스트리밍, 머신러닝 다양한 작업 가능



## Spark 용어 정리

- **RDD (Resilient Distributed Dataset)**
  - Dataset : 메모리, 디스크에 분산된 immutable한 데이터. 객체
    - **immutable** : RDD 수정시 새로운 RDD 생성
  - Distributed : RDD에 있는 데이터는 클러스터에 자동 분배 및 병렬 연산 수행
  - Resilient : 클러스터의 한 노드가 실패해도 다른 노드가 작업

  - **Partition** : 하나의 RDD는 여러 
    - partition 갯수 = executor의 갯수  

- Open API의 종류
  - Transformations : 데이터 변형, Return으로 RDD 반환
  - Actions : 결과 연산 리턴, Return으로 Collection 반환

- **Lazy Evaluation**
  - Action이 실행될 때, Transformation 실행
- Controllable Persistence 
  - RAM, Disk 안에 Cache 가능

- **Lineage** : Transformation, Action을 통해 새로운 RDD가 만들어지는 과정이 기록된 계보
  - Fault-tolerant : 데이터의 fault가 생겨도 lineage를 이용해 RDD 다시 생성 




- **Job** : HDFS or local에서 불러들인 data을 처리하기 위한 code
- **Stage** : Job의 구성요소이며, Map과 Reduce로 나누어지는 요소
  - computational boundaries에 의해 나누어 짐.
- **Task** : 병렬처리를 위해 나누어진 요소, parition = tast, 하나의 executor는 하나의 partition을 처리



- **Application** : Spark위에 세워진 user program으로, driver program과 executor로 구성
- **Driver program** : main이 돌아가는 프로세스, SparkContext 생성
- **Cluster manager** : 리소스를 얻기 위한 외부 서비스, (Standalone, Mesos, YARN)
- **Executor** : worker node내에 돌아가는 프로세스, memory와 disk안에서 돌아가는 데이터 유지
- 보통적인 흐름
  - `Rdd 생성` -> `Rdd 변형` -> `Rdd 연산`



## Spark application

- Interactive Shell : spark을 배우기 위한 빠른 방법
- Web UI
  - standalone : 클러스터 매니저 
  - worker
  - driver
  - history server
  
  ### interactive shell
  - 폴더 구조 
  - bin : spark 실행 파일을 포함
  - sbin : spark process를 구동하는 파일 포함
  - conf : spark 설정 파일 포함
    - spark-env.sh
    - spark-default.properties
    - log4j.properties
    - example : spark 예제 

## Spark Software Components

- 종류
  - Spark Driver : spark context를 실행하는 프로세스
  - Spark Context : spark driver와 cluster manager 사이를 통신하는 역활
    - locally하게 돌리거나, cluster manager를 돌리는 역활
    - cluster manger : standalone, YARN
  - Spark Application
    - Workers program : 로컬 쓰레드나 클러스터 노드 위에서 spark executor 실행

- 실행

  1) Driver 실행 

  2) Spark Context이 실행되어 cluster manager와 spark driver을 연결
    - action이 실행되면, DAG 생성되고, DAG scheduler에 DAG 제출
    - DAG scheduler는 stage를 나눈다. (optimization) => 여러 map은 하나의 stage에 구성

  3) cluster manager가 클러스터의 spark executor를 할당
    - stage은 cluster manager안에 Task scheduler에 전송

  4) jar이나 python code 를 실행하면, spark context가 executor에 task를 전송

    - task가 새로운 JVM에서 실행

- operation의 종류

  1) Transformations 
    - Dataset 생성 및 변형
    - Map, Filter, Distinct
  2) Action
    - output을 반환, storage에 데이터 저장
    - Count, Reduce, Collect, Take
  3) Persistence
    - caching dataset
    - Disk or RAM에 저장 옵션
    - Persist, Cache



## Spark 명령어

- `sc` : Spark context
  - `sc.master` :  Spark master 확인
  - `sc.parallelize()` : Collection을 RDD로 변환하는 명령어
  - `sc.textFile('*.txt')` : Text를 RDD로 변환하는 명령어



- `spark` : Spark Session
- `RDD.filter(_ < 10)` : 10미만의 수 제거 (Transfer)
- `RDD.map(r => r + "_map")` : "_map"있는 단어 출력 (Transfer) 
- `RDD.collect()` : Collection 반환 (Action)
- `RDD.count()` : count 반환 (Action)
- `RDD.saveAsTextFile("newData")` : 새로운 텍스트 파일 저장



- `RDD.toDebugString` : Lineage 확인
- `RDD.getNumPartitions` : partition 갯수 확인
- `RDD.repartition(10)` : partition 갯수 변경



## Cache 부여
- 반복 계산의 성능 향상을 위해 RDD 캐시 실행
- Chaching했는 데 오래 걸릴 경우, Serialize 문제


- `Rdd.cache` : 캐싱 부여
- `Rdd.name` : 이름 부여
  - UI에서 Storage 탭에서 `Fraction Cached` 기록
    - take 50%, collect 100%
- `distData.getStorageLevel` : 캐시 storageLevel 확인
- `distData.unpersist()`: 캐시 삭제

- `sc.getPersistentRDDs` : 캐싱이 설정된 RDD목록 확인

### cache size 확인

- Object : 16byte
- String : 40byte (overhead) 
