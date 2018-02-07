# Javascript Array

## 배열 

### 선언

```
var arr = ['a', 'b', 'c', 'd', 'e'];
```



### 크기 

```
arr.Length
```



### Indexing

```
arr[2]
```



### 추가 및 제거

- 추가

  `arr.push('f')` : 뒤에 추가

  `arr.unshift('z')` : 앞에 추가


- 삭제

  `arr.shift()` : 첫번째 원소 제거

  `arr.pop()` : 마지막 원소 제거



​	`arr.splice(2, 1)` : 2번에서 1개 자름

​	`delete arr[2]` : 2번 삭제(빈공간 남아 있음)



### 정렬

- `arr.reverse()` : 역순으로 정렬
- `arr.sort()` : 오름 차순 정렬
- `arr.sort().reverse()` : 내림 차순 정렬



