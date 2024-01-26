def menu():
      print("\nВыберите действие: \n"
      "1. Отобразить весь справочник\n"
      "2. Найти абонента по фамилии\n"
      "3. Найти абонента по немеру телефона\n"
      "4. Добавить нового абонемента\n"
      "5. Сохранить справочник в текстовом формате\n"
      "6. Завершить работу\n")
      choice = int(input())
      return choice

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

def filter_table(phone_book: list, key = 'Фамилия', parameter = -1):
      if parameter in [0,1,2,3]:
            for el in phone_book:
                  if el[headlines[parameter]] == key:
                        return [el]
            return []
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



def find_by_lastname(phone_book: list,last_name: str):
      max_columns = column_size(file_name)
      # печать шапки таблицы
      for n, column in enumerate(headlines):
            print(f"{column:{max_columns[n]+separator}}", end="")
      print()
      # печать разделителя шапки
      r = f"{'='*sum(max_columns)+'='*len(headlines)*separator}"
      print(r[:-separator])
      # печать тела таблицы
      for el in phone_book:
            if el[headlines[0]] == last_name:
                  for n in range(len(headlines)):
                        print(f"{el[headlines[n]]:{max_columns[n]+separator}}", end="")
                  print()

      print("Такой фамилии нет в справочнике")

def find_by_number():
      print()

def change_number():
      print()

# переменные
file_name_1 = "phone_directory.txt"
file_name = "phonebook.csv"

headlines = ["Фамилия", "Имя", "Телефон", "Примечание"]
separator = 2

# print(read_txt(file_name))
# print(column_size(filter_table(read_txt(file_name))))
