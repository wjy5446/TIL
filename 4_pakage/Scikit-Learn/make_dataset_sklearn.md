# Sklaern Make Dataset

### 1. Make_classification

```
from sklearn.datasets import make_classification
X, y = make_classification(n_samples=100, n_features=20)
```

- `n_samples` : 표본 데이터 수
- `n_features` : 독립 변수의 수
- `n_informative` : 서로 독립인 독립 변수의 수
- `n_redundant` : 변수의 선형 조합으로 나타나는 변수 의 수
- `n_repeated` : 단순 중복인 성분 수
- `n_classes` : 종속 변수의 클래스 수
- `n_clusters_per_class` : 클래스당 군집의 수
- `weights` : 클래스에 할당된 표본 수
- `random_State` : 난수 발생 시드



- 반환값 : X (독립 변수), y (종속 변수)



### 2. make_blobs

클러스터용 데이터 셋 생성

```
X, y = make_blobs(n_samples=100, n_features=2)
```

- `n_samples` : 표본 데이터의 수
- `n_feature` : 독립변수의 수
- `centers` : 생성할 클러스터의 수
- `cluster_std` : 클러스터의 표준 편차
- `center_box` : 생성할 클러스터의 바운딩 박스 

### 

- 반환 값 : X(독립변수), y(종속변수)

