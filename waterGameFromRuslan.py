vedro3 = 0
vedro5 = 0
countWater = 0
isWater3 = ''
isWater5 = ''
fullWater3 = '[:::]'
fullWater5 = '[:::::]'
halfWater3 = '[...]'
halfWater5 = '[.....]'
emptyWater3 = '[   ]'
emptyWater5 = '[     ]'

print('_'*74)
print('| >> Введите команду по принципу "откуда = куда", где "=" это разделитель |')
print('| >> Используйте для этого только слова: 3, 5, kran, sliv                 |')
print('| >> Где: 3 = 3-х литровое ведро, 5 = 5-и литровое ведро,                 |')
print('|  \tkran = налить из крана, sliv = вылить из ведра                        |')
print('| >> Например команда "kran = 5" - налить в 5л ведро                      |')
print('| >> Команда "5 = sliv" - вылить из 5л ведра                              |')
print('| >> Команда "3 = 5" - перелить из 3л ведра в 5л ведро                    |')
print('_'*74)
print('Введите команду:')
while True:
    action = [i.lower() for i in input().split()]
    #print(action)

    if len(action) < 3:
        print('В какую игру вы играете? Проверьте правильность ввода')
        print('3{}  ({})\t\t5{}  ({})\t\t[{}.0] - счётчик воды'.format(isWater3, vedro3, isWater5, vedro5, countWater))
        continue

    if action[0] == 'kran' and action[2] == '5':
        if vedro5 == 5:
            print('Что-то мне подсказывает, что 5 литровое ведро может вместить только 5 литров')
        else:
            while vedro5 != 5:
                vedro5 += 1
                countWater += 1

    elif action[0] == '3' and action[2] == '5':
        if vedro5 == 5:
            print('Что-то мне подсказывает, что 5 литровое ведро может вместить только 5 литров')
        else:
            while (vedro3 != 0) and (vedro5 != 5):
                vedro3 -= 1
                vedro5 += 1

    elif action[0] == 'kran' and action[2] == '3':
        if vedro3 == 3:
            print('Что-то мне подсказывает, что 3 литровое ведро может вместить только 3 литра')
        else:
            while vedro3 != 3:
                vedro3 += 1
                countWater += 1

    elif action[0] == '5' and action[2] == '3':
        if vedro3 == 3:
            print('Что-то мне подсказывает, что 3 литровое ведро может вместить только 3 литра')
        else:
            while vedro3 != 3 and vedro5 != 0:
                vedro5 -= 1
                vedro3 += 1

    elif action[0] == '3' and action[2] == 'sliv':
        if vedro3 == 0:
            print('Вы выливаете воздух')
        else:
            vedro3 = 0

    elif action[0] == '5' and action[2] == 'sliv':
        if vedro5 == 0:
            print('Вы выливаете воздух')
        else:
            vedro5 = 0

    elif action[0] == 'kran' and action[2] == 'sliv':
        print('Попадите уже в ведро')

    elif action[0] == 'sliv' and action[2] == 'kran':
        print('Если у вас что-нибудь получиться - я подарю вам вёдра')

    if vedro3 == 0:
        isWater3 = emptyWater3
    elif vedro3 == 3:
        isWater3 = fullWater3
    else:
        isWater3 = halfWater3
    if vedro5 == 0:
        isWater5 = emptyWater5
    elif vedro5 == 5:
        isWater5 = fullWater5
    else:
        isWater5 = halfWater5

    if vedro3 + vedro5 != 4:
        print('3{}  ({})\t\t5{}  ({})\t\t[{}.0] - счётчик воды'.format(isWater3, vedro3, isWater5, vedro5, countWater))
    elif vedro3 + vedro5 == 4:
        print('3{}  ({})\t\t5{}  ({})\t\t[{}.0] - счётчик воды'.format(isWater3, vedro3, isWater5, vedro5, countWater))
        print('Отлично! Вы таки набрали 4 литра! Счёт за воду вышлем в ближайшее время.')
        break

    else:
        print('В какую игру вы играете? Проверьте правильность ввода')
