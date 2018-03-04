# patsy 패키지

StatsModel의 `R style` 정의 방법을 지원



> from pasty import dmatrix 



### dmatrix

실험설계행렬(experiment design matrix) 제작 함수

> data_trans = dmatrix(formula, data)

- `formula` : 변환 방법
- `data` : dataframe



- formula만 입력시 현재 namespace에서 찾음
- data를 넣을 시 데이터플레임의 컬럼 namespace에서 찾음



- `자동 Agumentation` 지정 ("Intercept" 추가)

| intercept | x1   |
| --------- | ---- |
| 1         | 1    |
| 1         | 2    |



### formula 연산자

##### Intercept 제거

> dmatrix("x1 - 1")

> dmatrix("x1 + 0")

| x1   |
| ---- |
| 1    |
| 2    |



#####'+' 연산자

두 개 이상의 데이터 추가

>  dmatrix("x1 + x2")

| intercept | x1   | x2   |
| --------- | ---- | ---- |
| 1         | 1    | 3    |
| 1         | 2    | 4    |



##### ':' 연산자

두변수의 곱을 변수로 추가

> dmatrix("x1:x2")

| intercept | x1:x2 |
| --------- | ----- |
| 1         | 3     |
| 1         | 8     |

##### '*' 연산자

두 변수의 Interaction 계산

> dmatrix("x1*x2")

| intercept | x1   | x2   | x1:x2 |
| --------- | ---- | ---- | ----- |
| 1         | 1    | 3    | 3     |
| 1         | 2    | 4    | 8     |

- 두 변수가 동시가 일어 났을 때, 영향력이 클 때 사용



##### '/' 연산자

> dmatrix("x1 / x2")

| intercept | x1   | x1:x2 |
| --------- | ---- | ----- |
| 1         | 1    | 3     |
| 1         | 2    | 4     |

- x2가 촉매일 때 사용, 즉 x2는 영향력이 없지만 x1:x2일 때 영향력이 발생하는 경우



##### '~' 연산자

> sm.OLS.from_formula("y ~ x1 + x2")

- 왼쪽(종속 변수), 오른쪽(독립 변수)



### 변환

numpy 및 사용자 정의 함수를 이용해 자료 변환

- `center(n)` : 평균값
- ` standardize(x), scale(x)` : 평균 제거와 표준편차로 스케일링



### 변수 보호

`I(x)` : 실제 연산자를 이용할 때 사용

> dmatrix("I(x1 + x2)")

| intercept | I(x1+x2) |
| --------- | -------- |
| 1         | 4        |
| 1         | 6        |

##### 응용 (다항선형회귀)

> dmatrix("x1 + I(x1\*\*2) + I(x1\*\*3)")



### 카테고리 변수 인코딩

One-Hot-Encoding으로 카테고리 값 입력



