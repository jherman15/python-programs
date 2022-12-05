if __name__ == '__main__':
    user_input = input("Enter your name, surname and the year of birth. Values must be separated by commas and spaces:\n")
    try:
        name, surname, birth_year = user_input.split(", ")
    except ValueError:
        print("Wrong data format")
    else:
        print(f"Name: {name}, surname: {surname}, birth year: {birth_year}")
