setting_check = 0

user_pw = input("비밀번호를 설정하세요: ")

if "" == user_pw:
    print("비밀번호가 입력되지 않았습니다.")
    print("비밀번호 설정 실패")
elif "!" not in user_pw and "@" not in user_pw and "#" not in user_pw :
    print("특수 기호를 포함하세요.")
    print("비밀번호 설정 실패")
else:
    setting_check = 1

if setting_check == 1:
    pw = input("비밀번호를 입력하세요: ")
    if pw == user_pw:
        print("로그인 성공!")
    else:
        print("비밀번호가 틀렸습니다.")