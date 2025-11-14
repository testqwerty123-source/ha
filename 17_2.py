def max_subarray_sum_non_adjacent(arr: list) -> int:
    n = len(arr)
    
    if n == 0:
        return 0
    if n == 1:
        return arr[0]
        
    # included_max відповідає dp[i-1][1] (сума, включаючи попередній елемент)
    # excluded_max відповідає dp[i-1][0] (сума, не включаючи попередній елемент)
    excluded_max = 0 
    included_max = arr[0]
    
    for i in range(1, n):
        # Сума, якщо НЕ включаємо arr[i]: 
        # беремо краще з попередніх станів
        new_excluded_max = max(excluded_max, included_max)
        
        # Сума, якщо ВКЛЮЧАЄМО arr[i]: 
        # беремо суму, яка НЕ включала arr[i-1], і додаємо arr[i]
        new_included_max = excluded_max + arr[i]
        
        # Оновлення
        excluded_max = new_excluded_max
        included_max = new_included_max

    return max(included_max, excluded_max)

# --- Приклади ---
array1 = [3, 2, 7, 10]
array2 = [5, 5, 10, 40, 50, 35]
array3 = [30, 15, 60, 75]

print(max_subarray_sum_non_adjacent(array1))
print(max_subarray_sum_non_adjacent(array2))
print(max_subarray_sum_non_adjacent(array3))
