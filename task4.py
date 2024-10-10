N = int(input())
output = []
for i in range(N):
    output.append(str(pow(2, i + 1)))
print(output)
print(' '.join(output))