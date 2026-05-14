def main():
    with open('./src/count_log.txt', 'a', encoding='utf-8') as f:
        for i in range(11, 21):
            f.write(f'{i}번째 줄 \n')

if __name__ == '__main__':
    main()
