A = int(input("Введите целое число A: "))
B = int(input("Введите целое число B: "))

if A > B:
    print("Ошибка: <A> должно быть меньше или равно <B>.")
else:   # Перебираем числа от A до B
    for i in range(A, B + 1):
        if i % 2 == 0:
            print(i, end=" ")