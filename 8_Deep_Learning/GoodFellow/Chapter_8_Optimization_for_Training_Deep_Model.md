# 8.4 parameter Initialization Strategies

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

- 'break symmetry'

  - 같은 unit에 같은 initialization 시에 똑같이 업데이트
  - 해결방법 : drop out, random initialization, Gram-Schmitdt orthogonalization, Random initialization from high-entropy dist.

- bias, extra parameters initialization

  - constant로 초기화

- uniform, gaussian 중요성은 아직 연구 되지 않음

- initial distribution의 scale의 중요성!! -> optimization, gerneralization에 영향

  - 장점 : symmetry breaking effect를 나타내고, signal 손실을 피함
  - 단점 : 너무 클 경우, exploding 효과 발생 (특히, RNN, But gradien clipping으로 해결), activation의 saturate 발생
  - generalization 관점에서 early stop을 initialzation효과로 볼 수 있음.??
  - scale intialize의 방법
    - normalized initilaization
      - input m개 있을 때 유니폼 dist U(-1/root(m), 1/root(m))으로 초기화 
      - 이는 모든 layer에 같은 variance, gradient variance를 주기 위해서 이다.
      - 이는 linear한 network를 가정, 하지만 대부분 nonlinear에서 잘 동작
    - orthogonal matrice initialization with gain factor g
      - linear한 network 가정
      - g가 증가 할수록, forward은 활성화, backprop의 gradient 증가
      - g를 잘 조절하면 1000의 deep layer로 학습
      - 이런 이유는 random walk시에 activation과 gradient는 줄어들거나 폭발함. 하지만 g로 동일한 activation과 gradient를 유지한다면 학습이 잘됨.
  - 실제 initial weight의 최적 기준은 효과 없음
    - 이유
      - 실제 signal크기 유지하는 건 효과 없음
      - 학습이 시작되면 norm을 유지하기 힘듬
      - optimization 속도를 높힐 수 있으나 generalization error 증가
    - normalization initial은 layer가 극도 클 때 너무 작아진다. 
    - 이를 해결하기 위해, **sparse initialization** : k non-zero weight를 가지는 값으로 초기화, 전체 input의 크기를 input수에 독립적으로 생성
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
    - saturation을 피하기 위해 bias 선택
      - ReLU의 경우, 0.1로 초기화
      - random walk initialzation과는 같이 사용하지 않음
    - 어떤 unit이 다른 unit의 function 참여를 결정할 경우, 
      -  output u이고 gate h일 때, h를 1로 만들기 위해서 사용.
      - LSTM에서 1로 세팅

- variance or precision의 초기화 

  - 참고 : variance = 1/precision, linear regression의 분산
  - 보통은 1로 초기화 
  - 다른 방법은 weight가 충분히 0을 만든다면, output의 margin mean를 만들도록 bias를 초기화, output의 margin variance를 만들도록 variance 초기화 (train set의...)

- 또다른 initialization 방법

  - 같은 input으로 학습된 unsupervised model에 의해 학습된 파라미터로 supervised model 학습
  - 비슷한 작업을 수행하는 model로 학습
  - 심지어, 비슷하지 않는 작업을 수행하는 model로 학습해도 빠르게 학습
  - 이런 전략은 generalization에도 좋음

  

   