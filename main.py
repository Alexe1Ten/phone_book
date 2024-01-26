from functions_phonebook import *


def main():
    phonebook = read_txt(file_name)
    choice = menu()
    while choice != 7:
        if choice == 1:
            content = filter_table(phonebook)
            print_table(content,column_size(content))
        if choice == 2:
            filtering_parameter = 0
            last_name = input("Введите фамилию: ")
            content = filter_table(phonebook, last_name, filtering_parameter)
            print_table(content,column_size(content))

        input("Нажмите Enter чтобы продолжить")
        print()
        choice = menu()

main()