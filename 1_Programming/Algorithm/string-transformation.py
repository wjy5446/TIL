# string Transformation
from collections import Counter

#문자열 이동
def move_char(char, number):
    ord_char = ord(char)
    moved_char = (ord_char - 97 +number) % 26 + 97
    return chr(moved_char)

## 내 푼 방법
def Transformation_jy(string):
    result = ""
    dict_char = {}
    count = 0

    for char in string:
        # dict 안에 있는 char 확인
        if (char not in dict_char):
            dict_char[char] = 1
        else:
            count = dict_char[char]
            dict_char[char] += 1

        tf_char = move_char(char, dict_char[char])
        result += tf_char

    return result

##==========================<해답>==============================================

## 첫번째 방법 : Collections의 Counter 이용
def Transformation_1(string):
    result = ""

    for idx, char in enumerate(string):
        print(idx, char, string[:idx])
        count = Counter(string[:idx])
        tf_char = move_char(char, count[char])
        result += tf_char
    return result

## 두번째 방법 : 문자열의 count() 이용
def Transformation_2(string):
    result = ""

    for idx,char in enumerate(string):
        count = string[:idx].count(char)
        tf_char = move_char(char, count)
        result += tf_char

    return result


## 세번째 방법 :  Conuter 함수를 한번만 사용해서 문자열 제작
def Transformation_3(string):
    result = ""
    count = Counter(string)

    for idx in range(len(string), -1, -1):
        char = string[idx]
        count[char] = count[char] - 1
        tf_char = move_char(char, count[char])
        result += tf_char

    return result[::-1]
