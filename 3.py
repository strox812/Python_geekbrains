num_1 = int(input("Введите первое число: "))
num_2 = int(input("Введите второе число: "))
num_3 = int(input("Введите третье число: "))

def my_func(num_1, num_2, num_3):
    if num_1 >= num_3 and num_2 >= num_3:
        print(num_1 + num_2)
    elif num_1 > num_2 and num_1 < num_3:
        print(num_1 + num_3)
    else:
        print(num_2 + num_3)
        
my_func(num_1, num_2, num_3)
