numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in range(1, len(numbers)):
    count_divisor = 0
    for j in range(2, i):
        if numbers[i] % j == 0:
            count_divisor += 1
    if count_divisor == 0:
        primes.append(numbers[i])
    else:
        not_primes.append(numbers[i])
print(primes)
print(not_primes)