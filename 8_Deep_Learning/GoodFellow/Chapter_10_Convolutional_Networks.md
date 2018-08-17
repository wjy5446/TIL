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

