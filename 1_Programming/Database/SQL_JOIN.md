# SQL_JOIN

### 1. JOIN

여러개의 데이터를 모아서 보여줄 때 사용

- INNER JOIN
- LEFT JOIN
- RIGHT JOIN



#### 1-1. INNER

```
SELECT id
FROM user
JOIN addr
ON user.user_id = addr.user_id
```

둘 다 존재하는 데이터만 출력한다.



### 1-2. LEFT

```
SELECT id
FROM user
LEFT JOIN addr
ON user.user_id = addr.user_id
```

SELECT에 있는 데이터를 기준으로 테이블을 합쳐서 출력한다.



### 1-3. RIGHT

```
SELECT id
FROM user
RIGHT JOIN addr
ON user.user_id = addr.user_id
```

두 번째에 있는 테이블을 기준으로 합쳐서 출력한다.



### 2. UNION

두 테이블을 하나로 합쳐준다.

- 컬럼의 갯수, 타입, 순서가 같아야 한다.
- 자동으로 중복을 제거

```
SELECT name
FROM user
UNION (ALL) // 중복제거를 피할 때 사용
SELECT addr
FROM addr
```

