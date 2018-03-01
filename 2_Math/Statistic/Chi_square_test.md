# Chi square test

카이제곱 검정은 카테고리 변수 차이 및 관계를 분석하기 위한 방법



### 검정 목적

1. 독립성 검정(Testing Independence) : 두 변수가 서로 독립인 검정
2. 적합성 검정(goodness of fit test) 
   - 관측 데이터가 예측한 분포를 따르는 지 검정
3. 동일성 검정 : 두 집단의 분포가 동일한가?




- 조건
  - 임의 표집
  - 모집단의 크기가 표본 크기보다 10배
  - 범주형 변수
  - 변수 기댓값이 5이상인 경우




### 카이 제곱 적합도 검정

- 가설

  - $H_0$ : 자료는 특정 분포와 일치
  - $H_a$ : 자료는 특정 분포와 일치하지 않음

- 수행

-  $$
   \Sigma ^K_{k=1} \dfrac{(x_k-m_k)^2}{m_k}
   $$

   - $x_k$ : 각 카테고리별로 갯수
   - $m_k$ : 카테고리 별로 나오는 기대 횟수
   - 평균과 얼마나 가깝게 나왔는 지 확인



### 카이 제곱 동질성 검정

- 가설
  - $H_0$ : 각각 카테고리의 분포가 동일하다. (관계없음)
  - $H_a$ : 하나도 분포가 동일하지 않다. (종속적)
- 수행
  - Contingency table (Observation data)
  - Expect table (Expected data) : 서로 독립이라는 가정으로 생성된다. 즉, marginal 확률의 곱은 joint 확률이다.

$$
E_{i, j}=P(i)*P(j)*sampleSize
$$

- ​	contingency table과 expect table 비교

$$
\chi^{2} = \Sigma(O_i-E_i)^2/E_i
$$

- $DF = (row - 1)(column - 1)$
- 변수간에 연관이 없다면 같은 분포를 보인다.

