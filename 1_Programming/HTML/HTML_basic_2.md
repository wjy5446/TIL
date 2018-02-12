# HTML_2

## 레이아웃

- `<div>` : 레이아웃을 나누기
  - 주로 많이 사용된다. 
  - 레이아웃 선택자 종류
    - `<div id = "">` : id
    - `<div class = "">` : class

## 테이블

- `<table>` : 테이블 시작
- `<tr>` : 열행
- `<td>` : 데이터



- `<thead>` : 데이터 머리(index)
- `<tbody>` : 실제 데이터가 있는 곳
- `<tfoot>` : 항상 밑으로 하는 곳

#### 사용 예시

```
<table>
	<thead>
		<tr>
			<td> </td>
			<td> </td>
			<td> </td>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td> </td>
			<td> </td>
			<td> </td>
		</tr>
	</tbody>
</table>
```



## 리스트

- `<ul>` : 순서가 없는 리스트
- `<ol>` : 순서가 있는 리스트
- `<li> ` : 리스트 값



## 하이퍼 링크

- `<a href="http://google.com" target="_blank">Google</a>`
  - _blank : 새창열기



## 이미지

- `<img src="url address" alt="NoImage" witdh = "100" height = "100">`
  - src : url주소
  - alt : 그림을 대신할 글짜 웹 접근성을 확대
  - width, height : 그림의 넓이와 높이



## 아이프래임

- `<iframe src = "" width="100" height="200">`
  - src : 웹페이지 주소
  - width, height : 아이프래임의 넓이와 높이