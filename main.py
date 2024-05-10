import datetime
from classes import Record
from func import *
path_data = 'data/finances.txt'
records = read_data(path_data)
def main():   
    
    # Меню программы
    while True:
        print('\nВыберите действие:')
        print('1. Вывод баланса')
        print('2. Добавление записи')
        print('3. Редактирование записи')
        print('4. Поиск по записям')
        print('5. Выход')
        
        choice = input('Введите номер действия: ')
        
        if choice == '1':
            if len(records) == 0: 
                print('Запсей нет')
            else:
                show_balance(records)
        elif choice == '2':
            add_data_ui()
        elif choice == '3':
            if len(records) == 0:
                print('Запсей нет')
            else:
                edit_data_ui(records)
        elif choice == '4':
            if len(records) == 0:
                print('Запсей нет')
            else:
                search_data_ui(records)
        elif choice == '5':
            print('Данные сохранены.')
            break
        else:
            print('Некорректный ввод. Попробуйте еще раз.')

# Интерфейс получения данных от пользователя для новой записи
def add_data_ui():
    print('\nДобавление новой записи:')
    date = check_date(input('Введите дату (гггг-мм-дд): '))
    category = check_category(input('Введите категорию (Доход/Расход): '))
    amount = float(check_num(input('Введите сумму: ')))
    comment = input('Введите описание: ')
    new_record = Record(date, category, amount, comment)
    add_data(path_data, new_record)
    print('Запись добавлена')

# Интерфейс получения данных от пользователя для редактирования записи
def edit_data_ui(records):
    print('\nРедактирование записи:')
    id = int(input('Введите номер записи для редактирования: ')) - 1
    if 0 <= id < len(records):
        record = records[id]
        print('Текущая запись:')
        print(record)
        date = check_date(input('Введите новую дату или оставьте пустым (гггг-мм-дд): '))
        if date == '':
            date = record['Дата']
        category = check_category(input('Введите новую категорию или оставьте пустым (Доход/Расход): '))
        if category == '':
            category = record['Категория']
        amount = float(check_num(input('Введите новую сумму: ')))
        comment = input('Введите новое описание или оставьте пустым: ')
        if comment == '':
            comment = record['Комментарий']
        new_record = {'Дата': date, 'Категория': category, 'Сумма': amount,'Комментарий': comment}
        edit_data(path_data, records, id, new_record)
    else:
        print('Некорректный номер записи.')
        edit_data_ui(records)

# Интерфейс получения данных от пользователя для поиска записей
def search_data_ui(records):
    print('\nПоиск по записям:')
    category = input('Введите категорию (Доход/Расход) или оставьте пустым: ')
    start_date = input('Введите начальную дату (гггг-мм-дд) или оставьте пустым: ')
    end_date = input('Введите конечную дату (гггг-мм-дд) или оставьте пустым: ')
    min_amount = input('Введите минимальную сумму или оставьте пустым: ')
    max_amount = input('Введите максимальную сумму или оставьте пустым: ')

    if start_date:
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
    if end_date:
        end_date = datetime.strptime(end_date, '%Y-%m-%d')
    if min_amount:
        min_amount = float(min_amount)
    if max_amount:
        max_amount = float(max_amount)

    results = search_data(records, category, start_date, end_date, min_amount, max_amount)
    if results:
        print('\nРезультаты поиска:')
        for i, record in enumerate(results, start=1):
            print(f'\nКоличество найденых записей: {i}')
            print(record)
    else:
        print('По вашему запросу ничего не найдено.')
if __name__ == '__main__':
    main()