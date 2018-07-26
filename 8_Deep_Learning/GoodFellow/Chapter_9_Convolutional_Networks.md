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