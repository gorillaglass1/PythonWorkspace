def main():
    matrix = [[i for i in range(5)] for _ in range(6)]
    print(matrix)

    matrix2 = [[i * 5 + j for j in range(5)] for i in range(3)]
    print(matrix2)

if __name__ == "__main__":
    main()