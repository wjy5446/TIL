# Database DataType

## 1. Numeric

### 1-1. Integer types

- `TINYINT` : 1byte
- `SMALLINT` : 2 byte
- `MEDIUMINT` : 3 byte
- `INT` : 4 byte
- `BIGINT` : 8 byte



### 1-2. Floating-point types

- `FLOAT` : 4 byte 
  - `FLOAT(M,D)` : 고정 소수점 타입
- `DOUBLE` : 8 byte
  - `DOUBLE(M,D)` : 고정 소수점 타입



### 1-3. Fixed-point types

- `DECIMAL(M, D)` : 고정 소수점 표시
- `NUMERIC(M, D)` : 고정 소수점 표시



### 1-4. Bit value

- `BIT(M)` : M 비트의 범위를 표시



## 2. Date & Time

- `DATE` : "년-월-일"
- `TIME` : "시:분:초"
- `DATETIME` : "년-월-일 시:분:초"
- `TIMESTAMP` : 날짜와 시간을 저장
  - 날짜 입력하지 않을 시 현재 날짜와 시간 자동 저장
- `YEAR` : 연도 저장 
  - `YEAR(2)` : 2자리 연도
  - `YEAR(4)` : 4자리 연도



## 3. String

### 3-1. CHAR & VARCHAR

- `CHAR` : 고정된 크기로 저장된다. 
  - 우편번호와 같이 고정된 형태일 때 사용
- `VARCHAR` : 변화되는 크기로 저장
  - CHAR보다 데이터를 효율적으로 저장



### 3-2. TEXT

- `TEXT` : 큰 문자열을 저장할 때 사용
  - `TINYTEXT` : 255 byte
  - `TEXT` : 64kiB
  - `MEDIUMTEXT` : 16 MiB
  - `LONGTEXT` : 4 GiB



## Constraint

- `NOT NULL` : 비어있는 값을 저장할 수 없다.
- `UNIQUE` : 같은 값을 저장할 수 없다. 
- `PRIMARY KEY` : `NOT NULL` + `UNIQUE` 동시에 만족하는 값,
  - 테이블에 하나의 컬럼만 조건을 설정할 수 있다.
- `FOREIGN KEY` : 다른 테이블과 연결되는 값
- `DEFAULT 'values'`  : default값을 지정
- `AUTO_INCREMENT` : 숫자를 1로 증가시켜 저장