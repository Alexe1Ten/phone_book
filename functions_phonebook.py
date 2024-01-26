def print_menu():
      print(menu)
      choice = int(input("Выберите действие: "))
      return choice

def print_submenu():
      print(submenu)
      choice = int(input("Выберите действие: "))
      return choice

def print_choice_menu():
      print(choice_menu)
      choice = int(input(f"Сохранить изменения в файл {file_name_1}?"))
      return choice

def print_parametr_for_search():
      for i, el in enumerate(headlines):
            print(f"{i + 1}. {el}")
      print()
      choice = int(input(f"Выберите параметр для поиска: "))
      return headlines[choice - 1]

def print_parametr_for_change():
      for i, el in enumerate(headlines):
            print(f"{i + 1}. {el}")
      print()
      choice = int(input(f"Выберите параметр для изменения: "))
      return headlines[choice - 1]

def clear_console():
      print("\033c", end="")

def read_txt(file_name: str):
      phone_book = []
      with open(file_name, "r", encoding='utf-8') as tmp:
            for line in tmp:
                  record = dict(zip(headlines, line.replace("\n","").split(",")))
                  phone_book.append(record)
            return phone_book

def column_size(table: list):
      max_columns = []
      size_columns = [[len(el) for el in headlines]]
      for coup in table:
            len_el = []
            [len_el.append(len(el)) for el in coup.values()]
            size_columns.append(len_el)
      for col in zip(*size_columns):
            max_columns.append(max(col))
      return max_columns

def filter_table(phone_book: list, key = "", value = ""):
      for el in phone_book:
            if el[key] == value.lower().capitalize():
                  return [el]
      return phone_book

def print_headlines(colum_size: list):
      # печать шапки таблицы
      for n, column in enumerate(headlines):
            print(f"{column:{colum_size[n]+separator}}", end="")
      print()
      # печать разделителя шапки
      r = f"{'='*sum(colum_size)+'='*len(headlines)*separator}"
      print(r[:-separator])

def print_table(filter_table: list, max_columns: list):
      print_headlines(max_columns)
      # печать тела таблицы
      for el in filter_table:
            for n in range(len(headlines)):
                  print(f"{el[headlines[n]]:{max_columns[n]+separator}}", end="")
            print()


def change_data(phone_book: list, key: str, val: str, key_for_change: str):
      new_val = input(f"Введите новое значение для параметра {key_for_change}: ")
      for el in phone_book:
            if el[key] == val.lower().capitalize():
                  el[key_for_change] = new_val
      clear_console()
      return phone_book

# переменные
file_name_1 = "phone_directory.txt"
file_name = "phonebook.csv"
headlines = ["Фамилия", "Имя", "Телефон", "Примечание"]
menu = "1. Отобразить весь справочник\n"\
      "2. Найти абонента\n"\
      "3. Добавить нового абонемента\n"\
      "4. Завершить работу\n"
submenu = "1. Меню\n"\
      "2. Изменить данные\n"
choice_menu = "1. Да\n"\
            "2. Нет\n"

separator = 2

