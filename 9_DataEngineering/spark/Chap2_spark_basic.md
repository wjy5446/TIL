### Chapter 2. 스파크 맛보기

- 스칼라로 제작되며, 가상머신(JVM)위에서 동작



## 2-1. Download spark

- http://spark.apache.org/downloads.html
- Download spark : [spark-2.3.0-bin-hadoop2.7.tgz](https://www.apache.org/dyn/closer.lua/spark/spark-2.3.0/spark-2.3.0-bin-hadoop2.7.tgz)
- Java jdk 설치 되어야 한다. (8- version), 10-version은 오류가 난다.




### 1) 파일 구성

- Readme : 스파크 소개
- bin : 다양한 방식의 스파크 실행 파일
- core, streaming, python : 주요 컴포넌트 소스
- examples : 스파크 API 예제 파일





### 2) 파이썬 쉘, 스칼라 쉘

- 여러 머신의 메모리에 존재하는 데이터들과 통신할 수 있도록하는 쉘
- 대화형 쉘 (파이썬, 스칼라) 존재



- spark는 연산과정을 자동으로 병렬화하여 작은 작업들의 모음으로 표현
  - 이 분산 데이터세트를 "RDD"라 표현




### 3) 간단한 RDD 생성

```
lines = sc.textFile("README.md") # RDD 생성
lines.count()
lines.first()
```





## 2.2 스파크 핵심 개념

- 클러스터에서 병렬 연산을 수행하는 드라이버 프로그램으로 구성
- 클러스터의 분산 데이터세트를 정의 및 수행
- 예 ) 스파크 쉘, 파이썬 쉘



- Driver : SparkContent(sc)으로 스파크에 접속 

  - main() 함수를 가지고 있는 프로그램
  - sc를 이용해 RDD를 생성할 수 있다.
  - 이는 다수의 Excutor를 관리

  ​

- Excutor : 병렬처리 태스크를 처리하는 역할 







## 2.3 단독 어플리케이션

- 독립적인 프로그램 내에서 스파크 사용이 가능
- 단지, 직접 SparkContext 객체를 초기화 해주어야 한다.



- 자바, 스칼라 경우 :  Maven 의존성 필드에 spark-core artifact  입력
  - Maven : 자바 기반 언어의 공개된 저장소의 라이브러리를 가져와 연결해주는 패키지 관리 툴
- 파이썬 경우 : 스크립트로 생성, 단, 실행은 spark-submit을 이용해 실행

`bin/spark-submit script.py`



### 1) sparkContext 초기화 

```
from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("My App")
sc = SparkContext(conf = conf)
```

- 파라미터
  - 클러스터 URL : local이라 쓰여 있는 부분, 어떻게 클러스터 접속할 지 알려줌
  - 애플리케이션 이름 : My App 부분, 클러스터 접속 후, 앱 이름으로 어플 구분
- 종료

`sc.stop()` or `System.exit(0)` 사용



