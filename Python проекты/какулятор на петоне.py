a = int (input("Введите a: "))
character = (input("Знак(+. -. *, /, ^): "))
b = int (input("Введите b: "))

def solution(a, b):
    if character == "+":
        print (a + b)
    elif character == "-":
        print (a - b)
    elif character == "*":
        print (a * b)
    elif character == "/":
        print (a / b)
    elif character == "^":
        print (a ** b)
    else:
        print ("АШЫБКА НОЛЬ НОЛЬ НОЛЬ НОЛЬ НОЛЬ")
        

result = solution(a, b)

print (result)