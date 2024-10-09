k = 1
N = 133 * k + 125
numbers = []
out = []
while N // 100000 == 0:
    numbers.append(str(N))
    if N // 10000 != 0:
        out.append(str(N))
    N += 133
print(f'Искомые числа: {', '.join(out)}')
