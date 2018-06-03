## 6.2 Gradient-Based Learning

### 6.2.1 Cost Functions

$$
J(\theta)=-E_{x, y\tilt \hat{p}_{data}}\log p_{model}(y | x)
$$





##  6.3 Hidden Units

- 보통 ReLu 사용, 하지만 다양한 Hidden Unit이 존재
- Hidden Unit에 미분 불가능한 점 존재, 하지만 이점은 무시



### 6.3.1 Rectified Linear Unit and Their Generalizations

$$
g(z)=max\{0, z\}
$$

- optimize가 쉽다.
- gradient가 크고 일정하다.
- 초기화할 때, 0.1과 같이 작은 양수로 선택하는 것이 좋다.
- 단점 : 음수에서 훈련이 어렵다.



#### 1) 변형

$$h_i=g(z, \alpha)_i=max(0, z_i)+\alpha_imin(0. z_i)$$

- Absolute value rectification : $\alpha = -1$
  - object recognition에 사용
- leaky ReLU : $\alpha_i = 0.01$ 
- parametric ReLU, PReLU : $\alpha_i$는 훈련 파라메터로 사용



#### 2) Maxout unit

$$
g(z)_i = max_{j \in G} z_j
$$

- z를 그룹으로 나누고 그룹안에서 최고 값을 선택한다.
- 적은 파라미터를 사용해 계산적, 통계적 이점을 가짐.
- maxout을 이용하면 general한 ReLu를 만들 수 있음.







### 6.3.2 Logistic Sigmoid and Hyperbolic Tangent

- Logistic sigmoid

$$
g(z) = \sigma(z)
$$

- hyperbolic tangent

$$
g(z) = tanh(z)
$$

- 둘의 관계

$$
tanh(z)=2\sigma(2z)-1
$$

- hyperbolic tanget > Logistic sigmoid : 훈련이 더 쉽게 된다.



### 6.3.3 Other Hidden Units

- 새로운 hidden unit은 상당한 성능을 보일 때만 의미를 갖는다.



- Linear unit : activation을 사용하지 않는 경우.
  - Parameter를 줄이는 효과를 가지고 있다.
- softmax unit : memory를 조작할 때 사용.



- Radial basis function : x에서 0으로 수렴하기 때문에, opimize에 적합하지 않다.
- softplus : rectifier의 smooth version
  - 직관적이지 않고, 실험적으로 미분값의 saturation이 높다.
  - 적합하지 않다. 
- Hard tanh : tanh, rectifier와 모양이 비슷, 하지만 성능은 떨어진다.





### 6.4 Architecture Design

- architecture : 전체적인 network의 구조
  - 얼마나 unit이 있는가?
  - 어떻게 연결되어 있는가?
- 대부분의 neural network은 chain structure의 layer로 이루어져 있다.
- structure의 중요성 : depth, width of layer
  - 깊을 수록, layer별로 적은 unit , parameter를 사용이 가능, 하지만 optimize가 어려워진다.
- 이상적인 model을 찾는 방법은 validation error에 대해서 참고해야 된다.




#### 6.4.1 Universal Approximation Properties and Depth

- universal approximation theorem : network에 hidden unit이 충분히 제공받는다면, 유한한 공간에서 원하는 0이 아닌 error로 매핑하는 Borel measurable function으로 근사 가능하다.
- neural network는 유한한 discrete 공간내 매핑하는 function으로 근사 가능
- 어떤 함수라든 MLP로 표현이 가능하다. 하지만 learning은 보장하지 않는다.
  - 이유 : 
  - optimization algorithm이 원하는 parameter를 찾을 수 없음
  - overfitting으로 잘못된 function을 찾을 수 없음



- deeper architecture은 unit수을 줄이고, generalization error를 줄일 수 있음.



=> neural network가 어느 함수든 표현이 가능하지만, 얼마나 depth를 가질 지는 설명해 주지 않는다.

- neural network가 표현할 수 있는 linear region의 수는 depth의 exponential에 비례한다.
- 하지만 모든 함수가 그런 특징을 가지고 있다는 보장은 없다.
- 단순히, deep model를 사용한다 할 때, 우리가 원하는 모델은 좀더 심플러한 모델의 조합으로 구성된다.



#### 6.4.2 Other Architecural Considerations

- 다양한 구조
  - CNN, RNN
  - Skip connections : i layer와 (i+2) layer를 연결하는 구조
    - 이유 :  gradient가 output layer에서 input layer까지 더 쉽게 흐르게 만든다.
- 두 layer를 연결하는 방법
  - input가 output을 전체를 연결하는 것이 아니라, 부분만 연결
    - 이유 : parameter의 수,  계산 속도 줄임
    - 문제에 의존적임
    - 예) CNN



## 6.5 Back-propagation and Other Differentaiation Algorithms

- forward propagation : input -> cost function
- back propagation : cost function -> input으로 진행되는 과정, (for gradient) 
  - gradient 계산하는 데, 간단하고 빠르다.



- 머신러닝에서, $\nabla  _\theta J(\theta)$, parameter에 대한 cost function의 gradient를 말함
- jacobian을 계산하는 데에도 사용할 수 있다.



### 6.5.1 Computational Graphs

- computational graph : backprop을 설명하기 위한 수단
  - Node : 변수(스칼라, 벡터, 행렬, 텐서)
  - Operation : Variable을 이용한 연산
  - x에서 y가 도출되면, x -> y 
  - operation이 생략되거나, output node에 operation이 명시



#### 6.5.2 Chain Rule of Calculus

- chain rule of calculus를 이용해 미분 값을 구함.
- 스칼라의 경우,

$$
\dfrac{dz}{dx}=\dfrac{dz}{dy} \dfrac{dy}{dx}
$$

- 벡터의 경우,

$$
\dfrac{\partial  z}{\partial x_i}=\sum_{i}\dfrac{\partial z}{\partial y_j} \dfrac{\partial y_j}{\partial x_i}
$$

$$
\nabla_xz = (\dfrac{\partial y}{\partial x})^{T}\nabla_yz
$$

- Jacobian matrix와 gradient의 곱으로 표시
- 텐서의 경우,

$$
\nabla_{\mathsf{X}}z = \sum_j(\nabla_{\mathsf{X}}\mathsf{Y}_j)\dfrac{\partial z}{\partial \mathsf{Y}_j}
$$



#### 6.5.3 Recursively Applying the Chain Rule to Obtain Backprop

#### 6.5.4 Back-Propagation Computation in Fully-Connected MLP

#### 6.5.5 Symbol-to-Symbol Derivatives

#### 6.5.6 General Back-Propagation

- dz/dz = 1에서 시작하여, 현재 계산된 gradient를 곱해 가면서 계산.
- back-propagation시 한 노드에 만나게 될 시, 합으로 계산.

##### 여러 subroutine : 

- get_operation(V) : V를 계산하는 operation을 return하는 함수
- get_consumers(V, g) : V의 자식을 return 하는 함수
- get_inputs(V, g) : V의 부모를 return 하는 함수
- bprop : jacovian-vector의 곱
  - 각 op는 bprop하는 법을 가지고 있다. 
- ​

