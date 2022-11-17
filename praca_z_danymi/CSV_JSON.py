import csv
import sys


class CsvManager:

    def __init__(self, file_path):
        self.file_path = file_path

    def handle_csv(self):
        with open(self.file_path, 'r') as csv_file:  # 'r' is read file
            csv_reader = csv.reader(csv_file)
            header_rows = next(csv_reader)

            for line in csv_reader:
                print(line)


if __name__ == '__main__':
    file_path = "files/example_csv.csv"
    csv_file_handler = CsvManager(file_path)
    csv_file_handler.handle_csv()
