out = []
for i in range(10_000, 100_000):
    if i % 133 == 125 and i % 134 == 111: out.append(str(i))
print(f'Искомые числа: {', '.join(out)}')
