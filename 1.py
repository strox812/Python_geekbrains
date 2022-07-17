# c параметрами не выходит, могу по простому

from sys import argv


def sal():
    try:
        time = float(input('Выработка в часах: '))
        salary = int(input('Ставка в час: '))
        bonus = int(input('Премия: '))
        res = time * salary + bonus
        print(f'Заработная плата сотрудника  {res}')
    except ValueError:
        return print('Not a number')


sal()

# name, time, salary, bonus = argv
# try:
#     time = int(time)
#     salary = int(salary)
#     bonus = int(bonus)
#     res = time * salary + bonus
#     print(f'Заработная плата сотрудника  {res}')
# except ValueError:
#     print('Not a number')
    
