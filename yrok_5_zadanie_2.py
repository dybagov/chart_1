word = input("Введите слово из маленьких латинских букв: ")
# Списки гласных и согласных букв
vowels = ['a', 'e', 'i', 'o', 'u']
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
# Переменные для хранения количеств гласных и согласных букв
vowel_count = 0
consonant_count = 0
# Прохожу по каждой букве в слове
for letter in word:
    # Проверяю, является ли буква гласной
    if letter.lower() in vowels:
        vowel_count += 1
    # Проверяю, является ли буква согласной
    elif letter.lower() in consonants:
        consonant_count += 1
    # Если буква не является ни гласной, ни согласной, вывожу False
    else:
        print(False)
else:
    print("Количество гласных букв:", vowel_count)
    print("Количество согласных букв:", consonant_count)