#짝수만 출력
for i in range(1, 201):
    if i % 2 == 0:
        print(i, end=" ")
print("\n")

total = 0

#3의 배수의 합
for i in range(1, 21):
    if i % 3 == 0:
        print(i, "는 3의 배수입니다.")
        total += i

print("3의 배수의 합:", total)