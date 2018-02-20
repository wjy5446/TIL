# selenium file

### change iframe

`ifrmae = driver.find_element_by_css_selector("#id")`

`driver.switch_to_frame(iframe)` : 포커스 이동

`driver.switch_to_default_content()` : 포커스 파져 나오기



### file Input

file path input에 주소를 입력하여 얻는다. 

`driver.find_element_by_css_selector("#id").sendkey(filepath)` : input에 값 입력

`driver.find_element_by_css_selector(.class)[0].text` : 텍스트 가져오기

`driver.find_element_by_css_selector(.class).get_attribute("href" or "src") ` : URL 가져오기



##### 기타

`driver.find_element_by_css_selector().size` : 크기 반환

`driver.find_element_by_css_selector().location` : 위치 반환



### 스크린샷 찍기

`driver.save_screenshot("screen.png")` : 브라우저 화면 저장



### 시간이 걸리는 작업 처리

##### 1. time.sleep() 이용

`time.sleep(10)` : 고정된 시간 동안 정지

- 이방법을 사용시 간단하게 작성할 수 있지만, 유지 보수가 힘들다.





##### 2. element 체크 함수 이용

```
def check_element(driver, selector):
	try:
		driver.find_element_by_css_selector(selctor)
		return True
	except:
		return False
```

- 에러가 날 확률이 적어져, 유지 보수가 간단해 진다.

