import random

def generate_number():
    answer_numbers = []
    while len(answer_numbers) < 3:
        num = random.randint(0, 9)
        if num not in answer_numbers:
            answer_numbers.append(num)
    return answer_numbers

def check(guess_numbers, answer_numbers):
    strike = 0
    ball = 0
    for i in range(3):
        if guess_numbers[i] == answer_numbers[i]:
            strike += 1
        elif guess_numbers[i] in answer_numbers:
            ball += 1
    return strike, ball


def input_guess_number():
    guess_numbers = []
    for i in range(3):
        guess_numbers.append(int(input(f"{i+1}번째 숫자를 입력하시오: ")))
    return guess_numbers

def main():
    answer_numbers = generate_number()
    while True:
        guess_numbers = input_guess_number()
        strike, ball = check(guess_numbers, answer_numbers)
        if strike == 3:
            print(f"정답입니다.! 정답 숫자: {answer_numbers}")
            break
        else:
            print(f"오답입니다. (힌트: {strike} strike, {ball} ball)")

if __name__ == "__main__":
    main()