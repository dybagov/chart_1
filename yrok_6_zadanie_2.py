x = int(input("Введите натуральное число X: "))

if x < 1:
    print("Число должно быть натуральным.") #Текст с ошибкой для пользователя
else:
    divisor = 0
    i = 1
    while i*i <= x:
        if x % i == 0:
            if i*i == x:
                divisor += 1
            else:
                divisor += 2
        i += 1
    print("Количество натуральных делителей числа", x, ":", divisor)