def main():
    s = input("문자열을 입력하시오: ")

    count_letters = 0
    count_digits = 0

    for i in s:
        if i.isalpha():
            count_letters += 1
        elif i.isdigit():
            count_digits += 1
        
    dic = {"LETTERS": count_letters, "DIGITS": count_digits}
    print(dic)

if __name__ == "__main__":
    main()
    