## 8.4 parameter Initialization Strategies

- Deep learning은 initial point 선택에 크게 영향을 받음.

- initialization이 영향을 주는 요소

  - converge 할지 말지
  - convergence 속도
  - convergence cost
  - generalization error

- initialization의 어려움

  - 딥러닝 구조가 이해하기 힘들기에 어려움 작업
  - 대다수가 intialization의 좋은 특징을 이용, 하지만 환경에 따라 특징도 달라짐.
  - optimization을 한다고 해도 generalization 관점에서 효과가 없을 수 있음

- **'break symmetry'**

  - 같은 unit에 같은 initialization 시에 똑같이 업데이트
  - 해결방법 : random initialization, Gram-Schmitdt(orthgonal_를 찾기 해서 ) orthogonalization, Random initialization from high-entropy dist.

- bias, extra parameters initialization

  - constant로 초기화

- uniform, gaussian 중요성은 아직 연구 되지 않음

- initial distribution의 scale의 중요성!! -> optimization, gerneralization에 영향

  - 장점 : symmetry breaking effect를 나타내고, signal 손실을 피함

  - 단점 : 너무 클 경우, exploding 효과 발생 (특히, RNN, But gradien clipping으로 해결), activation의 saturate 발생. 

    - RNN에서는 Batch Nomalization에서 사용

  - generalization 관점에서 early stop을 initialzation효과로 볼 수 있음.??

  - scale intialize의 방법
    - normalized initilaization (**Xivier initialization**)
      - input m개 있을 때 유니폼 dist U(-1/root(m), 1/root(m))으로 초기화 
      - 이는 모든 layer에 같은 variance, gradient variance를 주기 위해서 이다.
      - 이는 linear한 network를 가정, 하지만 대부분 nonlinear에서 잘 동작
    - orthogonal matrice initialization with gain factor 
      - **gain factor을 잘 정하는 것이 중요**
      - linear한 network 가정
      - g가 증가 할수록, forward은 활성화, backprop의 gradient 증가
      - g를 잘 조절하면 1000의 deep layer로 학습
      - 이런 이유는 random walk시에 activation과 gradient는 줄어들거나 폭발함. 하지만 g로 동일한 activation과 gradient를 유지한다면 학습이 잘됨.
      - **input의 norm과 output의 norm을 항상 비슷하게 유지해 주어야 한다.** 

  - 실제 initial weight의 최적 기준은 효과 없음
    - 이유
      - 실제 signal크기 유지하는 건 효과 없음
      - 학습이 시작되면 norm을 유지하기 힘듬
      - **optimization 속도를 높힐 수 있으나 generalization error 증가**

    - normalization initial은 layer가 극도 클 때 너무 작아진다. 

    - 이를 해결하기 위해, **sparse initialization** : k non-zero weight를 가지는 값으로 초기화, 전체 input의 크기를 input수에 독립적으로 생성

      - 이유 : 너무 딥러닝의 갯수가 커지게 되면, weight의 norm이 커지게 되므로 작게 해주어야 한다. 그러므로 이를 위해 대부분을 0으로 넣는다.

      - 장점 : 다양성을 성취
      - 단점 : large gaussian values를 사용시, 긴 시간이 걸림, maxout에서 문제 발생

  - dense, sparse initialization인 hyperparameter로 작용

  - inital scale을 찾는 좋은 방법
    - activation과 gradient의 minibatch의 표준 편차 범위를 확인
    - weight가 작으면, activation의 범위가 줄어들고, 첫 레이어는 매우 작아지고 weight는 증가.

- Bias의 initialization

  - 대부분 weight initialization은 0으로 초기화
  - non-zero로 초기화하는 경우
    - output unit에 bias 사용 : train-set output의 오른쪽 한계 통계를 적용한 역 activation function 값으로 초기화
      - 가정 : weight 값은 작고, output은 bias에 의해 결정
      - classification 뿐 만이라 auto-encoder, boltzmann machine에서 사용 ( input과 비슷한 값으로 initailization)
    - **saturation을 피하기 위해 bias 선택**
      - ReLU의 경우, 0.1로 초기화
      - random walk initialzation과는 같이 사용하지 않음
    - 어떤 unit이 다른 unit의 function 참여를 결정할 경우, 
      -  output u이고 gate h일 때, h를 1로 만들기 위해서 사용.
      -  gate 0으로 두면 학습이 되지 않기 때문.
      -  LSTM에서 1로 세팅

- variance or precision의 초기화 

  - 참고 : variance = 1/precision, linear regression의 분산
  - 보통은 1로 초기화 
  - 다른 방법은 weight가 충분히 0을 만든다면, output의 margin mean를 만들도록 bias를 초기화, output의 margin variance를 만들도록 variance 초기화 (train set의...)

