import datetime
import time
print("Введите время будильника в фомате ЧЧ ММ СС")
while True:
    n = input().split()
    if (len(n) != 3
            or not n[0].isdigit() or not n[1].isdigit() or not n[2].isdigit()
            or int(n[0]) > 23 or int(n[1]) > 59 or int(n[2]) > 59
            or int(n[0]) < 0 or int(n[1]) < 0 or int(n[2]) < 0):
        print('Проверьте правильность ввода')
        continue
    else:
        break

l = 60
f = 0
dateNow = datetime.datetime.now()
dateCustom = datetime.datetime(dateNow.year, dateNow.month, dateNow.day, int(n[0]), int(n[1]), int(n[2]), 0)
delta = (dateCustom - datetime.datetime.now()).seconds
delta1Perc = delta / 100

while True:
    scale = '|' * l + '.' * f
    now = datetime.datetime.now()
    print('\r{} {}'.format(now.strftime('%H:%M:%S'), scale), end='')
    if now.hour == int(n[0]) and now.minute == int(n[1]) and now.second == int(n[2]):
        print('\n\nБип! ', end='')
        time.sleep(1)
        print('Бип!', end=' ')
        time.sleep(1)
        print('Бип!', end=' ')
        break
    delta -= 1
    l = int(delta / delta1Perc / 100 * 60)
    f = 60 - l
    time.sleep(1)


