# Scikit-Learn 샘플 데이터 가져오기

### 종류

- load : 저장된 dataset
- fetch : 인터넷에서 캐쉬로 다운로드해 구한 dataset
- make : 가상 dataset 생성



### Load data

적은 용량 데이터를 사용할 때 사용.

`from sklearn.datasets import load_boston`



### Fetch data

데이터가 너무 커서 인터넷에서 다운로드 받아 scikit_learn_data 서브 디렉토리에 저장해서 사용

`from sklearn.datasets import fetch_covtype()`



### Make data

모형을 시험하기 위한 가상 데이터 생성

`from sklearn.datasets imort make_regression()`



### 데이터 세트의 형식

`Bunch` 라는 클래스 객체로 생성

##### Bunch의 속성

- `data` : 독립 변수(ndarray)
- `target` : 종속 변수(ndarray)



- `feature_names` : 독립 변수 리스트
- `target_names` : 종속 변수 리스트
- `DESCR` : 자료에 대한 설명