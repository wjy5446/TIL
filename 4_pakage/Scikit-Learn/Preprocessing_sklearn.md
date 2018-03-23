# Sklearn 전처리

## Pipeline

`from sklearn.pipeline import Pipeline`

`model = Pipeline([('name', object), ('name', object)])`

- 앞에서 부터 차례대로 진행 ('preprocessing1', 'preprocessing2', ..., 'model')



### 1. Scaling

선형변환을 이용해 자료의 분포를 동일하게 만들어 주는 과정

- overflow, underflow 방지하고 condition number를 감소시켜 최적화 과정에 안정성과 속도 향상



#### 1-1. 종류

- 함수 이용
  - `scale(X)` : 평균과 표준편차 사용 (일반적)

  - `robust_scale(X)` : median과 IQR 사용

    - 아웃라이어 영향을 최소화

  - `minmax_scale(X)` : 최대/최소값이 1, 0이 되도록 스케일링

  - `maxabs_scale(X)` : 최대절대값과 0이 1, 0이 되도록 스케일링

     

- 클래스 이용

1. `from sklearn.preprocessing import StandardScaler` : 클래스 import
2. `scaler = StandardScaler()` : 객체 생성
3. `scaler.fit(train)` : train data를 이용해 변환
   - train에 대한 mean, var를 객체에 저장한다.
4. `data = scaler.transform(test)` : test data를 이용해 변환 
   - `fit_transform()` : fit과 transform를 동시에 수행
   - 함수를 이용했을 때 서로 다른 값을 이용해 scaling 된다.



### 2. Normalization

개별 데이터의 크기를 같게 만드는 변환

- 상대적 크기가 중요할 때 사용

`from sklearn.preprocessing import normalize` : 클래스 import



### 3. Encoding

카테고리 값이나 텍스트 정보를 정수로 변환

##### 3-1. One-Hot_Encoder

0~K-1의 값을 K 차원 벡터로 변환

`from sklearn.preprocessing import OneHotEncoder`

- `ohe.fit(x)`

  - `ohe.n_values_` : 최대 클래스 수 => 숫자 인식
  - `ohe.feature_indices_` : 입력이 벡터인 경우, 원소의 slice 정보
  - `ohe.active_features_` : 실제로 사용된 클래스들

- Example

  ```
  X = np.array([[0,0,4], [1,1,0], [0,2,1], [1,0,2]])
  ```

  ```
  ohe.fit(x)
  ohe.n_values_ => [2, 3, 5]
  ohe.feature_indices_ => [0, 2, 5, 10]
  ohe.active_features_ => [0, 1, 2, 3, 4, 5, 6, 7, 9]
  ```



- `ohe.transform(X)`
  - 반환할 때, sparse matrix 객체 반환
    - `ohe.toarray()` : numpy 형태로 반환



### 4. Imputer

결측값을 채우는 변환

`from sklearn.preprocessing import Imputer`

`imp = Imputer(missing_values='NaN', strategy = 'mean', axis = 0)`

- `missing_values` : 결측값 정의
- `strategy` : 채우는 방법
  - `mean` : 평균
  - `median` : 중앙값
  - `most_frequent` : 최빈값
- `imp.fit_transform()` 



### 5. PolynomialFeatures

독립변수를 다항식으로 변환

`from sklearn.preprocessing import PolynomialFeatures`

`poly =PolynomialFeatures(degree=2, interaction_only=True) `

- `degree` : 다항식 차수
- `interaction_only` : interaction 항 생성 여부
- `include_bias` : 상수항 생성 여부



### 6. Function Transformer

사용자가 원하는 함수를 사용해 변환

`from sklearn.preprocessing import FunctionTransformer`

` FunctionTransformer(function).fit_transform(X)`

- function은 np를 입력하고 np를 출력하는 함수 제작



### 7. Binarizer

threshold 값을 기준으로 0, 1 구분

` from sklearn.preprocessing import Binarizer`

`binar = Binarizer(threshold=1.1)`

- threshold : threshold 설정



### 8. Label Binarizer

one-hot-encoder와 유사하지만 종속변수 값만 사용가능

- 역변환이 가능
- 1차원 벡터만 사용 가능
- multi-class classification 사용

`from sklearn.preprocessing import LabelBinarizer`

`lb =LabelBinarizer()`

- `lb.classes_` : 클래스 출력
- `lb.transform(y)` : 변환함수
- `lb.inverse_transform(y)` : 역변환 함수



### 9. Label Encoding

라벨을 0 ~ K-1 까지의 정수로 변환

`from sklearn.preprocessing import LabelEncoder`

`le=LabelEncoder()`

- `le.classes_` : 클래스 출력
- `le.transform(y)` : 변환함수
- `le.inverse_transform(y)` : 역변환 함수



