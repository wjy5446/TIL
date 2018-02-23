# 베이지안과 빈번론의 통계 접근

### Sample을 다루는 두가지 방법

- descriptive statistics : 샘플을 정량적인 방법으로 표현한 통계 (mean, variance 사용)
- inferenctial statistics : 샘플에서 일반적인 특징(모집단의 특징)을 찾아 표현한 통계
  - frequentist inference
  - bayesian inference



### Inferential statistics의 목표

##### 1. Parameter estimation

특정 확률 분포의 parameter를 알아내는 것

##### 2. Data prediction

이미 parameter가 정해지고 미래의 값을 예측

##### 3.Model camparison

여러 모델 중에서 적합한 모델을 찾아내는 과정. 

- 종속변수에 얼마나 독립변수가 영향을 주는 지 측정.



### Frequentist and Bayesian frameworks



**확률의 정의**

1. Long-term frequencies
2. Physical tendencies/propensities
3. Degrees of belief
4. Degrees of logical supportr



##### Frequentist

`Long-term frequencies`를 기반한 추론

- 반복가능한 사건이 확률을 가질 수 있다.
- 고정되어 있지만 unknown한 변수의 불확실성을 정량화하지 않는다.

##### Bayesian

`Degree of belief, Degree of logical support`를 기반한 추론

- 반복 불가능한 사건도 확률을 가질 수 있다.
- 변수에 대해 불확실성을 정량화한다.





### Parameter estimation and data prediction

정규분포를 따르는 여자 키 분포에서 mean을 구한 다고 할 때, 각 확률론자들의 시점



##### frequentist way

> 여자 키 평균은 모른다. 하지만 고정되어 있다는 사실은 안다. 그러므로 우리는 특정한 값이 평균일 확률과 그것보다 적거나 같을 확률을 구할 수 없다. 우리가 할 수 있는 것은 샘플 데이터를 최대한 모으고 **모집단 평균과 일치하는 샘플 평균 값을 추정하는 것**이다.

- maximum likelihood estimate



##### Bayesian way

> 평균이 고정되었고 알수없는 값인 것을 인정한다. 그러나 불확실성으로 확률을 표현이 가능하다. 평균이 가능한 값의 확률분포를 정의하고 sample data를 확률 분포를 업데이트하는 데 사용할 것이다.

- Bayes 정리를 이용해 parameter로 가능한 모든 변수의 확률 분포를 업데이트한다.

   

##### Frequentist vs Bayesian

- **이전 확률을 사용여부** 차이
- 하지만 실제로는 Frequentist는 불확실성을 제거한 것은 아니다. (측정시 틀릴 확률을 가지고 있다.)



##### Frequentist의 uncertainty 다루는 방법

- long-term error rate를 제한함
  - parameter가 null value일 때와 비교함(NHST, p-value)
  - confidence intetval을 계산 함

