def main():
    colors = ["red", "blue", "green", "black", "white"]
    sizes = ["small", "medium", "large"]

    combi = [(color, size) for color in colors for size in sizes]

    print(combi)

if __name__ == "__main__":
    main()