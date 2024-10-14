x_first = int(input('x_first >> '))
y_first = int(input('y_first >> '))
x_second = int(input('x_second >> '))
y_second = int(input('y_second >> '))

if abs(y_second - y_first) == 1 and abs(x_second - x_first) == 2:
    print('YES')
elif abs(y_second - y_first) == 2 and abs(x_second - x_first) == 1:
    print('YES')
else:
    print('NO')
