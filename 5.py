import csv


def read_file():
    proj_count = 0
    price_sum = 0
    with open('C:/Users/alumne_1r/Desktop/projects_board.csv') as csvfile:
        read_csv = csv.reader(csvfile, delimiter=',')
        next(read_csv)
        for row in read_csv:
            proj_count, price_sum = extract_data(row, proj_count, price_sum)
    print(f'\n Proyectos: {proj_count}'
          f'\n Precio total: {price_sum}')


def extract_data(row, proj_count, price_sum):
    proj_count += 1
    price_sum += int(row[4])
    return proj_count, price_sum


def main():
    read_file()


if __name__ == "__main__":
    main()
