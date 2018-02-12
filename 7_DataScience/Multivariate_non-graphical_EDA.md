# Multivariate non-graphical EDA

다변수 EDA 기술은 두개나 세개 이상의 변수를 cross-tabulation과 통계 형식으로 나타내는 방법이다.



## 4.4 Multivariate non-graphical EDA

### 4.4.1 cross-tabulation

- 두 변수 인 경우
  - columns(categorical data의 level) - row(categorical data의 level) - value(두 데이터를 모두 가지고 있는 데이터 갯수)
    - 추가적으로 row, column, total 합계 및 퍼센트 추가 할 수 있다.
- 여러 변수인 경우
  - columns(third value data의 level) - row(two value data)



### 4.4.2 Correlation for categorical data

카테고리 데이터의 여러 correlation 방법이 존재한다. 하지만 범위 밖임;;



### 4.4.3 Univariate statistics by category

카테고리 데이터와 실수형 데이터간의 데이터 분석

- 각 카테고리 level별 단변수 실수형 데이터 분석, 그리고 카테고리 level별로 비교
- 평균 비교는 ANOVA의 약식 버전
- 중앙값 비교는 단방향 ANOVA의 강력한 약식 버전
- spread분석은 동등한 분포를 가지고 있는 지 확인하는 간단한 버전



### 4.4.4 Correlation and covariance

#### Covariance

- 두 데이터가 얼마나 같이 변화하는 가를 측정(즉, 하나의 변수가 변화할 때, 다른 변수는 어떻게 변화하는 지 알려준다. )

$$
covariance = \dfrac{\sum(x_1-\mu)(x_2-\mu)}{N}
$$

- 양수일 때, 하나의 값이 상승하면, 다른 값도 상승한다는 의미
- 음수일 때, 하나의 값이 상승하면, 다른 값은 하강한다는 의미
- 0이면 두 변수는 독립적으로 움직인다는 의미



- $Cov(X,X)=Var(X)$


- covariance는 해석하기가 어렵다.



#### Correlation

- -1 과 1 사이에 나타내어 covariance보다 해석이 쉽다.

$$
Cor(X,Y)=\dfrac{Cov(X, Y)}{s_xs_t} \\
\\
\mbox{s_x : standard deviation of x} \\
\mbox{s_y : standard deviation of y}
$$

- -1이면, perfect하게 negative linear correlation
- +1이면, perfect하게 positive linear correlation
- 0이면, uncorrelation 



### 4.4.5 Covariance and correlation matrices

여러개 실수형 데이터를 이용한 EDA 방법은 두 데이터간의 covariance와 correlation를 하고 이를 matrix로 나타낸다. 

