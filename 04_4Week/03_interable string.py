sentence = input("문자열을 입력하시오: ")
reverse_sentence = ''

for ch in sentence:
    reverse_sentence = ch + reverse_sentence

print(reverse_sentence)

sentence = input("문자열을 입력하시오: ")
reverse_sentence = ''

i = len(sentence) - 1 # index참조를 위해 있어야함

while i >= 0:
    reverse_sentence += sentence[i]
    i -= 1

print(reverse_sentence)