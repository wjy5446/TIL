# Scipy를 이용한 확률 분포 

### scipy.stats

Scipy에서 확률 분포 분석을 하기 위한 서브 패키지



### 확률 분포 생성

##### 이산

- `bernoulli(p=theta)` : 베르누이 분포 
- `binom(n = N, p = theta)` : 이항 분포
- `multinomial(n = N, p = [0.2, 0.3, 0.5])` : 다항 분포



##### 연속

- `uniform` : 균일 분포

- `norm(loc = 0, scale = 1)` : 정규 분포

- `beta` : 베타 분포

- `gamma` : 감마 분포

- `t` : 스튜던드 t 분포

- `chi2` : 카이 제곱 분포

- `f` : F 분포

- `dirichlet` : 디리클리 분포

- `multivariate_normal` : 다변수 정규 분포

   

### 확률 분포 메서드

- `pdf(x)` : 확률 밀도 함수
- `pmf(x)` : 확률 질량 함수
- `cdf(x)` : 누적 분포 함수



### 랜덤 샘플 생성

- `rvs(size = (3,5), random_state = 0)` : 랜덤 샘플 생성 



### * Q-Q plot

- `sp.stats.probplot(x, plot = plt)` : Q-Q plot