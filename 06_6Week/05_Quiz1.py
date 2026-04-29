import random

def find_patten(data):
    max = -1
    cnt = 0
    for i in range(len(data)):
        if i == 0:
            cnt += 1
        elif data[i] >= data[i-1]:
            cnt += 1
        else:
            if cnt > max:
                max = cnt
            cnt = 1
    
    if max > cnt:
        return max
    else:
        return cnt


def main():
    for _ in range(5):
        data = [random.randint(0, 9) for _ in range(0, random.randint(5, 15))]
        print(f"리스트 {data}의 연속된 증가 구간의 길이는 = {find_patten(data)}")

if __name__ == "__main__":
    main()