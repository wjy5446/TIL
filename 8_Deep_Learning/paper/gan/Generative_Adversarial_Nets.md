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

![algorithm](/Users/whale/Desktop/document/paper/summary/gan/image/5.png)



1. noise에서 m개의 noise sample 추출
2. 실제 데이터에서 m개의 data sample 추출
3. equ.1를 maximum하도록 discriminator 학습
4. 1-3을 여러번 학습
5. m개의 noise sample 추출
6. equ.1를 minimum하도록 generator 학습

* 여기서는 momentum 사용



## Theoretical Results

### 1. global optimum ($p_g = p_{data}$)

#### 1-1. first proof

**G가 고정되었을 때, optimum D $D^{*}_{G}(x)= {{p_{data}(x)}\over{p_{data}(x)+p_g(x)}}$이다.**

![eq1](/Users/whale/Desktop/document/paper/summary/gan/image/1.png)

- $p_z(z)$ 대신 $p_g(x)$을 이용.
- 이때, $a\log(y)+b\log(y)$의 최댓값은 ${a\over a+b}$  이다.
- 즉, $y=D(x), a=p_{data}(x), b=p_g(x)$ 라면, $D^*_G(x)={{p_{data}(x)}\over{p_{data}(x)+p_g(x)}}$

#### 1.2 second proof

 **최적의 값 $C(G)$은 $p_g=p_{data}$일 때이며 최소값은 $-log4$이다.**

![eq2](/Users/whale/Desktop/document/paper/summary/gan/image/2.png)	

- **1.1**에서 $D^{*}_{G}(x)= {{p_{data}(x)}\over{p_{data}(x)+p_g(x)}}$을 증명한 것을 대입

- 다음 식에 로그 안에 2를 나누고 곱해 주어 KLD 형태의 식을 나타낸다.

![eq3](/Users/whale/Desktop/document/paper/summary/gan/image/3.png)

- 다음 식은 jensen-shannon divergence로 표현이 가능

![eq4](/Users/whale/Desktop/document/paper/summary/gan/image/4.png)

- JSD는 양수만 가능하기 때문에 $C(G)= -log(4)$ , 그러므로 최소값이 되는 경우는, $p_{data}=p_g$만 가능 



**참고**

- KLD(Kullback - Leiber divergence)
  - Non-symmetric

$$
D_{KL}(P||Q) = \int p(x){{p(x)}\over{q(x)}}
$$

- JSD(Jensen-Shannon divergence)
  - Symmetric
  - 항상 non-zero
  - zero일 때 p와 q가 같음.

$$
JSD(P||Q) ={1\over2}D_{KL}(p||{p+q\over2})+{1\over2}D_{KL}(q||{p+q\over2})
$$



### 2. Convergence of Algorithm

#### 2.1 proof

**G, D가 충분한 capacity를 가질 경우, 최적화된 D에서 G는 항상 optimum에 도달한다.**

 ```
The subderivative pf supremum of convex functions include the derivative of the function at the point where the maximum is attained
 ```

-> convex 함수의 상한선의 서브 미분값은 최댓값에서의 함수의 미분값를 포함한다.

- subderivative : $\lim_\limits{x \rightarrow x_0^-}{f(x)-f(x_0)\over x-x_0}$,  $\lim\limits_{x \rightarrow x_0^+}{f(x)-f(x_0)\over x-x_0}$,



- $V(G, D)=U(p_g, D)$라고 했을 때, U가 $p_g$에대해 convex function이고 **1.1**에서 단일 최소값을 가진다. 그러므로 단일 최소값은 함수의 미분값이다.



- 하지만, 실제로 G가 multilayer perceptron로 이루워 졌을 때, 다수의 critical points가 있을 수 있다. 하지만 이론적 증명이 부족해도 multilayer을 이용하는 이유는 실제로 학습이 잘되기 때문이다.



## Experiments

- Dataset : MNIST, TFD, CIFAR-10
- Generative : rectifier linear activation, sigmoid activation
- Discriminative : maxout activation, Dropout
  - 이론적으로 중간 layer에서 dropout과 noise가 가능하지만, 실제로는 generator에 bottommost layer에 noise를 주었다.



- G에 의해 생성된 sample의 Gaussian Parzen Window를 fitting함으로 test set의 확률을 $p_g$에 fitting 시킴.
  - Parson window : 길이가 h인 d차원 공간내 샘플의 갯수



## Advantages and disadvantages

### Disadvantages

- $p_g(x)$의 표현이 명확하지 않다. 
- D와 G는 훈련하는 동안 싱크가 맞아야 한다. 
  - 특히, G는 D가 학습되지 않으면, 학습이 되지 않는다.
  - 'Helvetica scenario' : $p_{data}$에 비해, z가 같은 x 값을 출력하는 현상



### Advantages

- Markov chain이 필요하지 않다.
- inference가 필요하지 않는다.
- 다양한 함수가 모델로 나타낼 수 있다.



## Conclusions and future work

### future work

- G, D를 학습할 때, label c를 추가하여 conditional generative model 사용가능
- x가 주어졌을 때, z를 예측하는 auxiliary network를 학습함으로 approximate inference 학습 가능. (학습된 generator를 고정시킴으로..)
- x의 가르킴의 부분 집합인 S로 모든 conditional으로 모델이 가능하다. 

- Semi-supervised learning : 제한된 데이터를 가지고 있을 때, discriminator와 inference net의 feature를 이용해 classifier 성능을 증가.
- Efficiency improvements : G, D의 coordinating을 위한 방법을 고안하거나 더 좋은 z 분포를 사용하여 더 빠른 학습이 가능하다.