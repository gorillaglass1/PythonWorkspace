def fibo_iter(n):
    a = 0
    b = 1
    if n <= 1:
        return n
    else:
        for i in range(2, n+1):
            c = a + b
            a = b
            b = c
    return b

def fibo_recursive(n):
    if n <= 1:
        return n
    return fibo_recursive(n-1) + fibo_recursive(n-2)

def main():
    n = int(input("n: "))
    if (n < 0):
        print("잘못된 입력")
        return
    print(f"반목문 구현 결과: {fibo_iter(n)}")
    print(f"재귀문 구현 결과: {fibo_recursive(n)}")

if __name__ == "__main__":
    main()