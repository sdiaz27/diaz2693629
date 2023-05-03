def is_perfect_number(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum == n

perfect_numbers = []

for i in range(1, 1001):
    if is_perfect_number(i):
        perfect_numbers.append(i)

print("Hay", len(perfect_numbers), "números perfectos entre 1 y 1000. Son:", perfect_numbers)

