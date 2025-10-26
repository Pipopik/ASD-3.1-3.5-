def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Пример использования
test_array = [3, 5, 2, 7, 9, 1, 4]
target = 7
result = linear_search(test_array, target)
print(f"Массив: {test_array}")
print(f"Поиск {target}: {'Найден на позиции ' + str(result) if result != -1 else 'Не найден'}")
