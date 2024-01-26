from functions_phonebook import *
import os



def main():
    phonebook = read_txt(file_name)
    choice = print_menu()
    while choice != 7:
        clear_console()
        if choice == 1:
            content = filter_table(phonebook)
            print_table(content,column_size(content))
        if choice == 2:
            key_for_search = print_parametr_for_search()
            clear_console()
            value_for_search = input(f"Введите параметр {key_for_search} для поиска: ")
            clear_console()
            content = filter_table(phonebook, key_for_search, value_for_search)
            print_table(content,column_size(content))
            print()
            choice2 = print_submenu()
            if choice2 == 2:
                clear_console()
                key_for_change = print_parametr_for_change()
                clear_console()
                phonebook = change_data(phonebook, key_for_search, value_for_search, key_for_change)
                content = filter_table(phonebook, key_for_search, value_for_search)
                print_table(content,column_size(content))
                print("Данные успешно изменены!")
                choice3 = print_choice_menu
                if choice3 == 1:
                    print()
        clear_console()
        choice = print_menu()

main()