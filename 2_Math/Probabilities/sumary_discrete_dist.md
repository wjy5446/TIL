# 이산 확률 분포

- 이산 확률 분포는 모두 PMF(Probability mass function)으로 표현된다.



|                |              Bernoulli dist              |              Binomial dist               |             Categrical dist              |             multinomial dist             |
| :------------: | :--------------------------------------: | :--------------------------------------: | :--------------------------------------: | :--------------------------------------: |
| representation | $Bern(x;\theta) = \begin{cases} \theta & \text{if }x=1 \\ 1-\theta & \text{if }x=0 \\ \end{cases}$ | $\text{Bin}(x;N,\theta) = \binom N x  \theta^x(1-\theta)^{N-x}$ | $ \text{Cat}(x;\theta) = \theta_1^{x_1} \theta_2^{x_2}  \cdots \theta_K^{x_K}  =  \prod_{k=1}^K \theta_k^{x_k}$ | $\text{Mu}(x;N,\theta) = \binom N {x_1, \cdots, x_K} \prod_{k=1}^K \theta_k^{x_k}$ |
|     input      |                  0 or 1                  |           0, 1, 2, $\dots$ , N           | $x_i=\begin{cases} 0 \\ 1\end{cases}, \Sigma^k_{k=1}x_k=1$ 인 벡터 x |                   벡터 x                   |
|   patameter    |                 $\theta$                 |             시행횟수 N, $\theta$             |           각 벡터에 할당된 $\theta_k$           |       시행횟수 N, 각 벡터에 할당된 $\theta_k$       |
|  Expectation   |            $E[Bern] = \theta$            |            $E[Bin] = N\theta$            |            $E[x_k]=\theta_k$             |            $E[x_k]=N\theta_k$            |
|   Variation    |      $Var[Bern] = \theta(1-\theta)$      |       $Var[Bin]=N\theta(1-\theta)$       |     $Var[x_k]=\theta_k(1-\theta_k)$      |     $Var[x_k]=N\theta_k(1-\theta_k)$     |
|                |           동전을 1번 던져서 앞면이 나올 확률           |           동전을 N번 던져서 앞면이 나올 확률           |           주사위를 1번 던져서 1이 나올 확률           |           주사위를 N번 던져서 1이 나올 확률           |

