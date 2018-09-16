# Scala 정리

## 기본 스칼라 형태

```
object LearnScala{
    def main(args:Array[String]): Unit = {
        println("Hello, world!")
    }
}
```



## 연산자

```
println(1 + 2)
println((1). + (2))
```

- literal을 **객체(Object)** 로 취급
- Operator notation, infix



## 변수와 상수

- `var` : 변수
- `val` : 상수



## 출력

- `println`
  - `println("$x is bigger than $y")` :  `$`을 이용해 변수이름으로 바로 변수 출력 가능
  - `println("${x + y}")` : `${}`으로 수식 입력이 가능
  - `printf()` : `%f`로 숫자 표기가 가능



## Range와 List

- `Range` 
  - `range = 1 to 10` : 1에서 10 생성
  - `range = 1 until 10` : 마지막 포함하지 않는 range 출력
  - `range = 1 until 10 by 3` : 3을 건너 뛰는 range 출력
  - `range.toList` : List로 range 변환
  - `range.filter(_ > 4)` : 조건에 맞는 데이터 출력
  - `range.map(_ *2)` : 각 아이템의 값 변경



## 숫자용 메소드

- `num.abs` : 절대값
- `num1.max(num2)` : num1과 num2의 최대값
- `num1.min(num2)` : num1과 num2의 최소값 



## 문자용 메소드

- `string.reverse` :  뒤집기
- `string.capitalize` : 첫글자 대문자
- `string * 7` : 7번 반복
- `string.toInt` : 정수로 변환



## 메소드

- 여러 방식의 메소드 호출

```
# 공식
def add(x:Int, y:Int):Int = {
    return x + y
}
```

```
# 매개변수가 함수일때
def fun1(f:(Int, Int)=>Int)={
    f(1,2)
}
```

```
# return을 생략한 메소드 (자동으로 자료형 설정)
def add(x:Int, y:Int) = {x + y}
```

- 익명함수

```
# 명시적으로 타입 선언
(x:Int, y:Int) => x + y
```

```
# 타입 선언 생략
(x, y) => x + y
```

```
# 완전히 생략
_ + _
```

- 한줄로 메소드 정의

```
val add1(x:Int, y:Int) = x + y
```

```
val add2 = (x:Int, y:Int)=> x + y
```

```
val add3:(Int,Int) => Int = _+_
```

```
val add4 = (_ + _):(Int, Int) => Int
```



## 반복문

- while
  - `++`, `--` 제공하지 않음

```
while (i<10){
    sum += 1
    i += 1
}
```



- for

```
for ( i <- 0 until 10){
    sum += 1
}
```

```
# 중첩된 반복문
for(a <- 1 to 3; b <- 10 to 12){
    println(a, b)
}
```



## 조건문

- if
  - 생략이 가능

```
if(조건){
    조건 만족
}
else {
    조건 불만족
}
```





## Collection

- 튜플 : 여러 타입의 객체를 담을 수 있는 곳
  - 선언 : `val t1 = new Tuple3()` : 3개 객체를 담는 곳
    - `()`을 이용해 선언
  - 메소드 
    - `._1` : 튜플 값에 접근
  - 튜플로 이용해 여러 값 리턴