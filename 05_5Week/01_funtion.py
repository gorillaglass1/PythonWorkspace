def introduce(name, age=20, *hobbies, **info):
    print(f"이름: {name}")
    print(f"나이: {age}")

    print("취미:")
    if hobbies:
        for hobby in hobbies:
            print(f"- {hobby}")
    else:
        print("- 없음")
    
    print("추가 정보:")
    if info:
        for key, value in info.items():
            print(f"- {key}: {value}")
    else:
        print("- 없음")

introduce("이름")
print("-----")

introduce("이름", 21, "게임", "운동")
print("-----")

introduce("이름", 21, "게임", "운동", job="학생", city="춘천")