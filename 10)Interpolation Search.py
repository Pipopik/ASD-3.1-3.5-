def interpolation_search(arr, target):
    low, high = 0, len(arr) - 1
    
    while low <= high and target >= arr[low] and target <= arr[high]:
        if low == high:
            if arr[low] == target:
                return low
            return -1
        
        # Формула интерполяции
        pos = low + ((high - low) * (target - arr[low])) // (arr[high] - arr[low])
        
        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
    
    return -1

# Пример использования
test_array = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47]
target = 18
result = interpolation_search(test_array, target)
print(f"Массив: {test_array}")
print(f"Поиск {target}: {'Найден на позиции ' + str(result) if result != -1 else 'Не найден'}")
