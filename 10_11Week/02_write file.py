def main():
    f = open('./src/count_log.txt', 'w', encoding='utf-8')

    for i in range(1, 11):
        txt = f'{i}번째 줄\n'
        f.write(txt)

    f.close()

if __name__ == '__main__':
    main()