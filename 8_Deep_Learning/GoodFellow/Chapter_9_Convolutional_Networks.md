# Chapter 9. Convolutional Networks

- 1d-time-series와 image에 특화된 NN

-  matrix multiplication 대신에 **convolution**을 이용해 계산하는 NN
  - 여기서 convolution은 수학적 conv와 다른 의미



## 9.1 The Convolution Operation

- convolution 
  - 일반적인 의미로, 두 함수의 연산 
  - 어떤 값 x에 weighting function w(a)를 적용한 것. 예를 들어 noise 제거
  - weight average이외의 다른 목적으로 사용 가능

$$
s(t)=\int x(a)w(t-a)da
$$

$$
s(t) = (x*w)(t)
$$

- convolution의 argument
  - x : input
  - w : kernel
  - output : feature map

-  실제로는 유한한 숫자 array의 summation으로 구성한다.

- 2차원에서의 convolution 
  $$
  S(i,j)= (I*K)(i,j)=\sum\sum I(m,n)K(i-m,j-n) \\
  S(i,j)= (K*I)(i,j)=\sum\sum I(i-m,j-n)K(m,n)
  $$

- 교환 법칙 성립

  - machine learning에서는 후자를 사용
  - 증명할 때 유용



- cross-correlation 
  - 딥러닝에서는 cross-correlation을 많이 사용
  - not flip

$$
S(i,j)= (I*K)(i,j)=\sum\sum I(i+m,j+n)K(m,n)
$$

- 이 책에서는 cross-correlation과 convolution을 convolution이라 부름

- kernel flip이 상관있을 때에는 명확히 명시.
- 머신러닝에서는 fliped 도니 kernel를 학습, 또한 홀로 사용되지 않고 다른 함수와 동시에 사용됨 그리고 이는 filp되지 않음.
- convolution은 Toeplitz matrix, doubly block circulant matrix와 같은 제약을 가짐, 또한 sparse matrix의 곱과 같다.
- 일반적으로는 계산의 효율을 위해 좀더 전문화 된 것을 사용한다.



## 9.2 Motivation

- convolution을 사용하는 이유
  - sparse interactions
  - parameter sharing
  - equivariant representation



- sparse interactions
  - 일반적으로 딥러닝은 input과 output의 interaction을 학습하는 것이다. 이는 output은 모든 input과 연관되어 있음
  - sparse interaction은 input보다 적은 kenel로만 연관되어 있음.
  - 딥러닝에서는 간접적으로 모든 input과 연관되어 있음.
  - **receptive field** : output에 영향을 주는 input영역
  - 장점 :
    - 적은 parameter 필요
    - memory 효율 증대
    - 통계적인 효율 증대



- Parameter sharing
  - 다른 레이어로 matrix를 곱할 때, 동등한 parameter 사용 (tied wieghts)
  - 즉, 따로 따로 학습하는 것이 아니라 하나의 set parameter를 학습
  - 장점:
    - forward propagaion running-time에는 영향이 없으나, memory 효율에는 좋다.



- equivariant represention

  - shared parameter에 의해서 생기는 특징이다.
  - equivarinat property

  $$
  f(g(x))=g(f(x))
  $$

  - 예)	
    - 이미지의 경우, 이미지가 shift되었을 때, 이에 대한 feature도 같은 양만큼 shift되어서 측정된다. 
    - convolution한 feature을 shift하는 것과 shift된 이미지를 convolution한 것이 같은 의미를 가짐
  - 실제로 Convolution은 scale, rotation에는 equivariant하지 않는다.,
  - 이는 몇몇 특징을 검출할 때 유용하다. 



- 마지막으로, 몇몇 종류의 data는 fixed-shape matrix의 곱으로 학습하지 못한다. 하지만 Convolution는 이를 가능하게 해준다. 



## 9.3 Pooling Layer

- convolution layer의 3단계
  - 1  단계 : convolution
  - 2 단계 : non-linear activation function (**detector**)
  - 3 단계 : pooling function
- 종류
  - max pooling : 사각 영역 내 최대 값 출력
  - average of a rectangular neighborhood
  - L2 norm of a rectangular neighborhood
  - weighted average based on the distance from the central pixel.
- pooling의 특징
  - 작은 이동에도 invariant 함.
  - 예를 들어, 얼굴을 찾을 때, 눈의 정확한 위치가 아니라, 눈의 대략적인 존재여부를 파악할 때 유의미하다.
  - pooling은 작은 이동에도 invariant해야 된다는 prior가 적용되는 것
  - max pooling시 어느 transformation에서 나왔는지 학습할 수 있다. 
  - detector unit보다 적은 수의 pooling unit 사용, (input 정보 정리)
    - computational efficiency 향상 시킴
