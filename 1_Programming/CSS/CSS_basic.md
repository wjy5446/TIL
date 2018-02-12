# CSS_basic

HTML를 꾸미기 위한 코드



## CSS가 존재하는 이유

HTML : 정보에 집중

CSS : 디자인에 집중

- 코드의 분업을 위해서...




## 선택자

### 종류

- 태그 선택자 : 태그를 꾸미는 선택자

`li{color:red;}`

- 클래스 선택자 : 해당 클래스를 꾸미는 선택자

`.item{color:red;}`

- ID 선택자 : 해당 id를 꾸미는 선택자

`#id_name{color:red;}`



### 여러가지 선택자

- 부모 자식 선택자

  - 를 이용해 자식 선택자 

    `ol li{color:red}`

  - `>` 를 이용한 직계자손 선택자

    `ol>li{color:red}`

    `ol>>li{color:red}` 연속도 가능



- 여러개 선택

  `ul,ol{color:red;}`



- 선택자 옵션

  - `h1:not(.ds1){color:red;}` : ds 이외의 것선택

  - `h1:first-child{color:red;}` : 첫번째 것 선택

  - `h1:last-child{color:red;}` : 마지막 것 선택

  - `h1:nth-child(2){color:red;}` : 특정 위치 것 선택

    ​

## 문법

- color : 색깔
- text-decoration:underline : 밑줄
- border:1px solid red : 테두리
- background-color : 배경화면