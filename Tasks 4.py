
# Задача 1

from datetime import datetime

while True:
    try:
        day = int(input("День: "))
        month = int(input("Місяць: "))
        year = int(input("Рік(4 цифри): "))
    
        date = datetime(year,month,day)
        break

    except ValueError:
        print("Некоректна дата, спробуйте ще раз")
       
def get_days_from_today(date):
    difference = datetime.today() - date
    return difference.days
    
result = get_days_from_today(date)
print(result)

# Задача 2

import random

def get_numbers_ticket(min_val,max_val,quantity):
    if (
        min_val < 1 or
        max_val > 1000 or
        min_val >= max_val or
        quantity <= 0 or
        quantity > (max_val - min_val + 1)
    ):
        return []
    numbers = random.sample(range(min_val, max_val + 1), quantity)
    return sorted(numbers)

min_val = int(input("Введіть початок діапазону: "))
max_val = int(input("Введіть кінець діапазону: "))
quantity = int(input("Введіть необхідну кількість чисел: "))

result = get_numbers_ticket(min_val, max_val, quantity)
print("Ваші лотерейні числа:", result)

# Задача 3
import re

raw_numbers = [
    "067\t123 4567",
    "(095) 234-5678\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

def normalize_phone(phone_number):
    phone_number = phone_number.strip()
    phone_number = re.sub(r"[^\d+]", "", phone_number)
    if phone_number.startswith("380"):
        return "+" + phone_number
    elif phone_number.startswith("+"):
        return phone_number
    else:
        return "+38" + phone_number

sanitized_numbers = []
for num in raw_numbers:
    sanitized_numbers.append(normalize_phone(num))

print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)

# Задача 4
from datetime import datetime, timedelta

users = [
    {"name": "John Doe", "birthday": "1985.03.14"},
    {"name": "Jane Smith", "birthday": "2004.02.29"},
    {"name": "Jaad", "birthday": "2005.02.14"},
    {"name": "Kate", "birthday": "1995.04.15"}
]

def get_upcoming_birthdays(users):
    result = []

    current_date = datetime.today().date()
    end_date = current_date + timedelta(days=7)

    for user in users:
        birthday_str = user["birthday"]
        birthday_date = datetime.strptime(birthday_str, "%Y.%m.%d").date()
        try:
            birthday_this_year = birthday_date.replace(year=current_date.year)
        except ValueError: #перевірка якщо др 29 лютого а рік не високосний
            birthday_this_year = datetime(current_date.year, 3, 1).date()

        if birthday_this_year < current_date:
            birthday_this_year = birthday_this_year.replace(year=current_date.year + 1)

        if birthday_this_year >= current_date and birthday_this_year <= end_date:
            congrat_date = birthday_this_year

            if congrat_date.weekday() == 5:   
                congrat_date = congrat_date + timedelta(days=2)

            elif congrat_date.weekday() == 6:
                congrat_date = congrat_date + timedelta(days=1)

            result.append({
                "name": user["name"],
                "congratulation_date": congrat_date.strftime("%Y.%m.%d")
            })

    return result

birthdays = get_upcoming_birthdays(users)

for i in birthdays:
    print({
        "name": i["name"],
        "congratulation_date": i["congratulation_date"]
    })
