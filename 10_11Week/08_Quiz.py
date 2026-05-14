import os

def get_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

def process_file(input_file, output_file):
    try:
        rf = open("./src/"+input_file, 'r', encoding='utf-8')
        f = open("./src/"+output_file, 'w', encoding='utf-8')
        while True:
                line = rf.readlines()
                for i in line:
                    name, grade = i.rstrip().split()
                try:
                    grade = int(grade)
                    if 0 <= grade <= 100:
                        out_grade = get_grade(grade)
                        f.write(name + ' ' + str(grade) + ' '+ out_grade + '\n')
                    else:
                        raise ValueError

                except ValueError:
                    print("점수 입력값이 잘못되었습니다.")
        rf.close()
        f.close()
    except FileNotFoundError:
        print("파일 오류")


def main():
    process_file("hw_input.txt", "hw_output.txt")

if __name__ == "__main__":
    main()