# Pillow

이미지를 컨트롤 하기 위한 패키지



### 패키지 선언

`from PIL import Image as pil `



### 이미지 열기

`im = pil.open("image.png")`



### 속성

`im.size` : 사이즈 반환



#### 함수

`im.thumbnail((512, 512))` : 이미지 크기 변경 (많은 데이터 처리 할 때 사용)

`im.save("thum.png")` : 이미지 저장

`im.crop((left, top, right, bottom))` : 이미지 자르기

- 자를 때, 컴퓨터마다 해상도가 달라질 수 있다.