# 선형 회귀 가상 데이터 생성

### 선형 회귀

$$
y = b + Xw +e \\ 
\text{b : bias (N, 1)}, 아무 분포 \\
\text{X : feature (N, M)}, 아무분포 \\
\text{w : weight (M, 1)}, 아무 분포 \\
\text{e : error (N, 1)}, 정규 분포
$$

### error 가 정규 분포인 이유

y 는 여러 인수들의 조합으로 만들어 진다. 

- 그중에서 중요하지 않는 부분(disturbance) 은 여러 요소들의 합임으로 central limit theorem으로 정규 분포형태를 띈다.



### sklearn의 make_regression

`from sklearn.datasets import make_regression`



`make_regression()`

- 입력
  - `n_samples` : 표본 갯수 (N)
  - `n_features` : 특징점 갯수 (N)
  - `n_target` : 종속 변수 갯수 (y)
  - `bias` : 실수 (b)
  - `noise` : e의 표준편차
  - `coef` : w를 출력 할 것인지?
  - `random_state` : seed
- 출력
  - `X` : feature matrix (N, M)
  - `y` : target (N, 1)
  - `coef` : weight (N, 1)



### 그외 계수

##### 특징점이 두개 일 때

- `n_informative` : 독립 변수 중 종속변수와 관계가 있는 것들의 수
- `effective_rank` : 독립 변수 간에 독립인 독립 변수의 수
- `tail_strength` : 독립 변수 간에 상관관계 설정 (0.5 상관 없다.)