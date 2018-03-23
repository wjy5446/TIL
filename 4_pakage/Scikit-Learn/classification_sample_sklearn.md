# Sklearn 이용한 Classification Sample Data

### 1-1. Iris

```
from sklearn.datasets import load_iris
iris = load_iris()
```

- Target : setosa, versicolor, virginica 꽃 종류
- Feature : Sepal Length, Sepal Width, Petal Length, Petal Width



### 1-2. 뉴스 그룹 텍스트

```
from sklearn.datasets import fetch_20newsgroups
newsgroup = fetch_20newsgroups(subset = 'all')
```

- Target : 문서가 속한 뉴스 그룹
- Feature : 문서 데이터



### 1-3. 올리베티 얼굴 사진

```
from sklearn.datasets import fetch_olivetti_faces
olivetti = fetch_olivetti_faces()
```

- Target : 40명의 개인을 나타내는 식별 번호
- Feature : 64x64 개인 얼굴



### 1-4. Labeled Faces in the Wild (LFW)

```
from sklearn.datasets import fetch_lfw_people
lfw_people = fetch_lfw_people(min_faces_per_person=70, resize=0.4)
```

- `funneled` : 이미지의 위치 조정 여부
- `resize` : 이미지 크기 조절
- `min_faces_per_person` : 각 인물당 최소 사진 수
- `color` : 컬러 여부



#### pair

```
lfw_pairs = fetch_lfw_pairs(resize = 0.4)
```

한쌍의 이미지 데이터를 로드해서 데이터가 동일한지 확인한다.



### 1-5. Digits

```
from sklearn.datasets import load_digits
digits = load_digits()
```

- Feature : 0~25의 8x8 흑백 이미지



#### mldata.org

http://mldata.org 에서 데이터를 다운로드 받아서 사용.

```
from sklearn.datasets.mldata import fetch_mldata
mnist = fetch_mldata('MNIST ')
```

