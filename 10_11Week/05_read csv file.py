def main():
    line_counter = 0
    data_header = []
    country_list = []

    with open('./src/countries.csv') as country_data:
        while True:
            data = country_data.readline()
            if not data:
                break
            if line_counter == 0:
                data_header = data.split(',')
            else:
                country_list.append(data.split(','))
            line_counter += 1

    print(f"Header: {data_header}")

    for i in range(0, 5):
        print(f"Data[{i}]: {country_list[i]}")

    print(len(country_list))

if __name__ == "__main__":
    main()