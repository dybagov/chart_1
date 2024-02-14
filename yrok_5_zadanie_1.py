vvod = int(input("Введите число: "))

if vvod % 2 == 0 and vvod > 0:
    print("Положительное чётное число")
elif vvod % 2 == 0 and vvod < 0:
    print("Отрицательное чётное число")
elif vvod % 2 == 1 and vvod > 0:
    print("Положительное нечётное число")
elif vvod % 2 == 1 and vvod < 0:
    print("Отрицательное нечётное число")
else:
    print("Нулевое число")