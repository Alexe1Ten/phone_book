from functions_phonebook import *
import os



def main():
    phonebook = read_txt(file_name)
    choice = print_menu()
    clear_console()
    while choice != 7:
        if choice == 1:
            content = filter_table(phonebook)
            print_table(content,column_size(content))
        if choice == 2:
            filtering_parameter = print_parametr_for_search()
            clear_console()
            last_name = input(f"Введите параметр {headlines[filtering_parameter - 1]} для поска: ")
            content = filter_table(phonebook, last_name, filtering_parameter - 1)
            print_table(content,column_size(content))

        input("\nНажмите Enter чтобы продолжить")
        clear_console()
        choice = print_menu()
        clear_console()

main()