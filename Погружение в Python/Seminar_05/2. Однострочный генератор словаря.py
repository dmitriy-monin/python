"""
Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
имена str, ставка int, премия str с указанием процентов вида “10.25%”.
В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
Сумма рассчитывается как ставка умноженная на процент премии
"""

names = ["John", "Mike", "Sam"]
rates = [20000, 18000, 25000]
premiums = ["10.25%", "8%", "7.75%"]
gen = {name: round(rate * float(premium.strip('%')) / 100, 2) for name, rate, premium in zip(names, rates, premiums)}
print(gen)
