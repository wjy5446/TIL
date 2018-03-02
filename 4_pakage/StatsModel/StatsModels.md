# StatsModels

기초 통계, 회귀 분석, 시계열 분석 기능을 제공하는 파이썬 패키지, 특히 시계열 분석에 강력하다.

- R에 있는 패키지를 파이썬을 옮긴 패키지 (patst), R보다 다양
- Document는 빈약하나 강력한 분석 기능을 제공한다.



### 기능

##### 기초 통계

- `검정 기능`
- `커널 밀도 추정`
- `Generalized Method of Moments`



##### 회귀 분석

- `Linear Model`
- `Generalized Linear Model`
- `Robust Linear Model`
- `Linear Mixed Effects Model`
- `ANOVA(Analysis of Variance)`



##### 시계열 분석 (Time series Analysis)

- `ARMA/ARIMA Process`
- `Vector ARMA Process`



### 선언

`import statsmodels.api as sm`



### 샘플 데이터 가져오기

- <http://vincentarelbundock.github.io/Rdatasets/datasets.html> : dataset 목록

`sm.datasets.get_rdataset(item, package="datasets")` : 인터넷에 있는 데이터 가져오는 함수

- 속성
  - `data` : 데이터프래임
  - `__doc__` : 데이터에 대한 설명 문자열, R 패키지 설명으로 가져온다.