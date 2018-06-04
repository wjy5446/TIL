# Chapter 4. 키/값 페어 RDD 

## 4-1. 배경

- 키/값 쌍을 가지고 있는 RDD
- 키에 대한 병렬처리, 그룹핑에 사용



## 4-2. 페어 RDD 생성

- `map() `를 이용한 생성
  - `pairs = lines.map(lambda x : (x.split(" ")[0], x))`
- `parallelize()`를 이용한 생성
  - 메모리에 있는 데이터로 RDD 생성 시에 사용
- 반드시 Tuple 형태로 반환



## 4-3. 페어 RDD의 트랜스포메이션

- Tuple을 다루는 함수로 변환
- 기본 RDD에서 지원하는 함수 사용 가능



- `filter()` : 필터링
  - `result = pairs.filter(lambda keyvalue : len(keyvalue[1]) < 20)`
- `mapvalues()`: 키 변경없이 값에 함수 적용



### 1) 집합 연산

- 동일 키별로 통계를 산출하는 작업

- `reduceByKey()` : 동일 키에 대해 reduce 작업을 한다.

  - 각 키별 총합과 갯를 구하는 작업
  - `rdd.mapvalues(lambda x : (x, 1)).reduceByKey(lambda x, y : (x[0] +y[0], x[1] + y[1]))`
  - 단어수 세기
  - `rdd.flatMap(lambda x : x.split(" ")).map(lambda x : (x, 1)).reduceByKey(lambda x , y : x+y)`

- `foldByKey()` : zeroValue부터 reduce 작업을 실행

- `combineByKey()` : 가장 일반적인 집합 연산 (다른 결과 타입을 사용해 합친다.)

  - `combineByKey(createCombiner, mergeValue, mergeCombiners, partitioner)`

  - 동작원리

    - 한 파티션 내 데이터를 하나씩 처리
    - 새로운 키값인 경우, createCombiner를 이용해 키에 대한 accumulator(공유변수)의 초기값 생성
      - 파티션에서 처음 나올 때 생성 !!
    - 이미 있는 키값인 경우, mergeValue를 이용해 accumulator값과 현재 값을 합침
    - 둘 이상의 파티션이 동일 키에 대해 accumulator를 가지는 경우, mergeCombiners()를 이용해 합침

  - 키 값별 평균 계산

    ```
    sumCount = nums.combineByKey((lambda x : (x, 1)), # createCombiner(1)
    							(lambda x, y : (x[0] + y, x[1] + 1)), # mergeValue(accum, value)
    							(lambda x, y : (x[0] + y[0], x[1] + y[1]))) # mergeComvbiner()
    ```

- 병렬화 수준 최적화

  - RDD는 고정된 파티션 갯수를 통해 병렬 처리
  - 보통은 클러스터 사이즈에 따라 파티션 갯수를 찾지만, 직접 지정이 가능
  - `sc.parallelize(data).reduceByKey(lambda x, y : x + y, 10)`, 두번째 인자로 입력
  - `repartition()` : 파티션 갯수 변경 
    - 파티션 구성 변경을 위해 데이터 교환 발생 (비용이 크다.)
  - `coalesce()` : 데이터 교환이 없이 파티션 갯수 줄임
    - `rdd.getNumPartitions()` : 파티션 갯수 확인



### 2) 데이터 그룹화

- 동일 키에 대해 그룹화 시킨다.
- `groupByKey()` : 동일 키에 대해 그룹화, return [key, [value]]
- `groupBy()` : 쌍을 이루지 않을 경우나, 키와 관계되지않는 다른 조건을 통해 그룹화
  - 함수 결과를 키로 사용해 그룹화시킨다.
- `cogroup()` : 여러 RDD를 그룹화
  - join을 위한 블록 구성을 위해 사용.
  - intersect에도 사용이 가능



## 3) Join

- `rdd.Join(other)` : inner join 수행
- `rdd.rightOuterJoin(other)` : other의 키 기준으로 join 수행
- `rdd.leftOuterJoin(other)` : rdd 기준으로 join 수행
- 상대쪽 값들은 Option으로 표시된다. Some(), NULL



## 4) 데이터 정렬

- `rdd.sortByKey()` : 키로 정렬된 RDD 반환
  - `rdd.sortByKey(ascending = True, numPartitions=None, keyfunc = lambda x : str(x))`



## 5) RDD 액션

- `countByKey()` : 각 키에 대한 갯수
- `collectAsMap()` : 쉬운 검색을 위해 결과를 맵 형채로 모은다.
- `lookup(key) ` : 들어온 키에 대한 값을 반환