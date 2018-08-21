# Chapter 10. Sequence Modeling : Recurrent and Recursive Nets

- sequence한 data를 다루는 network
- CNN이 다양한 크기의 이미지를 다루는 데 사용했다면, RNN은 다양한 크기의 sequencial data를 다루는 데 사용.



- Shared parameter : 문장같은 경우, 비슷한 위치에서 발생 단어가 발생하기에 가능, 또한 다양한 문장 길이를 학습하는데 가능. separately model 이용시 각 위치에 따른 단어 분포 규칙을 학습



- 1d-cnn : input 주변부만 확인하여 output을 생성, RNN : 이전에 썼던 output을 이용해 생성 (이전에 썼던 output에 동일한 법칙 적용) 

-> share parameter를 사용하면서 deep learing 모델 생성 가능



- minibatch를 이용해 실제 학습. 하지만 여기서는 minibatch notation 생략 -> time step은 실제 time이 아니라 sequence의 position이다.



## 10.1 Unfolding Computational Graphs

- 반복적인 system 사용

$$
s^{(t)}=f(s^{(t-1)};\theta)
$$

- directed acyclic computational graph으로 반복적인 equation 표현가능 -> node은 각 시간에 state를 표시, edge를 함수 f를 표현



- 전형적인 equation

$$
h^{(t)}=f(h^{(t-1)}, x^{(t)}; \theta)
$$

- hidden unit을 사용



**hidden unit**

- 과거 인풋의 task-relevant의 정리로 h를 사용
- input과 hidden unit을 이용해 생성하면, 학습시에 과거의 sequence에서 중요한 부분에 초점을 맞춘다. 
- input sequence에 대해서 거의 대부분을 h에 커버한다. like autoencode



- sequence length에 따라 size 결정



**RNN 표현방법**

- unfolded은 f의 반복
  - 장점
    - 길이와 상관없이, input은 항상 같은 사이즈이다. state에서 다른 하나의 state의 이동 관점으로 볼 수 있다.
    - 같은 parameter를 사용
    - single, sharded model은 sequence length의 일반화를 허락한다. 더 적은 parameter를 튜닝
    - 좀 더 명확한 방법을 보여줌으로 loss, backward를 명확히 알 수 있다.



## 10.2 Recurrent Neural Networks

### RNN의 종류

1)  time step마다 output을 생성. hidden 유닛이 hidden으로 입력, 

​	- input -> hidden (U), hidden -> hidden (W), hidden -> output (V)

2) time step마다 output 생성, output으로 hidden으로 입력

- 덜 파워풀하다. (output의 고차원이고 풍부하지 않는다면)
- hidden이 간접적으로 연결
- 독립적으로 훈련되기 때문에 학습속도가 빠르다. (parallelization)

3) hidden끼리 연결되고 오직 하나의 output을 생산.

- sequence 정리하기 위해서 사용.



- time step 마다 output 생성하는 것은 범용적이다. (Turning machine)
  - binary sequence input, output



### RNN Feed Forwad

- activation : hyperbolic tangent activation
- output : discrete (character), unnormalized log -> softmax


$$
a^{(t)}=b+Wh^{(t-1)}+Ux^{(t)}\\
h^{(t)}=tanh(a^{(t)})\\
o^{(t)}=c+Vh^{(t)}\\
\hat{y}^{(t)}=softmax(o^{(t)})
$$

- Loss

$$
L(\{x^{1},\dots ,x^{\tau}\},\{y^{1},\dots ,y^{\tau}\})\\
=-\Sigma \log p_{model}(y^{(t)}|\{x^{(1)}, \dots,x^{(t)}\})
$$



- expensice operation
  - running time $O(\tau)$



- parallelization 불가



- $O(\tau)$의 back-propagation 저장 공간 필요 

=> Back-Propagatuin through time (BPTT) -> 시간이 오래걸림



### 10.2.1 Teacher Forcing and Networks with Output Recuurence

- 2번째 방법은 1번째 방법보다 덜 파워풀하다. input의 과거 기록을 모두 필요하지 않기 때문이다.
- 장점은 독립적으로 계산하여, parallel이 가능.



#### Teacher forcing

