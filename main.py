from functions_phonebook import *

def main():
    phonebook = read_txt(file_name_1)
    clear_console()
    choice = print_menu()
    while choice != 4:
        clear_console()
        if choice == 1:
            content = filter_table(phonebook)
            print_table(content,column_size(content))
            input("\nНажмите Enter чтобы вернуться в меню")
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
                choice3 = print_choice_menu()
                if choice3 == 1:
                    writing_to_file(file_name_1, phonebook)
                    print(f"Изменения успешно внесены в файл {file_name_1}")
            elif choice2 == 3:
                del_data(phonebook, key_for_search, value_for_search)
                writing_to_file(file_name_1, phonebook)
                print("Данные умпешно удалены!")
                input("\nНажмите Enter чтобы вернуться в меню")
        if choice == 3:
            add_data(phonebook)
            writing_to_file(file_name_1, phonebook)
        
        clear_console()
        choice = print_menu()
    clear_console()
main()

