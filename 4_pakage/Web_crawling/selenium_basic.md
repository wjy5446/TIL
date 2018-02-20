# selenium

테스트 자동화를 위해 사용되는 패키지

### 패키지 선언

`from selenium import webdriver`



### browser 열기

`driver = webdriver.Chrome()`

- driver는 브라우저 전체 객체




### 동작

#### url 이동

`driver.get("http://www.naver.com")`



#### 탭 객체

`main_win = driver.current_window_handle` : 열려있는 탭 객체ID 저장

`wins = driver.window_handles` : 리스트 형태로 객체 저장



`driver.switch_to_window(main_win)` : 탭 포커스 변경



#### Javascript 사용

`driver.execute_script("jave_code")` 



##### 응용

`diver.execute_script("window.scrollTo(200, 300);")` : 스크롤 변경

`diver.execute_script("window.open("http://www.google.com");")` : 새창 열기

`diver.execute_script("location.reload();")` : 새로 고침

- javascript이기 때문에 마지막에 ;를 넣어준다.



#### Set window size

`driver.set_window_size(800, 600)`



####Css selector

`driver.find_element_by_css_selector(".ico").click()` : 선택된 위치 클릭하기



### Alert와 Confirm 다루기

#### Alert & Conform

`driver.execute_script("alert('selenium test');")` : 확인 버튼만 존재

`driver.execute_script("corfirm('selenium test');")` : 확인 과 취소 버튼이 같이 존재



#### focusing alert

`alert = driver.switch_to_alert()`



#### alert 동작

`alert.text` : 텍스트 가져오기

`alert.accept()` : 확인 버튼 

`alert.dismiss()` : 취소 버튼



 

