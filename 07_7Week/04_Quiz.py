# my_upper(*args) 구현하기
def my_upper(*args):
    ls = list()
    for i in args:
        if type(i) != str:
            ls.append(i)
        else:
            temp = ""
            for j in i:
                if 96 < ord(j) < 123 and j.isalpha():
                    temp += chr(ord(j) - 32)
                else:
                    temp += j
            ls.append(temp)
    return ls
        


def main():
    print(my_upper('These are examples of my_upper()'))
    print(my_upper('my_upper() takese "args of strings and return a list of them that turn into upper case'))
    print(my_upper('aaa', 'Bb', 'CCccC', [1, 2, 3]))

if __name__ == "__main__":
    main()