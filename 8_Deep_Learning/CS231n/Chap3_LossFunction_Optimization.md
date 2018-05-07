# Loss functions and Optimization

## 1. Loss function

얼마나 정답을 맞췄는 지는 정량화하는 함수

### 1-1. SVM (Hinge loss) 

- 잘못된 label들의 (정답 score의 차이)합
- Q3 : 제곱이 있으면 상황이 달라진다.(non-linear)
- Q4 : min : 0, max : $\infty$
- Q5 : W를 0으로 초기화하면 loss가 2이 된다.
  - sanity check에 사용(초기화가 잘되어 있는 지 확인)

$$
L_i = \sum_{j \ne y_i}{max(0,s_j - s_{y_i}+1)} \\
s_j : \mbox{잘못된 label의 score} \\
s_{y_i} :\mbox{ 잘된 label의 score} \\
1 : \mbox{safety margin}
$$

-> Error : Loss가 0으로 만드는 W가 Unique하지 않는다.

**weight Regularzation**
$$
L = \frac{1}{N}\sum^N_{i=1}\sum_{j \ne y_i }{max(0,f(x_ikW)_j-f(x_i;W)_{y_i}+1)} + \lambda R(W)
$$

- Regularzation 종류
  - L2 regularzation $R(W) = \sum_k\sum_l{W^2_{k,l}}$
    - 동일한 스코어라면 spread된 값을 선호
  - L1 regularzation $R(W) = \sum_k\sum_l{|W_{k,l}|}$
  - Elastic Net (L1 + L2)
  - Max norm regularization
  - Dropout
- Train performance은 않좋으나 Test performance는 좋은 결과를 낸다. 



### 1-2. Softmax classifier(Multinomial Logistic Regression)

$$
P(Y=k|X=x_i)=\dfrac{e^{s_k}}{\sum{e^{s_{j}}}}
$$

-> score는 unnormalized log probabilities of the class



**정답 log는 최대로 만들고 아닌 log는 0으로 만드는 것이 목적 **
$$
L_i=-logP(Y=y_i|X=x_i) \\
L_i=-logP(\dfrac{e^{s_k}}{\sum{e^{s_{j}}}})
$$

- Q1 log를 취하는 이유 : 수학적으로 장점이 있다.
- Q2 loss min, max : (0, $\infty$)
- Q3 W가 0일 때, loss? $-log(1/N)$ - sanity check



### 1-3. softmax vs SVM

- SVM은 score가 조금 변화되더라도 margin 때문에 변화가 크지 않다.
- softmax은 score에 매우 민감하다.



### 4. Recap

- score function : $s = Wx$

- Regulazation function : W

- loss function 

  - SVM 

  - Softmax

  - Full loss 
    $$
    L=\dfrac{1}{N}\sum^N_{i=1}L_i+R(W)
    $$




## 2. Optimization

### 2-1. Random search

최악 사용 : random으로 골라서 최적화를 찾는 방법



### 2-2. Follow the slope

- numerical gradient 
  - approximate
  - 계산 속도가 매우 느리다.

직접 수식을 이용해 gradient를 구하는 방식
$$
\dfrac{df(x)}{dx}=\lim_{h -> 0}{\dfrac{f(x+h)-f(x)}{h}}
$$

- analytic gradient
  - exact
  - fast
  - error가 될 확률이 높다.



- gradient check : 항상 analytic gradient를 사용, check할 때만 nemerical gradient 이용



### 2-3. Gradient Descent

$$
w_{k+1} = w_k -lr * \dfrac{df}{dw}
$$

- Mini-batch Gradient Descent
  - training set의 일부만 사용
  - 특정 데이터만 업데이트하기 때문에 noise가 생긴다. But, 장기적으로는 조금씩 줄어든다.
  - Minibatch size : CPU 환경에 따라 조절
  - learning rate에 따른 트레이닝 결과
    - very high learning rate : diverge, explode
    - low learning rate : slow
    - high learning rate : local minimum 
    - **Decay** : high learning -> low learning를 사용
  - 종류 : SGD
  - weight update : momentum, Adagrad, RMSProp, Adam



## 3. 과거 Image Classification

### 1. Image features

특징점 추출한후 하나의 columns vector로 합쳐준다.

- Color Histogram
  - 모든 컬러의 hue를 확인한 후에 histogram의 bin 갯수를 확인 
- Hog/SIFT
  - local pixel의 edge를 9bin 오리엔테이션을 추출
- Bag of Words
  - local patch의 frequence,  color등  vector로 만들고 사전화하여 test에서 가장 유사한 값을 찾고 histogram화 한다. ??





**과거와 현재 방식의 차이**

- 과거 : image -> featue Extraction -> concat features -> linear classification
- 현재 : image -> linear classification
- feature extraction 이 필요가 없다.