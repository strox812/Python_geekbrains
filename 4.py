# Возведение в степень с помощью оператора **:

x = int(input("Введите x: "))
y = int(input("Введите y: "))
def my_func(x, y):
    result = x ** y
    print("Результат:", result)
my_func(x, y)

# Более сложная реализация без оператора **:

x = int(input("Введите x: "))
y = int(input("Введите y: "))
def my_func(x, y):
    p = 1
    while y > 0:
        p *= x
        y -= 1
    print("Результат:", p)
my_func(x, y)
