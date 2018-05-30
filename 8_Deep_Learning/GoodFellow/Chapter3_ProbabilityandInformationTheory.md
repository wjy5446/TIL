# Chapter 3. Probability and Information Theory

### 3.1 Why Probability

- 일반적인 컴퓨터 사이언스 : 정해져 있는 문제를 푼다.
- 머신러닝 : 불확실한 문제를 다룬다.



##### uncertainty의 이유

- Inherent stochasticity : 선척적으로 확률적인 문제 (양자역학)
- Incomplete observability : 정해져 있는 문제라도 관측이 정하지 않으면 문제 (Monty hall problem)
- Incomplete modeling : 모델을 사용할 때 정보 손실이 있을 때 버려진 문제는 uncertainty 하다.



##### probability의 종류

- frequentist probability : 이벤트가 발생한 횟수, 반복가능한
- bayesian probability : 신뢰도, 반복 불가능한



- probability는 불확실성을 다룬 logic이다.



### 3.2 Random Variables

랜덤적으로 다른 값을 받는 변수 (받을 수 있는 state)



##### 표기

$x_1, x_2$ : 생성된 변수

$x$ : random variable

- `probability distribution`은 어떻게 state가 나오는 지에 대한 설계도



##### 종류

- discrete : 유한하거나 셀수 있는 무한의 state인 경우
- continuous : 무한한 state인 경우
- random variable은 꼭 numeric data일 필요는 없다.



### 3.3 Probability Distributions

Random variable에서 어떻게 state가 나오는 지 묘사하는 것



#### 3.3.1 Discrete Variables and PMF

##### PMF

discrete variable을 나타내기 위한 확률 분포

##### 표기

- $P$ , $P(x=x)$, $x \sim P(x)$



##### Joint probability

여러 rv가 동시에 일어날 확률

##### 표기

- $P(x=x, y=y)$ or $P(x, y)$



##### 특징

- $P$ 의 도메인은 사용 가능한 $x$의 집합
- $0 \le P(x) \le 1$
- $\sum P(x)=1$



#### 3.3.2 Continuouse Variables and PDF