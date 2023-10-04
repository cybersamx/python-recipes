import csv
import pandas


def read_file_csv(filename: str):
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        row_count = 0
        for row in csv_reader:
            row_count += 1

            if row_count == 1:
                print(f'Columns: {", ".join(row)}')
                continue

            print()
            for cell in row:
                print(cell)

        print(f'\nRead {row_count} rows.')


def read_file_df(filename: str):
    df = pandas.read_csv(filename)

    print('\nDump of the csv file')
    print(df)

    print('\nDump of 2 cols')
    print(df[['student_name', 'grade']])


if __name__ == '__main__':
    read_file_csv('class.csv')
    read_file_df('class.csv')