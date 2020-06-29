# This is the main of the playground
def my_print(a, b):
    if a <= b:
        m = (a + b) // 2
        my_print(a, m - 1)
        print(m, end="")
        my_print(m + 1, b)


my_print(1, 100)
