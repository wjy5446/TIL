# 정보 이론

메세지의 기대 길이를 계산하기 위해서 사용 (통신), 놀람의 정도를 알기 위해 사용(확률) , 머신러닝에서는 확률분포의 특성, 확률 분포간 유사성을 정량화할 때 쓰인다.



## 1. Information ?

놀람의 정도, 예상치 못한 데이터(확률 쪽에서)

> "잘 일어나지 않는 사건"의 정보는 ""자주 발생하는 사건""보다 정보가 많다.

- 정의
  $$
  I(x)=-logP(x)
  $$

- 단위 

  * shannon, bit : 밑이 2 (통신에서 사용)
  * nat : 밑이 자연상수 (머신러닝에서 사용)

- 독립사건은 추가적인 정보량을 가진다. (그냥 정보량의 두 배)

- ​





## 2. Entropy ?

불확실성의 측정, 모든 사건의 정보량의 기대값 = Shannon entropy
$$
H(P)=E[I(x)] = -E[logP(x)] = -\Sigma p(k)logP(k)
$$

- 모든 사건이 균등하게 나올 때, 값이 가장 크게 나온다.
- 한 사건만 나왔을 때, 값이 가장 작다.





## 3. Cross Entropy

$$
H(P,Q)= -E[logQ(i)]=- \Sigma P(i)logQ(i)
$$



## 4. KL Divergence

두 확률 분포가 얼마나 "다른가" 알려주는 함수 (= `Relative Entropy`)

-> 정보를 얼마나 압축해 쓸 것인가를 알려주는 지표
$$
D_{KL}(P||Q)=\Sigma P(i)log\dfrac{P(i)}{Q(i)}
$$

### 4.1. 머신러닝에서의  KL-Divergence

확인 되지 않는 모델을 특정 확률분포로 근사시키기 위해서 사용된다.


$$
D_{KL}(P||Q)=\Sigma P(i)log\dfrac{P(i)}{Q(i)}
$$

- P : True distribution (Observation)
- Q : Theory, Model, (Approximation)
- Q가 P에 가깝게 만든다.



- 특징
  - 항상 0이상의 값을 갖는다.
  - 비대칭적이다. ($D_{KL}(p||q) \ne D_{KL}(q||p)$), 비대칭이기에 거리라고 표현하기 어려움
  - 확률분포가 동일할 때 KL-Divergence가 0이 된다.



### 4.2. KL-Divergence 분해

$$
\begin{eqnarray}
D_{KL}(P||Q)& =& \Sigma P(i)log\dfrac{P(i)}{Q(i)} \\ &=&\Sigma P(i)logP(i) - \Sigma P(i)logQ(i) \\ &=& -H(P)+H(P,Q)
\end{eqnarray}
$$

- KL-Divergence는 shannon entropy와 cross entropy로 나누어 질 수 있다. 
- 그러므로 실제 KL-Divergence를 최소화 할 때에는 cross entropy를 최소화하는 방향으로 진생한다. 

