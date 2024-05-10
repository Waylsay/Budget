from classes import Record
from datetime import datetime
# Чтение из файла
def read_data(path_data):
    records = []
    with open(path_data, 'r', encoding='utf-8') as file:
        record_data = {}
        for line in file:
            if line.strip():
                key, value = line.strip().split(': ')
                record_data[key] = value
            else:
                records.append(record_data)
                record_data = {}
        if record_data:
            records.append(record_data)
    return records

# Добавление записи
def add_data(path_data, new_record):
    with open(path_data, 'a', encoding='utf-8') as file:
        file.write(f'{new_record}\n')
        file.write('\n')

# Поиск по записям
def search_data(records, category=None, start_date=None, end_date=None, min_amount=None, max_amount=None):
    results = []
    i = 0
    for record in records:
        i += 1
        record['id'] = i  
        if (not category or record.get('Категория') == category) and \
        (not start_date or record.get('Дата') >= start_date) and \
        (not end_date or record.get('Дата') <= end_date) and \
        (not min_amount or record.get('Сумма') >= min_amount) and \
        (not max_amount or record.get('Сумма') <= max_amount):
            results.append(record)
    return results

# Редактирование записи
def edit_data(path_data, records, id, new_record):
    records[id] = new_record
    with open(path_data, 'w', encoding='utf-8') as file:
        for new_data in records:
            new_line = Record(new_data['Дата'], new_data['Категория'], new_data['Сумма'], new_data['Комментарий'])
            file.write(f'{new_line}\n\n')
        
    print('Запись изменена')

# Отображение баланса
def show_balance(records):
    income = sum(float(record.get('Сумма')) for record in records if record.get('Категория') == 'Доход')
    expenses = sum(float(record.get('Сумма')) for record in records if record.get('Категория') == 'Расход')
    balance = income - expenses
    print(f'Текущий баланс: {balance}')
    print(f'Доходы: {income}')
    print(f'Расходы: {expenses}')

# Проверка на число
def check_num(data):
    try:
        float(data)
        return data
    except ValueError:
        print('Некорректный ввод')
        data = input('Введите число: ')

# Проверка Доход/Расход
def check_category(data):
    if  not data in ('Доход', 'Расход'):    
        print('Некорректный ввод')
        data = input('Введите категорию (Доход/Расход): ')
    return data

# Проверка формата даты
def check_date(data):
    while True:
        try:
            valid_date = datetime.strptime(data, '%Y-%m-%d')     
        except ValueError:
            print('Некорректный формат даты')
            data = input('Введите дату (гггг-мм-дд): ')
        else:            
            break
    return data