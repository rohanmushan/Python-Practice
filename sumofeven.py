def sum_even_numbers(numbers):
    sum = 0
    for num in numbers:
        if num % 2 == 0:
            sum = sum + num
    print(sum)

sum_even_numbers([1, 2, 3, 4, 5, 6])