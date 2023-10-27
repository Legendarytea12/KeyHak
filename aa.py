import random

characters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
length = 25

keys = int(input("Количество Ключей: "))

random_string = ''.join(random.choice(characters) + ('-' if i % 5 == 4 and i < length - 1 else '') for i in range(length))

print(random_string)
