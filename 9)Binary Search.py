def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

# Пример использования
test_array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 7
result = binary_search(test_array, target)
print(f"Массив: {test_array}")
print(f"Поиск {target}: {'Найден на позиции ' + str(result) if result != -1 else 'Не найден'}")
