def calc(x, y):
    total = x + y
    print("calc 함수")
    print(f"a: {a}, b: {b}, a+b:{a+b}, total: {total}")

global a, b, total
a = 5
b = 7
total = 0

print("calc 함수 이전")
print(f"a: {a}, b: {b}, a+b: {a+b}, total: {total}")

sum = calc(a, b)

print("calc 함수 이후")
print(f"a: {a}, b: {b}, a+b: {a+b}, total: {total}, sum = {sum}")