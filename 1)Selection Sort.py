def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Пример использования
test_array = [64, 25, 12, 22, 11]
print("Исходный массив:", test_array)
print("Отсортированный массив:", selection_sort(test_array.copy()))
