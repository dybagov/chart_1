minsumma = int(input("Минимальная сумма инвестиций: "))
mike = int(input("Сумма у Майка: "))
ivan = int(input("Сумма у Ивана: "))
if mike >= minsumma and ivan >= minsumma:
    print("2")
elif mike >= minsumma and ivan < minsumma:
    print("Mike")
elif ivan >= minsumma and mike < minsumma:
    print("Ivan")
elif mike + ivan >= minsumma:
    print("1")
else:
    print("0")