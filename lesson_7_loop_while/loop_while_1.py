# КОГДА НЕТ ТОЧНОЙ ПОСЛЕДОВАТЕЛЬНОСТИ, НО ЕСТЬ ТОЧНОЕ УСЛОВИЕ РАБОТЫ ЦИКЛА
# НО НУЖНО ЧЕТКО ПЛАНИРОВАТЬ ВЫХОД ЧТОБ ЦИКЛ НЕ СТАЛ БЕСКОНЕЧНЫМ - ЭТО ПЛОХО
# i = 0
# while 1 > 0:
#     print(i)
#     i += 1
# В ПИТОНЕ НЕТ ПОСТУСЛОВИЯ ЦИКЛА
import time

# посчитать сколько раз нужно отнять 7 от числа 112 чтоб получилось < 0
# lst_1 = [0, 1, 2, ..., 112]

ost = 112
count = 0
# усложнено. стоит избегать усложнений
# while not (ost < 0):
# достаточно просто
while ost >= 0:

    if count > 100_000:
        # любой из СЦенариев ниже не допустит проваливание в блок else:
        # return
        # raise Exception
        break

    # ost -= 7
    count += 1
    print(count)
# по завершению цикла
else:
    print('вышли из цикла')
    print(count)

# бесконечный цикл - healthcheck
while True:
    # запрос к базе данных поднялась ли она
    print('еще не поднята')
    break

'''
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U $$POSTGRES_USER -d $$POSTGRES_DB || exit 1"]
      interval: 5s
      timeout: 5s
      retries: 20
      start_period: 5s
'''


retries_count = 0
while retries_count < 20:
    # заставляет код ждать 5 секунд
    time.sleep(0.1)

    # запрос к базе данных поднялась ли она

    print('еще не поднята')
    retries_count += 1
# не сработает если выходить из цикла break или ошибкой или еще каким-то способом
else:
    print('базу не удалось поднять')

# у тебя есть приложение APp Store / google play
# человек покупает у тебя в приложении что-то но оплачивает через магазин
# APp Store / Google Play
# WEBHOOK - такая штука которая ждет от внешнего ресурса (в нашем случае Apple
# или google магаз) какого-то события определенного
# и мы ждем события с названием "покупка" и как только его словили, что то делаем

def webhook_payment_check():
    return True

payment_ok = False
while not payment_ok:
    # ЖДАТЬ ПОКА ПРИДЕТ ПОКУПКА ПО WEBHOOK
    time.sleep(5)

    # допустим здесь функция проверки оплаты
    payment_ok = webhook_payment_check()
else:
    print('покупка оплачена')
