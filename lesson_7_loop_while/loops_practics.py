# ost = 10
# while ost >= 1:
#     print(ost)
#     ost -= 1

# password = ''
# while password != 'admin':
#     password = input('введите пароль: ')
# else:
#     print('вы успешно вошли')


# counter = 0
# while input('нажми enter чтобы продолжить или stop чтобы выйти') != 'stop':
#     counter += 1
#
# print(f'количество нажатий: {counter} ')

# lst = []
# while len(lst) <= 7:
#     lst.append(input('введи элемент: '))
#
# print(lst)

balance = 100

while balance > 0:
    print(balance)
    snatie = int(input('сумма снятия: '))
    if snatie <= balance:
        balance -= snatie
    else:
        print("баланс недостаточно")
        break
print(balance)