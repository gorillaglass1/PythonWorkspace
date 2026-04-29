def main():
    input_str = input("문자열을 입력하시오 ")

    split_str = input_str.split(" ")

    for s in split_str:
        change_str = ""
        for c in s:
            if not c.isalpha():
                change_str += c
            elif 96 < ord(c) < 123:
                change_str += chr(ord(c) - 32)
            else:
                change_str += chr(ord(c) + 32)
        
        print(change_str)

if __name__ == "__main__":
    main()

