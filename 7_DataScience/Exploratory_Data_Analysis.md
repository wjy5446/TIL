# Data Exploration

참고 자료 [[데이터 분석\]Data Exploration Guide](http://ourcstory.tistory.com/140?category=643554)



## 1. Step of DataExploration and Preparation

### Variable Identification

- Input과 Target 값 확인 
  - 변수 역활(예측값, 목표값)
  - 데이터 종류(문자형, 숫자형)
  - 카테고리 종류(카테고리형, 실수형)

### Univariate Analysis

- Continous Variables
  - Central tendency - Mean(평균), Median(중앙값), Mode(최빈값)
  - Spread - variance(분산), standard deviation(표준 편차)
  - skewness, kurtosis
  - 시각화 : histogram, box plot이용
- Categorical Variable
  - Count, ratio
  - 시각화 : bar plot, pie plot 

## Bi-variate Analysis

- Continous & Continous
  - Correlation : strength of relationship
  - 시각화 : scatter plot, heatmap(correlation)
- Categorical & Categorical
  - two-way table : 두 컬럼의 Count, ratio
  - 시각화 : stacked bar plot
  - Chi-Square Test
- Categorical & Continuous
  - Box plot : 카테고리의 level별 분포 확인
  - Z-test : 두 그룹간 statistically 얼마나 다른지 평균
  - T-test
  - ANOVA : 두 그룹의 statistically 다른 정도의 평균

## 2. Missing Value Treatment

- Missing value의 영향 : model이 biased 되거나 power나 fit을 감소시킨다.

### Missing value 발생 원인

- Data Extraction : 데이터를 추출하는 과정에서 발생한 원인
  - hashing procedures를 이용해 추출
- Data Collection : 데이터를 수집하는 과정에서 생기는 오류 
  -  Missing completely at random : 누락 가능성이 동등한 경우
  -  Missing at random : 누락되는 비율이 다른 경우 
  -  Missing that depend on unobserved predictors 
  -  Mssing that depends on the missing value itself

### Missing Value 처리 방법

- Deletion
  - List Wise Deletion : missing value가 포함되어 있는 row 삭제
    - sample size가 줄어 든다.
  - pair wise deletion : 해당 missing value만 제거
    - sample size는 유지하나 variable마다 크기가 다르다.
  - "Missing completely at random"경우에만 사용, 그냥 사용시 model이 bias 될 수 있다. 
- Mean/Mode/Median Imputation
  - Generalized Imputation : missing values 이외의 Mean, Median 값을 채워 넣는 방법
  - Similare case Imputation : 
- Prediction Model
  - 가장 Sophisticated method
  - predictive model를 생성하고 missing data를 estimate하는 방법
  - 방법 : missing data가 포함되지 않는 set를 training data,  missing data가 포함된 set를 dest data로 사용  
  - data set간에 relation이 존재해야 예측이 가능
- KNN Imputation
  - 연관성이 있는 attribution를 찾고 distance function을 통해 계산 확인
  - 장점
    - 예측이 가능하고 predictive model 생성이 필요 없다.
  - 단점
    - large 데이터에서 시간 소모가 많다. 
    - 적절한 k 값을 선택 



## 3. Oulier treatment

### Outlier 종류

- Univariate
- Multivariate 
- univariate에서 발견하지 못한 outlier가 multivariate에서 발견될 수 있다.



### Outlier의 원인

- Error / Non-Natural
  - Data Entry Error : 사람이 데이터를 수집하는 과정에서 발생하는 에러
  - Measurement Error : 데이터를 측정하는 과정에서 발생하는 에러 
  - Experimental Error : 다른 실험조건에서 발생한 에러
  - Intentional Outlier : 민감한 질문에 대해서 거짓된 답변을 했을 경우 발생한 에러
  - Data processing Error : 데이터를 추출하거나 조합할 때 발생한 에러
  - Sampling Error : 데이터를 샘플링하는 경우 발생한 에러
- Natural 
  - 자연적으로 발생한 outlier



### Outlier가 데이터에 미치는 영향

- error variance 증가 , tests power 감소
- normality 감소
- regression, ANOVA, statistical model assumptions에 영향



### Outlier 발견 방법

- Visualization을 통해 발견
  - Box plot, Histogram, Scatter plot
  - 값이 -1.5\*IQR ~ 1.5\*IQR을 벗어나는 경우
  - Capping method : 백분위수 5~95를 벗어나는 경우
  - Data points : mean, standard deviation을 이용해 outlier 측정
  - influence, leverage, distance를 이용해 outliers 측정 



### Outlier 제거 방법

- Deletion : outlier 삭제
- Transfroming : 자연로그를 취해 extreme value 값 감소
- Binning values : bin 구간 평균을 사용해 outlier 제거
- Imputating : 평균, 중간, 중앙값 사용, 
  - natrual, artificial를 분석하고 artificial일 때, imputing
- Treat Separately : outlier가 많이 발생할 경우 두 그룹을 따로 따로 처리한다. 



## 4. Feature enineering

feature를 변경하거나 새롭게 추가해 모델링하는 방법

### Variable transformation

- 데이터를 모델링하는 과정에서 함수를 통해 변수를 변형하는 과정(square, cube root, logarithm)
  - non linear -> linear로 변경할 때 사용(logarithm)
  - skewed dist -> symmetric dist로 변경할 때 사용(logarithm)
  - categorizing을 통해 binning



- 종류
  - Logarithm 
    - 오른쪽 skewness 감소 및 non-linear 감소
    - 0과 negitive 값은 적용 불가
  - Square / Cube root
    - cube root는 0과 negative 적용 가능
  - Binning : 기존의 데이터를 categorize할 때 사용
    - Domain 지식으로 결정



### variable/feature creation

- 기존의 variables/features를 이용해 새로운 variables/feature를 만드는 과정 



- 종류
  - creating dervived variables : 기존 변수를 이용해 새로운 변수를 생성
  - creating dummy variables : 카테고리 데이터를 numerical 변수로 변경하는 것 