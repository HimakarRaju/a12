def bubble_sort(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers


numbers = [5, 4, 1, 3, 6, 2]
sorted_numbers = bubble_sort(numbers)
print(sorted_numbers)  # [1, 2, 3, 4, 5, 6]