- 변하기 쉬운 image를 다루는 데에 pooling은 필수적
  - pooling region에 offset를 변화시켜서 고정된 features size를 생성
- autoencoder, boltzman machine의 경우, pooling은 네트워크를 복잡하게 한다.



- 실제 convNet은 간단한 구조가 아니라, 많은 branch를 가지고 있다. 
- 1000 classifier convolution 구조의 종류
  - convolution, pooling을 거친 후, flattening한후 fully-connective layer 지남.
  - variable-pooling layer를 거친 후, fully-connective layer 지남.
  - conv, pooling을 거친 후, fc 대신에 conv를 이용해 클래스당 feature맵을 생성한 뒤, avg pooling 사용



## 9.4 Convolution and Pooling as an Infinitely Strong Prior

- prior probability distribution : 데이터를 보기 전에, 신뢰성을 encode한 모델의 파라미터 분포
- weak prior : 높은 variance를 가진 가우시안 분포 (높은 엔트로피)
- strong prior : 낮은 variance를 가진 가우시안 분포, 
  - 이럴경우, 파라미터 결과에 중요한 역활
- infinitely strong prior : 몇몇 파라미터에 zero probability를 가진 것.
  - 이런 경우, 그 파라미터 값은 절대로 금지 됨.



- convolution을 infinitely strong prior를 가진 FC로 생성할 수 있다. 
  - convolution의 사용은 infinitely strong prior로 간주.
    - 오직 local interaction, equivariant to translation
  - pooling의 경우도 small translation에 대한 invariant



- fully connective layer로 convolution net를 사용하는 건 매우 메모리적 낭비
  - 하지만 convolution이 어떻게 동작하는 지 알려줌.



- two insight
  - 첫번 째 인사이트 : pooling, convolution은 underfitting이 발생할 수 있음
    - prior가 합리적으로 정확할 때, pooling과 convolution이 잘 동작
    - 정확한 위치를 알아낼 때, Pooling을 사용하는 건 별로 좋지 않음
    - 또는, 멀리 떨어진 위치의 통합된 정보를 이용할 때에는 convolution이 부적절
  - 두번째 인사이트 : 확률적 학습 성능을 convolutional model끼리만 비교해야 한다.
    - 많은 이미지 데이터는 permutation invariant하고 학습을 통해 concept을 발견하는 모델과 디자이너에 의해 하드코딩된 공간적 지식을 가진 모델을 위한 별도의 benchmarks가 존재한다.??



## 9.5 Variants of the Basic Convolution Function

- neural network에서는 수학적인 convolution을 사용하지 않는다. 



- 실제 neural network의 convolution은 평행한 convolution application의 조합을 의미한다. 
  - 하나의 convolution은 하나의 feature만 추출, 하지만 우리는 다양한 위치의 많은 feature을 뽑기 원한다
- 실제로 multi-channnel convolution은 교환법칙이 성립하지 않음. 오직 input channel과 같은 output channel을 가질 때 동작.



- **convolution equation**

$$
Z_{i,j,k}=\sum V_{;,j+m-1,k+n-1}K_{i,l,m,n}
$$

- Z : output, (i : input channel, j : row, k :columns)
- V : input, (i : input channel, j : row, k : column)
- K : kernel, (i :output channel, j : input channel, k : row, l : columns) 



- **downsampled convolution**

  - stride를 증가시킨 convoltion
  - downsampling 효과 있음
  - 방향마다 다른 stride 적용가능

  

- **zero padding**

  - output을 만들기 위해 input에 zero-padding
  - 없다면, kernel 크기와 network의 깊이를 사이를 골라야 한다.
  - 종류
    - Valid convolution
      - no zero-padding
      - output의 크기가 줄어든다, deep하게 만드는 데 한계가 있음.
      - w(input width), k(kernel) -> m-k+1, kernel size의 크기가 커지면, 급격히 줄어듬
    - Same convolution
      - 같은 size를 만들기 위해서 zero-padding
      - 많은 layer 생성가능
      - 하지만, border에 있는 pixel은 적은 영향을 준다.
    - full convolution
      - kernel안에 하나의 픽셀이라도 있으면 zero-padding
      - m+k-1 output size
    - 적당한 값은 valid와 same 사이이다.



- unshared convolution
  - local에 따라 parameter를 공유하지 않은 convolution
  - locally connected layers
  - 각 feature가 작은 space의 함수로 이루어져있다는 사실을 알고 있을 때 가능.
  - 예를 들어, 얼굴 여부를 판단할 때, 입이 특정 위치에 존재하는 알 경우.