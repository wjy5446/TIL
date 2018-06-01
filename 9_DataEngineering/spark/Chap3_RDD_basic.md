# Chapter 3. RDD

## 3-1. RDD (Resilient Distributed Dataset)

- 분산되어 있는 데이터 요소


- 새로운 RDD 생성, 존재하는 RDD 변형, RDD에서 연산 호출 하면서 존재



## 3-2. RDD 기초

- 분산되어 있는 변경 불가능한 객체 모음
- 여러 클러스터에서 연산이 가능하도록 여러 **partition**으로 구성



#### 1) RDD 생성

- 외부 데이터세트 로드
- 드라이버 프로그램에서 객체 컬렉션 분산



### 2) RDD 연산 타입

- Transformation : 존재하는 RDD에서 새로운 RDD를 만들어 나는 것
  - filter()
  - 반환 타입 : RDD
- Action : RDD를 기초로 값을 계산해 드라이버 프로그램에 반환하거나 저장하는 것
  - first()
  - 반화 타입 : 그외 값



### 3) RDD 특징

- lazy evaluation : 액션이 사용되는 시점에서 처리
  - 메모리 공간 낭비 줄임
  - 필요한 데이터만 연산
- 액션이 실행될 때마다 새로 연산
  - RDD 재사용시 `RDD.persist()` 활용



### 4) RDD 동작 과정

1. 외부데이터에서 입력 RDD 생성
2. 트랜스포메이션을 이용해 새로운 RDD 정의
3. 재사용을 위해 `persist()` 요청
4. 병렬처리를 위해 액션 사용



## 3-3. RDD 생성

- 외부 데이터세트 로드
- 드라이버 프로그램내 데이터 집합 병렬화



### 1) paralleize()

- 프로그램내 데이터 집합을 병렬화

`lines = sc.parallelize(["pandas", "i like pandas"])`

- 머신 메모리에 모든 데이터 세트를 입력되기에 테스팅 목적으로 쓰임



### 2) textFile()

- 외부 스토리지에서 데이터 로드

`lines = sc.textFile("/path/Readme.md")`



## 3-4. RDD 연산

### 1) Transformation

- 실제 액션이 시작되는 시점에서 발현
- 한번에 하나의 요소만 동작
- 기존 RDD는 변경하는 것이 아니라, 새로운 RDD 포인터를 반환
- `RDD.union(RDD)` : 여러 RDD를 이용해 사용이 가능



### 2) Action

- 드라이버 프로그램에 결과 값을 반환 및 저장소에 기록
- `count()` : 데이터 갯수 
- `take()` : 여러개의 데이터 출력
- `collect()` : 전제 데이터 출력
  - 로컬에서 데이터를 처리할 때 사용
  - 충분한 데이터 크기만 사용가능



### 3) lazy evaluation

- action이 호출되었을 때만 연산을 처리
- 메타데이터에 연산이 요청되었다는 사실만 기록, 어떻게 계산할 지에 대한 명령어만  가짐
- 사용 이유 : 연산을 그룹지어서 데이터 전달 횟수를 줄이기 위해서..



### 4) 함수 전달 

- 람다식 이용

`rdd.filter(lambda s : "error" in s)`

- 상위 레벨 함수 전달

```
def containError(s):
	return "error" in s
word = rdd.filter(containError)
```

- 주의 : 전체 객체를 전달하지 말아야 한다. (직렬화된 객체가 포함 될수 있음)

```
## 객체 전체가 포함되는 처리
class x:
	def getMeRefer(self.isMat):
		return rdd.filter(lambda x : self.query in x)
```

```
## 객체 일부만 포함되게 처리
class x:
	def getMeRefer(self.isMat):
		query = self.query
    	return rdd.filter(lambda x : query in x)
```





## 3-5. 많이 쓰이는 트랜스포메이션, 액션

### 1) 기본 RDD (transformation)

- `filter()` : 함수 조건에 통과되는 값만 반환


