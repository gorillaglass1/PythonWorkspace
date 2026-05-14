def mian():
    with open('./src/dream.txt', 'r') as f:
        content_list = f.readlines()
        print(type(content_list))
        print(content_list)

    with open('./src/dream.txt', 'r') as f:
        i = 0
        while True:
            line = f.readline()
            if not line:
                break

            print(f"{str(i)} ==== {line.replace('\n','')}")

            i += 1

if __name__ == '__main__':
    mian()