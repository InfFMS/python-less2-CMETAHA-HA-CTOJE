a_1 = int(input('a_1 >> '))
b_1 = int(input('b_1 >> '))
a_2 = int(input('a_2 >> '))
b_2 = int(input('b_2 >> '))

if a_2 <= b_1:
    print(max(a_1, a_2))
    print(min(b_1, b_2))
else:
    print('пустое множество')
