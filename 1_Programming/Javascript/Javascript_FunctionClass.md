# Javascript Function and Class

## Function

### 함수 선언

```
function add(a, b){
  return a + b;
}
```

- 변수를 받아서 함수 사용 가능

```
var func = function(a, b){return a + b;};
func(1, 5)
```

- 이 때 데이터 타입은 `function` 



### scope

- 전역 변수 : 전역, 함수에서 모두 사용 가능
- 지역 변수 : 함수에서만 사용 가능



- 전역 변수는 계속 메모리를 차지하기 때문에 되도록이면 전역 변수를 사용하지 않는다.



### 익명함수

```
(function(n){
  var a = "hello";
  console.log(a);
  return a;
}(5))
```

- 전역 변수를 사용하지 않기 위해 익명함수 사용




### CallBack 함수

함수내에서 모든 동작이 끝나고 실행시키는 함수 (입력으로 함수를 받음)

```
function add(a, b, callback){
  var result = a + b;
  callback(result);
}
```

```
add(5, 8, disp)
```



## Object

Javascript에서 클래스를 구현하기 위해 사용 (dictionay 형태)



### 객체 생성

```
var obj = {};
obj.math = 92;
obj.english = 97;
obj.science - 85;

* obj["math"] = 92; 도 가능 But, 문법에 어긋남
```



### 객체 출력

```
obj.math
obj["math"]

* 객체 요소 하나하나 출력
for(var key in obj){
  console.log(key, obj[key]);
}
```



### 객체에 함수 및 변수 선언

#### 변수 선언

- value에 `dictionary`를 담아서 선언

```
var pointsObj = {
  'points' : {'math':91, 'science':98}
}
```



#### 함수 선언

- value에 `함수`를 담아서 선언

```
var pointsObj = {
  'total' : function(){
    var total = 0;
    for(var key in this.points){
      total += this.points[key];
    }
    return total;
  }
}
```

#### 함수 출력 

```
pointsObj.tatal()
```

