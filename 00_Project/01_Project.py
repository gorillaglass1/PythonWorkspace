import re
from datetime import datetime

def get_hashed_password(password):
    hash_value = 0xABCDEF

    for i, char in enumerate(password):
        ascii_code = ord(char)

        hash_value ^= (ascii_code << (i % 8))
        hash_value += ascii_code * (i + 1) + len(password)
        hash_value %= 0xFFFFFFFF
        hash_value ^= (hash_value >> 7)

    return format(hash_value % (16 ** 16), "016x")

def get_satisfied_password(password):
    password = password.strip()

    if len(password) < 10:
        return False

    has_number = re.search(r"[0-9]", password)
    has_upper = re.search(r"[A-Z]", password)
    has_lower = re.search(r"[a-z]", password)
    has_special = re.search(r"[^A-Za-z0-9]", password)

    return bool(has_number and has_upper and has_lower and has_special)


def signup(user_id, password):
    try:
        f = open("./src/user_list.txt", "r", encoding="utf-8")
        user_list = f.readlines().strip().split(",")
        if user_id in user_list | user_id == '':
            print("유효하지 않은 아이디입니다.")
    except Exception as e:
        print(e)

    while True:
        try:
            if get_satisfied_password(password):
                break
            else:
                raise ValueError
        except ValueError:
            print("비밀번호는 10자 이상이며, 숫자, 대문자, 소문자 특수기호를 모두 포함해야 합니다.")

    hashed_password = get_hashed_password(password)
    sign_up_write_to_file(user_id, hashed_password)
    f.close()

def sign_up_write_to_file(user_id, hashed_password):
    with open("./src/user_list.txt", "a", encoding="utf-8") as fe:
        fe.write(user_id + "," + hashed_password + "\n")
    print("회원가입이 완료되었습니다.")
    print("저장된 비밀번호 해시값: " + str(hashed_password))


def login(user_id, password):
    key_password = None
    if not user_id in user_list | user_id == '':
        print("유효하지 않은 아이디입니다.")
    try:
        user_list = {}
        f = open("./src/user_list.txt", "r", encoding="utf-8")
        while True:
            temp_id, temp_password = f.readline().strip().split(",")
            if temp_id == user_id:
                key_password = temp_password
                break
            if not temp_id:
                raise ValueError
    except Exception as e:
        print(e)

    if key_password == get_hashed_password(password):
        print("로그인 성공")
    else:
        print("로그인 실패")

def write_log(message):
    try:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open("./src/log.txt", "a", encoding="utf-8") as f:
            f.write(f"[{now}] {message}\n")

    except Exception as e:
        print("로그 저장 중 오류 발생:", e)

def main():
    while True:
        try:
            print("==== 로그인 프로그램 ====")
            print("1. 회원가입")
            print("2. 로그인")
            print("3. 종료")
            req = input("메뉴 선택: ")

            if not (1 <= req <= 3):
                raise ValueError
        except KeyboardInterrupt or ValueError:
            print("유효하지 않은 입력합니다.")
        except Exception as e:
            print(e)

        if req == 1:
            user_id, password = input().split()
            signup(user_id, password)
        elif req == 2:
            login()
        elif req == 3:
            return


if __name__ == '__main__':
    main()

