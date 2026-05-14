def xor_encrypt(text, key):
    result = []

    for ch in text:
        encrypted = ord(ch) ^ key
        result.append(encrypted)

    return result

def xor_decrypt(encrypted_list, key):
    result = ""

    for num in encrypted_list:
        decrypted = num ^ key
        result += chr(decrypted)

    return result

if __name__ == "__main__":
    key = 7

    try:
        with open('./src/typing_1_input.txt', 'r', encoding='utf-8') as input_file:
            text = input_file.read()

        encrypted = xor_encrypt(text, key)
        decrypted = xor_decrypt(encrypted, key)

        with open('./src/typing_1_output.txt', 'w', encoding='utf-8') as output_file:
            output_file.write("원문:\n")
            output_file.write(text)
            output_file.write('\n\n')

            output_file.write("암호문:\n")
            output_file.write(str(encrypted))
            output_file.write('\n\n')

            output_file.write("복호문:\n")
            output_file.write(decrypted)

        print("처리 완")
        print("저장 완")

    except FileNotFoundError:
        print("파일 없음")
    except Exception as e:
        print(e)