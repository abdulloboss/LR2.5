# Вводим кортеж
t = eval(input("Введите кортеж, например, (1, 1, 1, 2, 3, 4): "))

last_unique_index = len(t) - 1
while t[last_unique_index] == t[0]:
    last_unique_index -= 1

count_equal_elements = last_unique_index + 1

print(f"Количество равных элементов в начале кортежа: {count_equal_elements}")
print(f"Элементы, следующие за последним равным элементом: {t[count_equal_elements:]}")
