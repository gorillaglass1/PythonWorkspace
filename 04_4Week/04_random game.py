from random import randint

number = randint(1, 10)
userInput = int(input("1에서 10 사이의 숫자를 입력하시오: "))

while userInput is not number:
    if userInput > number:
        print("더 작습니다.")
    else:
        print("더 큽니다.")
    
    userInput = int(input("1에서 10 사이의 숫자를 입력하시오: "))
else:
    print(f"정답입니다! {number}")

