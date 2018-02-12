# Javascript basic

## 식별자

- 상수 : snake_case(대문자)

  `var TOTAL_COUNT`

- 변수 : camel case

  `var firstName`



## 데이터 타입

- number

  `a=1`, `b=1.9`

- string

  `c="data"`

- object

  `d=[1,2,3]`, `e={"a":1, "d":2}`

- boolean

  `f=true`, `g=false` (소문자)

- `typeof()` : 데이터 타입 확인



#### 특이한 데이터

- `null` : 값이 없음 `var a = null`
- `undefined` : 값이 지정되지 않음 `var b`
- `NaN` : 존재하지 않는 데이터 `var c = 0/0`



## 연산자

`+, -, *, /, %` : 기본 연산자

`++` : +1

`--` : -1

- 연산자 우선순위 : `*` > '-'



### 비교 연산자

- `==` : 값을 비교

  `1==1` : true, `1=="1"` : true

- `===` : 데이터 타입까지 비교

  `1===1` : true, `1==="1"` : false

  - NaN은 비교가 되지 않는다. 무조건 false



- `!=` : 같지 않다.

  `1!=1` : false, `1!="1"` : false

- `!==` : 데이터 타입까지 비r교

  `1!==1` : false, `1!=="1"` : true



- `>, <, >=, <=` : 크기 비교



### 할당 연산자

- `+=, -=, *=, /=, %=` : 할당 연산자



### 논리 연산자

- `&&` : 모두 참일때 참
- `||` : 하나라도 참일때 참



## 출력

`console.log()` : 값 출력