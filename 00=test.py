# 전역변수 (global변수)
Value = 0

def add():
    global Value # 함수 안에서 전역으로 선언된 변수를 변경하기 위해서는 반드시 전역변수 앞에 global이라고 선언해 줘야된다.
    Value = Value + 1
    return Value

print(add())