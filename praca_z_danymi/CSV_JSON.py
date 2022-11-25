import csv
import sys

class CsvManager:

    def __init__(self, file_path):
        self.file_path = file_path

    def display_info_from_csv(self):
        with open(self.file_path, 'r') as csv_file:
            reader = csv.reader(csv_file)
            #header_rows = next(reader)
            for row in reader:
                print(row)

    def add_record(self):
        # with open(self.file_path, 'r') as csv_file:
        #     reader = csv.reader(csv_file)
            #header_rows = next(reader)

        with open(self.file_path, 'a+', newline='') as csv_file:
            writer = csv.writer(csv_file)
            name = input("Enter new name: ")
            year = input("Enter new year: ")
            rating = input("Enter new rating: ")
            writer.writerow([name, year, rating])

    def delete_record(self):

        choose_record = int(input("\nEnter the number of record you want to delete: "))

        if choose_record == 0:
            print("Wrong number of record entered.")
            return

        with open(self.file_path, 'r') as csv_file:
            reader = csv.reader(csv_file)
            lines = [row for row in reader]

            for indx, row in enumerate(lines):
                if choose_record == indx:
                    lines.remove(row)
                    break
            else:
                print("The record does not exist.")
                return

        with open(self.file_path, 'w', newline='') as csv_out_file:
            writer = csv.writer(csv_out_file)
            writer.writerows(lines)

    def menu(self):
        choice = """
1 - Show all the data
2 - Delete a record
3 - Add a new record
4 - Exit
            
Choice: """

        user_input = {
            1: self.display_info_from_csv,
            2: self.delete_record,
            3: self.add_record,
            4: sys.exit
        }

        while True:
            answer = int(input(choice))
            try:
                user_input[answer]()
            except KeyError:
                print("Invalid user input")


if __name__ == '__main__':
    file_path = "files/csv_file.csv"
    csv_file_handler = CsvManager(file_path)
    csv_file_handler.menu()