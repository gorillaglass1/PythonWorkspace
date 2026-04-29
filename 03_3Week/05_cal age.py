birthYear = int(input("태어난 연도를 입력하세오: "))

age = 2026 - birthYear + 1

if age >= 20 and age < 26:
    print("대학생입니다.")
elif age >= 17 and age < 20:
    print("고등학생입니다.")
elif 14 <= age < 17:
    print("중학생입니다.")
elif 8 <= age < 14:
    print("초등학생입니다.")
else:
    print("학생이 아닙니다.")


