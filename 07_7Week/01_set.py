def main():
    s1 = input("첫 번재 문자열을 입력하세요: ")
    s2 = input("두 번째 문자열을 입력하세요: ")

    set1 = set(s1)
    set2 = set(s2)

    set3 = set1.intersection(set2) # set1&set2
    print(f"모두 포함된 글자: {set3}")

    for index, element in enumerate(set3):
        print(index, element)

if __name__ == "__main__":
    main()