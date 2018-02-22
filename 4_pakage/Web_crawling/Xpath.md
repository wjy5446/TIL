# Xpath

**XML Path Language**

xpath를 이용해 특정 selector 객체를 가져옴



### 문법

> //*[@id="PM_ID_ct"]/div[1]/div[2]/div[2]/div[1]/div/ul/li[17]/a/span[2]



- `//` : 가장 상위 Element
- `.` : 현재 Element



- `*` : 조건에 맞는 하위 Element 확인(= `띄어쓰기`)
- `/` : 바로 아래 level Element 확인 (= `>` )
- `@` : 속성값



- 조건 []
  - p[2] : p element의 두번째 element (1부터 시작)
  - p[@(attribute key) = "(attribute value)"]
  - p[@id="email"] : 아이디 값 
  - p[@class="pw"] : 클래스 값



- not(조건) : 조건이 아닌 요소 찾음




- `/text()` : 텍스트 값 가져오기