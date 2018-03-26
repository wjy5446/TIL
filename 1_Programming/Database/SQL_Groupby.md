# SQL_Groupby

### 1. GROUP

동일한 데이터를 가지는 컬럼을 합쳐주는 역할

- 합칠 때 **그룹함수**를 이용해 합쳐준다.

#### 1-1. COUNT

해당 데이터가 몇개 있는 지 확인

```
SELECT COUNT(DISTINCT(Language)) as population 
from country 
group by contitent
```

- 함수 밖에 함수 사용이 가능

#### 1-2. MAX, MIN

최댓값 최솟값 확인

```
SELECT MIN(population) 
FROM country
GROUP BY continent
```

#### 1-3. SUM

합계

```
SELECT SUM(population)
FROM country
GROUP BY continent
```

#### 1-4. AVG

평균

```
SELECT AVG(population)
FROM country
GROUP BY continent
```

- group by 하는 컬럼은 그냥 써줘도 distinct함수가 적용된다.



### 2. HAVING

group by에 조건을 주는 함수

- where은 전체 데이터에 조건을 줄 수 있다.

```
SELECT continent, SUM(population)
FROM country
GROUP BY continent
HAVING population > 50000
```



#### 문법 순서

* `where` > `group by` > `having` > `order by` > `limit`

