def factorial(n):
    if n == 1:
        print(f"{n}")
        return 1
    elif n > 1:
        print(f"{n} * ", end=" ")
        return n * factorial(n-1)
    else:
        print("Error occur")

num = int(input("숫자를 입력하시오: "))
result = factorial(num)
print(f"result: {result}")