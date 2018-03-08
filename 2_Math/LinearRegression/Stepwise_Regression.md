# Stepwise Regression

F-test와 T-test를 이용해 독립변수를 제거하거나 추가하여 모델을 생성하는 방법



### 종류

##### 모든 독립변수를 넣고 시작 "Backward method"

- 독립변수가 충분히 많고 변수를 적게 삭제하고 싶을 때 사용
- 각 단계에서 작은 F-검정(F-to-add)의 p-value를 제거한다. 

##### 독립변수가 없는 것에서 시작 "Forward method"

- 독립변수가 매우 많을 때 사용
- 각 단계에서 큰 F-검정의 p-value를 추가한다. 



##### "Bidirectional Elimination"

- Foward method를 이용해 변수 선택한 후, Backward method를 이용해 변수를 제거, 이를 추가하거나 제거할 케이스가 없을 때까지 적용



### 장점 단점

##### 장점

- 많은 잠재적 예측변수값을 다룰 수 있는 능력을 가지고 있다.
- 다른 model-selection 방법보다 빠르게 사용 할 수 있다.
- 변수가 제거되는 순서를 볼 수 있다.



### 단점

- 변수가 충분하지 않을 때는 사용이 어렵다.
- R-square이 너무 높게 나온다. 
- 예측치와 신뢰구간이 너무 좁다.
- ​

