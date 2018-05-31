# Gaussian Mixture Model

## Mixture Model ?

- 모수를 여러 개 가지고 있는 분포로 데이터가 생성된 모델


- Unsupervised Learning의 모수적 접근법

- 대표적은 Mixture Model : GMM (multi-modal)

   

## Binomial Gaussian Mixture Model

- 여러개의 가우시안 모델로 이루어진 모델 (multi-model gaussian model)


$$
p(X) = \sum_Z p(Z)p(X|Z) = \sum_{k=1}^{K} \theta_k N(X|\mu_k, \Sigma_k)
$$

- $p(X)$ : 전체 분포
- $p(X|Z)$ : Mixture의 성분이 되는 개별 연속 확률 분포
- $P(Z)$ : 개별 카테고리가 선택될 확률
- $\theta_k$ : 카테고리 확률 분포의 모수가 선택될 확률



## Parameter estimator

- 정규 분포의 모수 : $\mu_i, \sigma_i$
- 카테고리 확률 분포의 모수 : $\theta_k$



## 가우시안 혼합 모델 학습

### 1) MLE

**log likelihood**
$$
\prod_{i=1}^N P(X_i) = \prod_{i=1}^N \sum_{Z_i} p(Z_i)p(X_i|Z_i)  = \prod_{i=1}^N \sum_{k=1}^{K} \theta_k N(X_i|\mu_k, \Sigma_k) \\
LL = \sum_{i=1}^N \log \left( \sum_{k=1}^{K} \theta_k N(X_i|\mu_k, \Sigma_k) \right)
$$

-  만약 데이터 $x_i$가 원하는 카테고리 값 $z_i$에 속하는 지 알수 있다면 쉽게 계산이 가능
- 하지만, 실제 데이터가 어느 카테고리에 속하는 지 알 수 없다.
- latent variable model : 관측데이터가 보이지 않는 확률 모형
- latent variable : 카테고리값



**reponsibility**

각 데이터가 어떤 카테고리에 속하는 지 알려주는 확률
$$
\gamma(z_{ik}) = p(z_i=k|x_i) = \dfrac{p(z_i=k)p(x_i|z_i=k)}{\sum_{k=1}^K p(z_i=k)p(x_i|z_i=k)}= \dfrac{\theta_k N(X_i|\mu_k, \Sigma_k)}{\sum_{k=1}^K \theta_k N(X_i|\mu_k, \Sigma_k)}
$$


- reponsibility를 알고 있을 때,
  - $\mu$ : 카테고리에 속하는 데이터의 평균
  - $\sigma$ : 카테고리에 속하는 데이터의 분산
  - $\theta$ : 카테고리 데이터 값 / 전체 데이터 값 



### 2) EM(Expectation-Maximization)

모수와 reponsibility를 번갈아 추정하며 정확도를 높여가는 방법

1. E step : 우리가 알고 있는 모수가 정확하다 가정하고, responsibility 추정
2. M step : responsibility가 정확하다 가정하고 모수 추정

-> 위 방법을 반복하여 모수와 reponsibility 점진적으로 개선



## Clustering

- GMM의 pdf를 이용해 N_1에서 관측될 확률, N_2에서 관측될 확률, N_3에서 관측될 확률을 비교



