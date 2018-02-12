# Exploratory Data Analysis

주어진 자료만 가지고 데이터의 정보를 찾을 수 있도록 도움을 주는 데이터 분석 방법



## 목적

- 오류 탐색
- 가설을 점검
- 적절한 모델 선정
- 변수간의 관계 탐색
- 데이터의 이해





## EDA의 종류

- univariate + non-graphical
- univariate + graphical
- multivariate + non-graphical
- multivatiate + graphical



- 추가적으로 Role (outcome or explanatory), Type (categorical or quantitative)으로 나누어 질수 있다.





## Univariate non-graphical EDA

### 목표

- 적합한 sample distribution를 찾는것
- sample disribution으로 population distribution을 찾는 것
- Outlier 검출



### Categorical data

- 특성

  - 값의 범위
  - 빈출도

- 표 (count, proportion, percent + total)

  ​

### Quantitative data

Quantitative data는 변수의 모집단 분포를 미리 평가 하는 데 가장 좋은 방법

- 종류
  - center, spread, modlity, shape, outliers

  ​

#### central tendency 

전형적인 중간값 측정(mean, median, mode)

- arithmetic mean(평균)
  - 비율이 균등할 때 사용 or symmetric dist
- median(중간값)
  - skewed dist or outlier detection에서 사용
- mode(최빈값)





#### Spread 

 중앙에서 분산된 정도 (variance, standard deviation, interquartile range)

- variance(분산)

  - ANOVA
    $$
    s^2 = \dfrac{SS}{df} \\
    \mbox{SS  is  sum of squared deviations} \\
    \mbox{df is defrees of freedom}
    $$

  - 제곱단위로 원래데이터 단위가 다른다.

  ​

- standard deviation(표준 편차)

  - 데이터가 정규분포일 때, 표준 편차를 이용해  데이터 비율을 알 수 있다.



- interquartile range(IQR)

  - quartiles : 데이터를 오름차순으로 정렬하고 4분위 했을 때, 4개로 나눈 3 data

    - Q1(first quartile) : 작은 것에서 25% 
    - Q2(second quartile) : 작은 것에서 50% = median
    - Q3(third quartile) : 작은 것에서 75%

    ​

  - **계산 방법**
    $$
    IQR = Q3 - Q1
    $$

  - 데이터가 펴져있다면 IQR로 퍼진다.

  - 분산이나 표준편차 보다 좀 더 강경한 측정방법이다.  (outlier가 IQR에 영향을 미치지 않는단.)

  - 대조적으로, range(최솟값과 최댓값의 거리)는 강경하지 않는다. But, 최솟값, 최댓값은 outlier 혹은 data entry error를 고르는 데 사용된다.

  - 정규분포에서 IQR = standard deviratin  * 3/4



#### Skewness and kurtosis

- skewness : 분포의 비대칭 정도

$$
\dfrac{E(X-\mu)^3}{(\sigma^2)^3/2} \\
\mbox{a = 0 : 정규 분포} \\
\mbox{a<0 : 우측으로 치우침} \\
\mbox{a>0 : 좌측으로 치우침}
$$

$$
-2SE(e) \lt  e \lt 2SE(e) : 정규 분포 \\
e \le -2SE(e) : 우측으로 치우침 \\
e \ge 2SE(e) : 좌측으로 치우침
$$



- kurtosis : Gaussian shape에서 자료가 얼마나 중앙에 분포하는 지 측정 (첨도)

$$
\dfrac{E(X-\mu)^4}{(\sigma^2)^2} \\
\mbox{a=3 : 정규분포} \\
\mbox{a<3 : 평평함} \\
\mbox{a>3 : 뾰족함}
$$

$$
-2SE(u) \lt u \lt 2SE(u) : 정규분포 \\
u \le -2SE(u) : 평평함 \\
u \ge 2SE(u) : 뽀족함
$$
