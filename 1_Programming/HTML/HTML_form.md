# HTML FORM

- form : 사용자가 입력한 정보를 서버로 전송



## 다양한 form

### text (텍스트 입력창)

`<input type="text" name="" value="" placeholder="이메일">`

- name : form의 id
- value : 입력 값
- placeholder : 빈칸에 입력되는 값



###  password(패쓰워드 입력창)

`<input type="password" name="" value="" placeholder="pwd">`



### radio button

`<input type="radio" name="radio_1" value="b1">버튼</input>`

`<input type="radio" name="radio_1" value="b2">버튼</input>`

- name : 같은 라디오 버튼을 묶어준다.



### checkbox

`<input type="checkbox" name="" value="c1">체크박스1</input>`



### Text area(여러 줄을 입력받을 수 있는 공간)

`<textarea name="ta" rows="5" cols="50" style="resize: none"></textarea>`



### Select

```
<select>
	<option value="1">option 1</option>
	<option value="2">option 2</option>
	<option value="3">option 3</option>
</select>
```



### Button

`<botton type="button" onlick="javasript:(alert('Hello'))">Click</button>`



### Entities

특수문자를 나타내기 위한 문자

- `&lt;` : <
- `&gt;` : >

