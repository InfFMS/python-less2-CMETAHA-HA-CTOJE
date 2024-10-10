age = input()
if age[-1] == '0':
    print(f'{age} лет')
elif int(age) in range(11, 20):
    print(f'{age} лет')
elif age[-1] == '1':
    print(f'{age} год')
elif int(age[-1]) in [2, 3, 4]:
    print(f'{age} года')
elif int(age[-1]) in range(5, 10):
    print(f'{age} лет')

