def is_armstrong_numbers():
    n = 10
    while True:
        digits = [int(d) for d in str(n)]
        num_digits = len(digits)
        sum_power_digits = sum([d ** num_digits for d in digits])
        if n == sum_power_digits:
            yield n
        n += 1


def get_armstrong_numbers():
    return next(generator)


generator = is_armstrong_numbers()
for i in range(8):
    print(get_armstrong_numbers(), end=' ')
