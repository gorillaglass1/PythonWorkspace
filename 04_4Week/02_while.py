userInput = int(input("아무 숫자나 입력하시오: "))
sum = 0

while userInput >= 0:
    if userInput <= 5:
        break
    sum += userInput
    userInput -= 1

print(f"{userInput + 1}에서 입력 번호까지의 합: {sum}")