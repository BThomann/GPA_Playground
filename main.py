def my_calc(n):
    count = 0
    for i in range(1, n):
        for j in range(0, n, n // 2):
            count += 1
    return count


print(my_calc(5))
