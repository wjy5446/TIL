# Backpropagation and Neural Networks part 1

## 1. Computational Graph

각 그래프의 

- score function 정의
- loss function 정의 (+Regulazation)
- optimization

=> 실제로 엄청난 op가 있기 때문에 한번에 gradient를 구하는 계산이 매우 어렵다.



### example

> $f(x, y, z) = (x + y)z$
>
> q = x+y
>
> x = -2, y = 5, z = -4

- FP (Forward Pass)

$$
q = x+ y, \dfrac{dq}{dx}=1, \dfrac{dq}{dy}=1 \\
f=qz, \dfrac{df}{dq}=z, \dfrac{df}{dz}=q
$$

want : $ \dfrac{df}{dx},  \dfrac{df}{dy},  \dfrac{df}{dz}$



- BP (Backward Pass)

**chain rule**
$$
\dfrac{df}{dx}=  \dfrac{df}{dq}* \dfrac{dq}{dx} = -4 \\
 \dfrac{df}{dy}=  \dfrac{df}{dq}* \dfrac{dq}{dy} = -4 \\
 \dfrac{df}{dz} = 3 \\
$$
**local gradient** : 직접적인 gradient,  ex) $\dfrac{dq}{dx}$

**global gradient** :  간접적인 gradient , ex)  $\dfrac{df}{dq}$



- FP할 때 local gradient 계산이 가능 (메모리에 저장)
- BP할 때 global gradient 계산이 가능
- 결과적으로 local gradient와 global gradient를 곱해서 gradient가 구해진다



- `+`연산은 `gradient distribute`으로 그래도 global gradient를 전파한다.
- `*`연산은 `switcher` 서로 반대의 값을 곱하는 것이 된다.
- `max`연산은 `gradient router` 큰값만 통과시켜준다.



**logistic sigmoid의 특징**
$$
\sigma(x) = \dfrac{1}{1+e^{-x}} \\
\dfrac{d\sigma(x)}{dx}=(1-\sigma(x))\sigma(x)
$$


**gradients add at branch**

노드가 합쳐지는 경우: 단순히 더해주면 된다.



**실제 코드 구현**

```
class MultiplyGate(object):
	def forward(x, y):
		z = x*y
		self.x = x
		self.y = y
		return z
		
	def backward(dz):
		dx = self.y * dz
		dy = self.x * dz
		return [dx, dy]
```

- 입력이 보통은 벡터로 들어간다. (sample * )
- 그러므로 local gradient값은 Jacobian matrix가 된다.
- global gradient는 입력과 같은 차수가 된다. 



## 2. Neural Network

- Before : $f=Wx$
- After : $f=W_2max(0, W_1x)$
  - max는 activation function 비선형성을 위해 사용
- hidden 노드가 각각의 feature를 담당한다.
- 하나의 classifier에서 여러개의 classifier가 존재한다.



### 2-1. Activation Function 종류

- Sigmoid 
- tanh : tanh(x)
- ReLU : max(0, x)
- Leaky ReLU :  max(0.1x, x)
- Maxout
- ELU



### 2-2. Neural Networks: Architecture

- n - layer NN : weight를 가지는 layer (input은 제외)
- Fully Connected Layer



- hidden layer 가 늘어날 수록 분류 능력이 커진다.
- 하지만 이게 regularizer을 하는 것은 아니다. (overfitting 발생) regularization을 강하게 적용



