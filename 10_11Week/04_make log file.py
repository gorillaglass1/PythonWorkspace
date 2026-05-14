import os

def main():
    if not os.path.isdir('log'):
        os.mkdir('log')

    if not os.path.exists('./log/count_log.txt'):
        f = open('./log/count_log.txt', 'w', encoding='utf-8')
        f.write('기록이 시작됩니다.\n')
        f.close()

    with open('./log/count_log.txt', 'a', encoding='utf-8') as f:
        import random, datetime

        for i in range(1, 11):
            stamp = str(datetime.datetime.now())
            value = random.random()*1000000
            log_time = stamp + '\t' + str(value) + '값이 생성되었습니다. \n'
            f.write(log_time)

if __name__ == '__main__':
    main()