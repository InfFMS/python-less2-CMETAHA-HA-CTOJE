numMonth = int(input())
if numMonth in [1, 2, 12]:
    print('Зима')
elif numMonth in range(3, 6):
    print('Весна')
elif numMonth in range(6, 9):
    print('Лето')
elif numMonth in range(9, 12):
    print('Осень')
else:
    print('Неверный номер месяца')