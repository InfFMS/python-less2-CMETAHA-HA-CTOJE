N = int(input())

res = []
for i in range(2, N):
    pot = 1
    for j in res:
        if i % j == 0:
            pot = 0
            break
    if pot == 1:
        res.append(i)
    pot = 1
print(*res)