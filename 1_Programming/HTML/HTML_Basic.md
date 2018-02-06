# HTML (HyperText Markup Language)

## HTML 소개

HyperText : 링크

Markup : 마크업이라는 문법 특성

Language : 기계와 사람간 소통을 위한 약속



## HTML 구조

```
<html>
    <head>
    부가적인 내용
    </head>

    <body>
    본문 내용
    </body>
</html>
```

**DOCTYPE(Document type) : 어떤 표준에 따른 태그를 사용되는가? **



## 기본 문법

- 기본 문법태그 : <시작태그> </닫히는 태그>

- 속성 : 태그 안에 추가적인 특성을 입력할 때 사용

- `<p no=3> no3 </p>` : `=`으로 속석값 설정

  ​



## 기본 명령어

- `<head>` : 본문이 꾸며주는 


- `<title>` : 웹의 제목
- `<meta charset="utf-8">`



- `<body>` : 본문에 해당 

- `<h1>` : 제목 (h1 - h6)

- `<a>` : 하이퍼 링크

  ​

- `<li>` : 리스트

- `<ul>` : 순서가 없는 목록

- `<ol>` : 순서가 있는 목록



- `<p>` : 단락 (한줄만 표시)

- `<span>` : 단락 (한줄에 여러개 표시)

- `<pre>` : 내부 모습을 그대로 출력

  ​

- `<br>` : 줄바꿈 (void 태그)



- `<img>` : 이미지 태그

  ```
  <img src="moun.jpg" width="100" height="200" alt="산">
  ```



## 주석

`<!--code-->` : 주석을 사용



## 문자 스타일 변경

- `<b>`, `<strong>` : 굵은 글씨 출력
- `<i>`, `<em>` : 이탤릭체 출력
- `<sub>` : 아래첨자
- `<sup>` : 윗첨자
- `<small>` : 작은 글씨
- `<mark>` : 하이라이크 표시
- `<del>` : 삭제 문자열 표시
- `<ins>` : 언더라인 문자열 표시



## 코드 출력

- `<code>` : 코드 출력




## Selector

- `id(#)` : element의 고유한 값(중복이 없다.)
- `class(.)` : element를 그룹으로 묶어 주는 값
- `att([=])` : element는 속성값을 나타낸다.