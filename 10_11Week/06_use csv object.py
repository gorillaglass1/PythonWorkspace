import csv

def main():
    weather_data = []
    header = []
    row_num = 0

    p_file = open('./src/weather.csv', 'r', encoding='utf-8')
    csv_data = csv.reader(p_file)

    for row in csv_data:
        if row_num == 0:
            header = row
        if row_num != 0:
            location = float(row[2])
            if location < 0:
                weather_data.append(row)
        row_num += 1

    p_file.close()

    s_p_file = open('./src/cold_weather_data.csv', 'w', encoding='utf-8', newline='')

    writer = csv.writer(s_p_file, delimiter=',')
    writer.writerow(header)

    for row in weather_data:
        writer.writerow(row)

    s_p_file.close()

if __name__ == "__main__":
    main()