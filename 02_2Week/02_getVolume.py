#구의 부피 계산
PI = 3.141592

# 입출력 활용
r = float(input("반지름을 입력하시오: "))

#구의 부피 계산
volume = (4.0/3.0) * PI * r ** 3

print(f"구의 부피 = {volume}")
print("구의 부피 : %.3f" % volume)