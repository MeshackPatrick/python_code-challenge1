def number_checker(a, b, c):
    positive_count = 0
    if a > 0:
        positive_count += 1
    if b > 0:
        positive_count += 1
    if c > 0:
        positive_count += 1

        return positive_count == 2

    print(number_checker(2, 4, -3))  # Output: True
    print(number_checker(4, -6, 9))  # Output: True
    print(number_checker(-4, 6, 0))  # Output: False