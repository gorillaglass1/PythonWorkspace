def find_divisor_list(n):
    # n에 대한 모든 약수 찾는 함수
    arr = list()
    for i in range(1, n + 1):
        if (n % i == 0):
            arr.append(i)
    return arr


def main():
    # 입력 받고 함수의 결과를 받아서 출력
    n = int(input("n: "))
    print(find_divisor_list(n))

if __name__ == "__main__":
    main()