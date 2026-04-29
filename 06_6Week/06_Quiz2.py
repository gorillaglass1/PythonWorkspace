import random

def print_list(lst):
    for j in range(len(lst)):
        for i in range(len(lst[j])):
            print(lst[j][i], end=' ')
        print()

def main():
    # 리스트 컴프리헨션으로 작성하기
    #반복문으로 구현 가능 단, 점수 감점 있음
    row = int(input("행(row) 입력: "))
    col = int(input("열(col) 입력: "))
    lst = [[random.randint(0, 9) for _ in range(row)] for _ in range(col)]

    print_list(lst)

if __name__ == "__main__":
    main()