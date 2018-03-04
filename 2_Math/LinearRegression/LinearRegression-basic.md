# Linear Regression

독립변수 $x$와 대응하는 종속변수 $y$ 관계를 정량화 하는 작업



### 종류

- Deterministic Model (결정론적 모형)
- Probabilistic Model (확률적 모형)



### 결정론적 모형

종속 변수 $y$와 비슷한 $\hat{y}$ 만드는 함수를 찾는 과정
$$
\hat{y} = f(x) \approx y
$$
$f(x)$가 선형이면 **선형 회귀분석** 
$$
\hat{y}=w_0+w_1x_1+w_2x_2+ \dots+w_Dx_D
$$
이 때, $w_0, w_1$은 cofficient, parameter



### 바이오스 오그멘테이션

식을 간단히 나타내기 위해 feature matrix에 1를 추가해 붙힌다. 이를 **bias augumentation**

- 보통 표시되지 않아도 bias augmentation를 추가한다.

`sm.add_constant(X0)`를 이용해 추가시킨다.



### OLS(Ordinary Least Squares)

기본적인 결정론적 선형 회귀 방법으로 잔차제곱합를 최소화하는 가중치 벡터를 구하는 방법


$$
RSS = e^Te=(y-Xw)^T(y-Xw) \\ 
\dfrac{dRSS}{dw}=-2X^Ty+2X^TXw=0 \\
w=(X^TX)^{-1}X^Ty
$$
$X^Ty-X^TXw=0$ 은 **Normal(수직) equation**



- $X^Te=0$ 임으로 모든 벡터 $x$ 와 잔차 $e$ 와 수직이다.



### OLS Programing

##### Numpy

`np.linalg.lstsq(X, y)` 이용

- 차원이 높아지면 알수없다.



##### sklearn

`linear_model` 서브패키지에서 `LinearRegression` 클래스 사용

- 오그멘테이션이 할 필요 없다.
- fit할 때 입출력 입력
- fit할 때 자기 자신을 반환(chain-call)



- `model = LinearRegression(fit_intercept=True)` : fit_intercept 가 상수항 입력 여부
- `model = model.fit(X, y)`
  - `coef_` : 가중치 벡터
  - `intercept_` : 상수항
- `model.predict(x_new)` : 출력 데이터 예측



- **단점**

  - 가중치에 대한 오차를 알수 없다. (가중치 오차)
  - 얼마나 가중치에 영향을 미치는 지 알수없다., 특징의 단위에 따라 가중치 크기가 달라질 수 있기 때문이다. (영향력)
  - 가중치가 독립인 지 아닌지 알수없다.(독립여부)

  ​

##### StatsModels

`OLS`를 이용해 사용

- 오그멘테이션 필요
- 클래스 생성시 데이터 입력
- summary report 출력



- `model = sm.OLS(y, X)`
- `result = model.fit()`
  - reult 객체를 반환
- `result.summary()`
  - `R-squared` : predict와 target의 상관계수
  - `coef` : 계수
  - `std err` : coef의 에러
  - `t` : 계수가 0이다 라는 귀무가설의 t test
  - `[0.025 0.975]` : t의 신뢰구간
  - `Omnibus, Jarque-Bera` : 잔차가 정규성인지 확인
-  : `result.predict()`



##### result 클래스

- 속성

  - `resid` : 잔차벡터
  - `param` : 모수 벡터

- plot_regress_exog

  `sm.graphics.plot_regress_exog(resutl, "CRIM")`

  - fitted plot : 예측값과 실제값 차이 확인, 아웃라이어 확인
  - Residual plot : residual과 x와의 관계 확인(관계가 없어야 한다.)
  - Paritial regression plot : 실제 계수과 실제값의 관계가 있는 지 확인
  - CCPR plot : 이것도 실제 계수와 실제값 관계가 있는 지 확인