- `map()` :  RDD 각 데이터에 적용하고 새로운 RDD 리터
  - 입력 타입과 반환 타입이 달라도 됨

```
nums = sc.parallelize([1,2,3,4])
square = nums.map(lambda x : x * x).collect()
```

- `flatMap()` : 입력 데이터에 대해 여러 개 아웃풋 데이터 생성
  - 여러 RDD가 포함되는 iterator내 요소들을 합쳐서 반환
  - flatten 효과를 만들 수 있다.

```
lines = sc.parallelize(["hello", "hi"])
words = lines.flatMap(lambda line :  line.split(" "))
```

- `sample(flase, 0.5)` : 복원추출, 비복원 추출로 표본 뽑아낸다.



- `distinct()` : 중복된 데이터 제거 (셔플링)
  - 데이터를 비교하기 위해서 연산량이 많다.
- `union()` :  단순히 두 집합을 합침 (중복 존재)
- `interaction()` : 두 집합에 존재하는 요소 출력 (중복 없음 셔플링)
- `substract()` : 집합내 interaction되는 요소 제거 (중복 없음 셔플링)
- `cartesian()` : 두 집합의 데이터 쌍 생성
  - 가능한 쌍의 유사성 파악시 사용
  - 연산량이 매우 많다.



### 2) 기본 RDD (action)

- 특정 타입 RDD에서 사용하는 경우가 있음
  - 수치형 RDD : mean, variance
  - 키 페어 RDD : join


- `reduce()` : 두 개의 데이터를 하나로 합쳐 하나의 데이터를 반환
  - 동일한 타입 반환

```
sum = rdd.reduce(lambda x, y : x + y)
```

- `fold(zero)(func)` : reduce와 같은 역할, 하지만 초기 호출 값을 받는다.
- `aggregate(zero)(seqOp, combOp)` : 여러개의 reduce 사용, 동일한 타입 전송 

```
sumCount = num.aggregate((0, 0),
			(lambda acc, value: (acc[0] + value, acc[1] + 1),
			(lambda acc1, acc2: (acc1[0] + acc2[0], acc1[1] + acc2[1]))))
return sumCount[0] / float(sumCount[1])
```

- `foreach(func)` : RDD의 func 적용



- `collect()` : RDD 전체 데이터 반환
  - 결과 비교가 쉬움
  - 모든 데이터가 단일 메모리에 업로드
- `take(n)` : n개의 특정 RDD을 반환
  - 순서대로 반환을 하지 않는다.
- `top()` : 상위 값만 반환
- `takeSample(withReplacement, num, seed)` : 비복원, 복원 표본 추출





- `count()` : RDD의 데이터 요소 갯수 
- `countByValue()` : RDD에 있는 각 데이터의 갯수
- `takeOrdered(num)(ordering)` : ordering 기준으로 num개 반환





## 3-6. 영속화(캐싱)

- RDD를 여러번 사용하고 싶을 때, 실제는 RDD에 의존되는 액션을 재연산
- 이를 방지하기 위해, 데이터 영속화 요청
- 영속화 요청시 계산한 파티션을 저장
- `persist()` : 캐싱, `unpersis()` : 캐싱 취소



- 너무 많은 데이터를 주었을 때, LRU로 파티션 삭제된다. 


- LRU(Least Recently Used) : 오랜된 파티션을 자동으로 버림

- 자주 사용할 시 필요한 데이터가 내려가고 다시 재계산될 확률이 높아진다.

  ​

### 1) 영속화의 종류

- `MEMORY_ONLY` : 공간사용(높음), CPU사용(낮음), 메모리 저장
- `MEMORY_ONLY_SER` : 공간사용(낮음), CPU사용(높음), 메모리 저장
- `MEMORY_AND_DISK` : 공간사용(높음), CPU사용(중간), 메모리, 디스크 일부 저장
- `MEMORY_AND_DISK_SER` : 공간사용(낮음), CPU사용(높음), 메모리, 디스크 일부 저장
- `DISK_ONLY` : 공간사용(낮음), CPU사용(높음), 디스크 저장