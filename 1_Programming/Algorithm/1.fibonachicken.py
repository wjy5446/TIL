def is_fibo(num):
    a, b = 1, 1
    while b < num:
        a, b = b, a+b

    if num == b:
        return True, a
    else:
        return False, b

def fibo_chicken(person):
    idx = 0 # 최근 fibo에서 얼마나 떨어져 있는 지??
    val_recent = 0 # 최근 fibo 위치의 값

    ls = [] # 피보나치킨 리스트

    for i in range(1, person+1):
        tmp = is_fibo(i)
        if(tmp[0]==True):
            idx = 0
            val_recent = tmp[1]
            ls.append(tmp[1])
        else:
            ls.append(val_recent + ls[idx])
            idx += 1

    return ls

user_input = int(input("몇명이서 치킨을 먹을 것인가요?? : "))
ls = fibo_chicken(user_input)

for i in ls:
    print(i)
