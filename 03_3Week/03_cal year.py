year = int(input("윤년을 확인할 연도를 입력하세요: "))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(f"{year}는 윤년입니다.")
else:
    print(f"{year}는 평년입니다.")