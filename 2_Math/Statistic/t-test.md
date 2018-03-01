# t-test

### t-value

$$
t=\dfrac{\bar{x}-\mu_0}{s/\sqrt{n}}
$$

**signal-to-noise ratio**

- signal(분자) : 모집단 평균과 샘플 평균의 차이
  - 차이 클수록 signal이 강해진다.
  - signal 을 effect size라고 불리기도 한다.

  ​
- Noise(분모) : 평균의 분산정도(에러)
  - $\sqrt{n}$ 를 나누는 이유는 평균의 분산을 단일화하기 위해

  - 데이터가 작을 수록 에러가 더 크기 때문에

  - SE(Standard Error) 

  - $$
    Var[\bar{X}] = Var[\dfrac{1}{n}\Sigma x_i] =\dfrac{1}{\sqrt{n}}Var[X]
    $$

- t-value는 평균과 샘플 평균 차이가 Noise 배수 만큽 차이가 난다는 의미 (정확히 차이가 얼마나 나는 지 확인하기 위해 사용)



### Paired t-test = 1-Sample t-Test

- 1-sample t-Test : 하나의 샘플 mean를 비교를 귀무가설로 사용
- paired t-test는 paired data의 차이를 구하고 이를 t-test로 구한다.  (차이가 없다면 $\mu=0$인 정규 분포를 띈다.)



### Two-Sample T-test

$$
t=\dfrac{\bar{X_1}-\bar{X_2}}{s}
$$

- $H_0$ 은 두 그룹의 평균이 같다.
- 두 샘플의 분산이 같다는 가정

