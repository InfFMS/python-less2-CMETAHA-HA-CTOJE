x_first = int(input('x_first >> '))
y_first = int(input('y_first >> '))
x_second = int(input('x_second >> '))
y_second = int(input('y_second >> '))

if x_second > x_first and abs(y_second - y_first) == x_second - x_first:
    print('YES')
elif x_second < x_first and abs(y_second - y_first) == x_first - x_second:
    print('YES')
else:
    print('NO')
