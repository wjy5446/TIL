# SQL_Intermediate

### 1. CEIL, ROUND, TRUNCATE

- `CEIL` : 소수를 올려 정수로 만든다.

`SELECT CEIL(12.345)` : 반드시 하나의 실수값이 들어가야 한다.

- `ROUND` : 반올림

`SELECT ROUND(12.345, 2)` : Default로 0이다.

- `TRUNCATE` : 버림

`SELECT TRUNCATE(12.345, 2)` : 반드시 파라미터로 2개가 들어가야 한다.



### 2. Conditional

- `if(조건, 참, 거짓)`

```
SELECT IF(population > 1, 'big', 'small')
from city
```

- `ifnull(참, 거짓)` : NULL(0) 값인 경우

```
SELECT IFNULL(indepYear, 0)
from city
```

- `case when(조건) then (출력) else (나머지 출력) end`

```
SELECT 
	CASE 
		WHEN pop > 1 THEN "UPPER"
		WHEN pop > 2 THEN "MIDDLE"
		ELSE "BOTTOMER"
	END
FROM country
```



### 3. DATE_FORMAT

날짜 데이터 포맷 변경

```
SELECT DATE_FORMAT(payment_date, "%T-%m") 
FROM payment
GROUP BY monthly
```



### 4. Sub-Query

- `Select`에서 sub-query

```
SELECT 
	(SELECT count(name) FROM city)
FROM DUAL
```



- `From`에서 sub-query

```
SELECT *
FROM 
	(SELECT countrycode FROM city WHERE pop > 800)
JOIN
	(SELECT code FROM country)
```

- from에서 사용시 JOIN 속도를 높혀 줄 수 있다.



- `WHERE`에서 sub-query

```
SELECT code
FROM country
WHERE code IN(SELECT DISTINCT(countrycode) FROM city)
```



### 5. INDEX

데이터를 빨리 찾을 수 있는 기능

```
CREATE INDEX 인덱스이름 ON 테이블 (칼럼이름1, 칼럼이름2)
```

- 장점 : 자주 사용할 수 있는 칼럼은 빠르게 검색할 수 있다.
- 단점 : 새로운 storage 필요, 추가 삭제, 삽입시 UPDATE 필요(속도가 느리다.)



```
EXPLAIN SELECT * FROM city
```

- EXPLAIN의 EXTRA에서 INDEX사용 여부 확인



### 6. VIEW

특정 데이터를 보기 위한 가상 테이블

- 실제로 데이터를 저장하지 않는다.
- 쿼리를 단순히 만들 때 사용

```
CREATE VIEW 뷰이름 AS (QOURY)
```