- true output과 hidden unit을 연결하는 train 테크닉
- 장점 
  - time을 통한 back-prop을 피하게 도와준다.
  - BPTT와  techer forcing 동시에 사용 가능
- 단점 
  - open loop에서는 train에 사용된 input이 test에서 사용된 input과 다르다.
  - 해결방법 : teacher forced input과 free-running input을 둘다 학습
    - train에서 볼수 없는 input 조건 고려, ?
    - 실제값과 생성값의 차이를 random으로 골라서 사용.



### 10.2.2 Computing the Gradient in a Recurrent Neural Network

- 일반 gradient 계산 방법과 같다. 



### 10.2.3 Recurrent Networks as Directed Graphical Models

- Loss는 task에 따라 정의, 
  - Gaussian dist은 MSE 사용
- joint distribution

$$
P(Y)=P(y1, y2, y3, y\tau)=\prod P(yt|yt-1,yt-2,y1)
$$

- 모든 model은 관계가 없는 edge를 생략해 효율을 얻기 위해함.
- RNN은 이전 모든 관계 연관있을 때 효율적이다. (hidden이어주는 건 효율적)



- k에 의해 y 생성시 $O(k^{\tau})$
- share parameter $O(1)$
- 하지만 sequence의 중간을 예측하는 것은 계산적으로 힘들다.



- sharing parameter의 가정 : t까지 변수가 주어졌을 때 t+1의 확률분포는 **stationary**
  - **stationary** : 이전 step과 다음 step의 관계가 의존적이지 않음.



**sequence를 끝날지 말지를 결정하는 방법**

- vocabualry이용시에 end를 나타내는 symbol을 추가적으로 넣어주어야 한다. 
- 계속 생성할지, 말지에 대한 bernoulli dist를 사용 (general)
  - 어느 RNN에서 사용이 가능
  - sigmoid를 이용해 sequence 끝낼지 말지를 예측한다.
- sequnce length를 예측하는 output 생성
  - 추가적인 input이 필요, 즉, 남은 time step의 수
  - input이 없을 때, 갑자기 중단됨.



### 10.2.4 Modeling Sequences Conditioned on Context with RNNS

- 지금까지는 y에 대한 값만 다룸
- 하지만 보통은 x에 대해서 것도 다뤄진다.
- $P(y|x)$



**extra input**

- 각 step간에 input 입력

  - image captioning (input image)
  - $x^{T}R$은 hidden의 bias parameter로 사용

  

  - 보통은 x의 sequence가 입력되어 계산
  - 이 때 conditional independence assumption이 사용 
  - 하지만, 이 가정을 없애기 위해, t의 output과 t+1의 hidden 을 연결한다.
  - 이는 다양한 y의 sequence가 만들어진다.
  - 이런 방법은 항상x, y의 length가 같아야 한다.

- 초기 state hidden
- 둘다 사용



## 10.3 Bidirectional RNNs

- causal struction : 과거의 정보만 이용해 예측
- 하지만 몇몇 app은 전체 input sequence를 의존해 예측



- 예를 들어, speech recognition, sequnce to sequence, handwriting recognition, bioinformatics



- **Bidirectional RNN** : forward와 backward를 모두 고려해 output생성
  - 과거와 미래 둘래 의존하여 나타냄
  - t 주변 값에 민감하다.



- 2차원 이미지로 사용가능(up, down, left, right) 사용 가능
- convnet과 비교해 expensive하다.



## 10.4 Encoder-Decoder Sequence-to-Sequence Architectures

- input sequence를 같은 길이를 가지지 않는 output sequence를 학습시키는 법 (**encoder-decoder or sequence-to-sequence RNN**)
  - speech recognition, machine translation, question answering



- encoder를 이용해 context를 생성 (x를 요약하는 context)



- encoder : input sequence를 처리하여 context 생성
- decoder : context를 받아 output sequence를 사용
- $logP(y1,y2, yn|x1, x2,xn)$를 최대하도록 학습



- 단점 : input을 summarize하는 데 C의 차원이 너무 작다
  - 해결방안으로 fixed-size대신에 variable한 length사용



- **Attention mechanism** : output 요소와 context 요소를 합쳐서 학습