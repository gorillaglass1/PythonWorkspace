print("아무 숫자나 입력하시오.")
print("(-1: 종료, -2: 숫자 변경)")
num_list = []

while True:
    userInput = int(input("숫자를 입력하시오: "))
    if userInput == -1:
        break
    if userInput == -2:
        if not num_list:
            print("비어 있습니다.")
            continue
        

        print("변경할 index와 수를 입력하세오: ")
        index_num = int(input())
        change_num = int(input())

        num_list[index_num] = change_num
        continue

    num_list.append(userInput)

        
    

    

print(f"최종 리스트: {num_list}")