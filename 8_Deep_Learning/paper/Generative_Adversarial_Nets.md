# Generative Adversarial Net

## Abstract

- Discriminative model D : 생성된 data와 트레이닝 data를 구분하는 역할
- Generative model : Discriminative 모델을 속이는 역할
  - Gan은 G와 D의 minimax game이다.

- G와 D는 어느 곳이든 1/2를 보인다.

** 여기서 G, D는 multilayer perceptron



## Introduction

  딥러닝은 여러 데이터에 관한 확률 분포를 표현하는 풍부하고, 계층적인 모델이다. 지금까지 딥러닝은 **discriminative model**에서 큰 두각을 보여주었다. Backpropagation, Dropout 기법과 piecewise linear unit은 성공의 주된 요인이다. 반면에 **generative model**은 큰 영향을 주지 못했다. 그 이유는 1) 확률 계산을 근사화하는 데의 어려움, 2) piecewise linear unit의 사용의 어려움 이 있다. 하지만 여기서는 그 어려움을 극복하기 위한 새로운 genderative model 학습법을 소개한다.



  discriminative model은 위조범이고, generative model은 경찰이다. generative은 실제 데이터 분포와 비슷하게 만들고, discriminative은 실제 데이터와 가짜 데이터를 구분하도록 학습된다. 학습은 discriminative가 진품과 구분하지 못할 때까지 학습된다. 



  여기에서 discriminative와 generative은 multilayer perceptron을 이용한다.



## Adversarial nets

G(z; $\theta_g$) 은 input noise $p_z(z)$에서 z을 data space에 맵핑하는 함수이며, $D(x;\theta_d)$은 실제 데이터와 $p_g$ 데이터의 확률을 나타내는 함수이다.  



D는 `logD(x)+log(1-D(G(z)))`을 학습하며, 동시에 G는 `log(1-D(G(z)))`을 최소화 시키도록 학습한다. 

$$min_Gmax_DV(D,G)=E_{x~p_{data}(x)}[logD(x)]+E_{z~p_{z}(z)}[log(1-D(G(z)))] $$    

- D를 maximum할 경우, 진짜일 때는 1로 가짜일 때는 0으로 학습됨
- G를 minimum할 경우, 가짜일 1로 학습



이는 반복적이고, 수치적인 접근으로 학습한다. D가 overfit하기 전에 훈련을 중단시키고, G를 학습시킨다.



실제로 위 식은 충분한 gradient를 제공하지 않는다. 초기에 G가 매우 않좋기 때문에 학습이 되지 않는다. 이를 해결하기 위해서 log(1-D(G(z))) 최소화 보단 log(D(G(z)))를 최대화 시키는 방법을 사용한다.



### 학습 방법

1. noise에서 m개의 noise sample 추출
2. 실제 데이터에서 m개의 data sample 추출
3.  equ.1를 maximum하도록 discriminator 학습
4. 1-3을 여러번 학습
5. m개의 noise sample 추출
6. equ.1를 minimum하도록 generator 학습

* 여기서는 momentum 사용



## Theoretical Results

### 1. global optimum ($p_g = p_{data}$)

G가 고정되었을 때, optimum D는
$$
D^{*}_{G}(x)= {{p_{data}(x)}\over{p_{data}(x)+p_g(x)}}
$$


### 2. Optimize equtions 1



 