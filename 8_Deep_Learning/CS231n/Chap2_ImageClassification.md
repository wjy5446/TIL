# Image Classification pipeline

## 1. Image Classification

core task in computer Vision 

-> Detection, Segmentation, Image Captioning 가능



**The problem : Semantic gap**

- Viewpoint Variation : 시각에 따라 다르게 보임.
- illumination : 조명에 따라서 다르게 됨
- Deformation : 
- Occlusion : 방해물로 
- Background clutter : 배경과 색이 비슷
- Intraclass variation : 넓은 스펙트럼



> input : image
>
> output : labels
>
> -> 명백한 알고리즘이 존재하지 않는다.



**Image history**

>과거 : edge, shape, number value를 이용해 정렬
>
>predict만 존재



> 현재 : data-driven approach
>
> 1. 이미지를 모으고
> 2. machine learning을 이용해 train
> 3. image set으로 평가
>
> train, test 존재
>
> traing : image + label -> model
>
> test : model -> 



## Nearest Neignbor Classifier

train : memory 상에 image와 label 저장

test : 가장 가까운 데이터를 label로 지정

작업속도 : test data에 대해 O(n)

* CNN의 경우 train은 매우 느리다, test는 매우 빠르다.

=>  ANN, FLANN 빠르게 NN



**Distance**

- L1 distance : 절대값을 이용한 distance
- L2 distance : 제곱을 이용한 distance



**KNN**

- k개의 NN을 찾고 Vote를 통해 라벨을 찾는다.
- Hyperparameter : distance, k
  - hyperparameter 선택 : 문제마다 다르다. try error로 performance가 좋은 것을 선택
- 문제점
  - test performance이 않좋다.
  - distance는 정확하지 않는다.



**CIFAR- 10**

10개 label

50000 train image

10000 test image

32x32



## Set HyperParameter

- validation set를 생성
- 데이터가 적을 경우 Cross-validation 적용



## Linear classification

- pamametric approach

$$
f(x, W) \\
x : image \\
W : parameters
$$

- Linear classification 

이미지를 하나의 array 확장
$$
f(x, W) = Wx
$$
-> 이미지내 픽셀의 가중합이다.

-> color들의 count (color가 중요한 요소로 작용)

-> label당 score function 정의

-> 추후에는 loss function을 정의해야 된다.



- 해석
  - 공간상으로 선으로 나누는 것
- 단점
  - Negative 필름은 처리가 힘들다.
  - gray color는 분간이 힘들다.