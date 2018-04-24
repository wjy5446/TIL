# Theano

GPU 지원하는 Symbolic Linear Algebra Complier

단일 컴퓨터에서 사용



### Symbolic Compiler

- 미분을 빠르게 처리
- 수식을 재정리하여 최적의 계산 경로를 찾음



### GPGPU

General-Purpose computing on Graphics Processing Units, 그래픽 처리를 하기 위한 GPU를 CPU 연산 용도로 사용하는 것, 

- 성능은 CPU보다 낮지만 다수의 코어를 지원
- CPU와 연산 설계가 달라 GPU 연산에 맞게 Compiling이 요구 됨.



- 예 : CUDA(Nvidia), OpenCL(Apple, AMD, Intel)



### Theano 사용



- **심볼 변수 정의**

```
import theano
import theano.tensor as T
```

```
x1 = T.dscalar('x1')
x2 = T.dvector('x2')
x3 = T.dmatrix('x3')
```



- **심볼 관계 정의**

```
z1 = x1 + x2 # add
z2 = T.exp(x1) # exp
z3 = T.dot(x1, x2) # multiple 
z4 = T.sum(x3) + T.mean(x3)
```



- **심볼 함수 정의**

```
f1 = theano.function(inputs=[x1, x2], output=z2) # 함수 정의

f1(1, 2) # 함수 계산
```

```
f1 = theano.function([x1, theano.In(y1, value-2)], z2) # In Default로 값 지정
```

```
from theano.tensor.shared_randomstreams import RandomStreams

rng = RandomStreams(0)
rv = rng.uniform()
f_rv = theano.function([], rv)

f_rv()
```



- **변수 갱신**

갱신되는 값은 공유 메모리(shared memory)에 저장

```
w1 = theano.shared(0.0, name="w1")
update = theano.function([x1], y1, givens=[(y1, w1)], update=[(w1, w1 + x1)])
```

- given : y1에 w1를 대체한다. (pair로 존재)
- updates : 업데이트 방식 (업데이트 저장 공간, 업데이트 식) 반드시 pair로 존재

```
w1.set_value(f_rv()) # 초기화 w1
w1.get_value() # w1 얻기
```

```
update(1)
```



- **미분**

```
gy1 = T.grad(y1, x1)
grad1 = theano.function([x1], gy1)
```



- **Print**

```
from IPython.display import SVG

theano.printing.pprint(x1)
SVG(theano.printing.pydotprint(z1, return_image=True, format='svg'))
```

