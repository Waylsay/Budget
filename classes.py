class Record:
    def __init__(self, date, category, amount, comment):
        self.date = date
        self.category = category
        self.amount = amount
        self.comment = comment
    def __str__(self):
        return f'Дата: {self.date}\nКатегория: {self.category}\nСумма: {self.amount}\nКомментарий: {self.comment}'