a=float(input())
b=float(input())
operator=input()
match operator:
    case "+":
        print(a+b)
    case "-":
        print(a-b)
    case "*":
        print(a*b)
    case "/":
        if b != 0:
            print(a/b)
        else:
            print("помилка")
    case _:
        print("невідомий оператор")
