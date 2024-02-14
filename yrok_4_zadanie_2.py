print("Введите пятизначное целое число: ")
a, b, c, d, e = map(int, input())
one = d ** e
two = one * c
three = two / (a - b)
print("Площадь прямоугольника: ", float(three))