- 또다른 initialization 방법

  - 같은 input으로 학습된 unsupervised model에 의해 학습된 파라미터로 supervised model 학습
  - 비슷한 작업을 수행하는 model로 학습
  - 심지어, 비슷하지 않는 작업을 수행하는 model로 학습해도 빠르게 학습
  - 이런 전략은 generalization에도 좋음

  

## 8.5 Algorithms with Adaptive Learning Rates

- parameter마다 다른 learning rate 적용, 자동적으로 adaptive한 learning rate 적용
- 사용 이유 : hyper parameter에 sensitive하게 적용.
- **delta-bar-delta algorithm**
  - 기본적인 방법
  - idea : loss의 편미분의 부호가 동일하면 learning_rate 증가, 부호가 변하면 learning_rate 감소
  - Full batch optimization일 때 가능  



### 8.5.1 AdaGrad

- 방법 : **지금까지의 loss의 제곱합의 제곱근에 반비례해서** learning_rates를 각 parameter에 adaptive하게 적용.
- 아이디어 : 지금까지 많이 학습된 것은 작은 파라미터를 적용하고, 지금까지 적게 학습되면 큰 파라미터 적용.
- 실험적으로, 학습 초기의 그래디언트 제곱합은 조기 과다 감소될 수 있다.
- 부분적인 deep learning에서 동작.
- 단점 : 시간이 지난 후에는 학습이 않될 수 있음



### 8.5.2 RMSProp

- 방법 : AdaGrad에서 gradient accumulation을 **exponentially weighted moving average**로 변경
  - exponentially weighted moving averate : $\rho r+(1-\rho)g$
- AdaGrad의 문제 : convex에서 잘동작하지만, 모든 gradient를 적용하여 learning rate가 convex 구조에 도착하기 전에 매우 작아짐.
- non-convex에서 convex 구조까지 빠르게 수렴
- 마치, AdaGrad를 convex에 초기화하는 것과 같음.
- parameter : $\rho$ : moving average length
- Netsterov momentum + RMSProp도 사용



### 8.5.3 Adam

- Adaptive moments의 준말
- RMSProp + momentum(조금은 다른 개념인)
- 1차 momentum  :$s=\rho s+(1-\rho)g$, 2차 momentum : $r=\rho r+(1-\rho)g^2$ 
- $s=s/1-\rho, r=r/1-\rho$
- $\theta=\theta-\epsilon \frac{s}{\sqrt{r}+\sigma}$
- Momentum in Adam
  - gradient에 1차 momentum 값이 측정으로 더해짐, 
    - 이론적 이유는 없음
  - 1차, 2차moment은 s와 r의 bias을 corrections하는 데 사용 
  - bias correction 하는 이유? 
    - exponential 값은 실제 더하는 값보다 적은 값을 가지게 된다. 그러므로 이를 보정하기 위해서.. 사용된다. 
- hyperparameter의 선택에 robust함
- parameter : $\rho_1, \rho_2$ 일반적으로 0.9 or 0.99, $\epsilon$ : 0.001



## 8.5.4 Right Optimization Algorithm

- 적합한 방법을 찾는 방법은 없음
- 하지만, adaptive learning rate 모델 (RMSProp, AdaDelta)가 좋은 성능을 보임.
- learning rate의 선택은 유저의 친숙도에 달려 있음 (parameter tuning이 쉬운 것)



## 8.7 Optimization Strategies and Meta-Algorithms

### 8.7.1 Batch Normalization

- 혁신적인 Optimization 방법 중 하나.
- Adaptive reparametrization
- 가장 큰 가장은 해당 레이어가 고정되어 있어야 한다. 
- 사실 back시 모든 레이어가 다 변하게 된다. 
- 엄청나게 크게 학습된다.
- Key Idea : learning rate 조정이 어려우니, activation을 조정.
- statictic normalization, 표준 정규 분포 만드는 것과 같다. 
- activation함수를 지나기 전에 batch normalization을 수행.
  - batch norm : batch들끼리 normalization
  -  layer norm : 같은 layer 끼리 normlaization
- test time에서는 이전에 train때 사용했던 mu, sigma를 저장해 두었다가, 전체 mu와 sigma를 이용해서 normalization한다. 
- Batch normalization은 deep model -> 한층으로 표현이 가능해진다. 
- 단점 : deep한 layer의 장점이 사라진다. 그러나 실제로는 한층으로 표현하는 것과 deep 장점을 같이 가져간다. 
- deep의 장점을 지우기 위해서는 $\gamma,\beta$를 사용 (없는 걸 vanila batch normalization)
  - 추가시 bias term이 없어진다.



### 8.7.2 Coodinate Descent

- J(H, W) 를 L1 Term 일때, H를 알고 있다고 가정하고 W를 학습하고, W를 알고 있다고 가정하고 H을 학습할 때, 이 두개를 번갈아가면서 학습하면 optimzation이 된다. 
- 어떤 한축에 대해서만 Descent를 시킨다. 