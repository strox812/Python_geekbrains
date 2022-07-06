profit = float(input("Введите выручку фирмы "))
costs = float(input("Введите издержки фирмы "))
if profit > costs:
    result = profit / costs
    print(f"Фирма работает с прибылью. Рентабельность выручки составила {result}")
    workers = int(input("Введите количество сотрудников фирмы "))
    workers_profit = profit / workers
    print(f"Прибыль в расчете на одного сотрудника составила {workers_profit}")
elif profit == costs:
    print("Фирма работает в ноль")
else:
    print("Фирма работает в убыток")
