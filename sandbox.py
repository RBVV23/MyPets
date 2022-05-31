# Функции def, описанные ниже, принимают на вход номер выбранной позиции и возвращают ее название
def coffee2(n):
    if n == 1:
        return ' американо '
    elif n == 2:
        return ' латте '
    elif n == 3:
        return ' капучино '
    elif n == 4:
        return ' раф '
    elif n == 5:
        return ' флет уайт '


def syrup2(n):
    if n == 1:
        return 'с карамельным сиропом '
    elif n == 2:
        return 'с ванильным сиропом '
    elif n == 3:
        return 'с банановым сиропом '
    elif n == 4:
        return 'с сиропом лесной орех '
    elif n == 5:
        return 'с кокосовым сиропом '
    elif n == 6:
        return 'с клубничным сиропом '


def milk2(n):
    if n == 1:
        return 'на обычном молоке'
    elif n == 2:
        return 'на овсяном молоке'
    elif n == 3:
        return 'на миндальном молоке'
    elif n == 4:
        return 'на кокосовом молоке'
    elif n == 5:
        return 'на соевом молоке'
    elif n == 6:
        return 'на банановом молоке'


def tea2(n):
    if n == 1:
        return ' черный чай'
    elif n == 2:
        return ' зеленый чай'
    elif n == 3:
        return ' молочный улун'
    elif n == 4:
        return ' чай с чабрецом'
    elif n == 5:
        return ' жасминовый чай'
    elif n == 6:
        return ' Эрл Грей'


def size2(n):
    if n == 1:
        return 'Маленький'
    if n == 2:
        return 'Средний'
    if n == 3:
        return 'Большой'


def take2(n):
    if n == 1:
        return ' с собой '
    elif n == 2:
        return ' здесь '


# переменная  whole_order содержит в себе заказ клиента
whole_order = ''

# следующие 4 переменные представляют собой меню, у каждой позиции есть присвоенный номер
coffee1 = '1 - Американо, 2 - Латте, 3 - Капучино, 4 - Раф, 5 - Флет уайт, 6 - другое'
milk1 = '1 - обычное, 2 - овсяное, 3 - миндальное, 4 - кокосовое, 5 - соевое, 6 - банановое, 7 - другое'
tea1 = '1 - черный, 2 - зеленый, 3 - молочный улун, 4 - чай с чабрецом, 5 - жасмин, 6 - эрл грей, 7 - другое'
syrup1 = '1 - карамельный, 2 - ванильный, 3 - банановый, 4 - лесной орех, 5 - кокосовый, 6 клубничный, 7 - другое'

# следующие 2 переменные представляют собой размер и способ выдачи заказа, у каждой позиции есть присвоенный номер
size1 = '1 - маленький, 2 - средний, 3 - большой'
take1 = '1 - с собой, 2 - здесь'

# приветствие бота с клиентом
print(
    "Здравствуйте! Добро пожаловать в BestPlaceCafe. Вас приветствует чат-бот Напиточник, сегодня я буду принимать Ваш заказ.")
name = input('Как Вас зовут? ')
print(f'Очень приятно, {name}!')
option1 = '1 - кофе, 2 - чай, 3 - другое'

# на данном этапе клиенту нужно сделать основной выбор между позициями из option1, цикл while True работает пока клиент не введет одну из трех цифр
while True:
    main_choice = int(
        input(f'Что Вы желаете заказать? Введите одну цифру, соответствующую Вашему выбору:\n {option1}\n '))
    if main_choice == 1 or main_choice == 2:
        break
    if main_choice == 3:
        print(f'{name}, к сожалению, я не могу Вас обслужить. Обратитесь в другое кафе. Хорошего дня!')
        break

# если клиент выбрал кофе, то далее нужно выбрать размер напитка
if main_choice == 1:
    size = int(input(f'Выберите размер напитка:\n {size1}\n '))
    whole_order += size2(size)

    # цикл while True работает пока клиент не введет запрошенный ответ в требуемом формате;
    # если выбрана цифра 6, то есть два варианта: 1. продолжить - в таком случае нужно заново выбрать напиток, или 2. уйти - тогда бот прекращает работу.
    while True:
        order = int(input(f'Введите одну цифру, соответствующую Вашему выбору:\n {coffee1}\n '))
        if order == 6:
            msg = input(
                f' {name}, к сожалению, в наличие есть только предложенные позиции. Вы хотите выбрать другой напиток или сделать заказ в другом месте?\n Ответьте "продолжить" или "уйти" с маленькой буквы без ковычек:\n')
            while msg != 'продолжить' and msg != 'уйти':
                msg = input('Боюсь, я неправильно Вас поняла, введите Ваш ответ еще раз: ')
            if msg == 'продолжить':
                continue
            else:
                if msg == 'уйти':
                    print('До свидания, хорошего дня!')
                    break
        if order in [1, 2, 3, 4, 5]:
            whole_order += str(coffee2(order))
            break

    # если выбрана цифра 1 (американо), то предлагается выбор молока
    if order == 1:
        choice_ = input('Добавить ли Вам молоко? Введите "да" или "нет" с маленькой буквы без ковычек: ')
        if choice_ == 'да':
            # цикл  while True работает пока клиент не введет запрошенный ответ в требуемом формате
            while True:
                kind_of_milk = int(input(
                    f'На каком молоке приготовить Ваш напиток?\nВведите одну цифру, соответствующую Вашему выбору:\n {milk1}\n '))
                if kind_of_milk == 7:
                    print(f'{name}, к сожалению, в наличие есть только предложенные позиции. Сделайте выбор снова.')
                else:
                    whole_order += milk2(kind_of_milk)
                    break
        else:
            choice_ = 'обычный'
            whole_order += choice_

    # при выборе остальных опций можно выбрать сироп
    if order == 2 or order == 3 or order == 4 or order == 5:
        presence_of_syrup = input('Добавить ли в кофе сироп? Введите "да" или "нет" с маленькой буквы без ковычек: ')
        if presence_of_syrup == 'да':
            while True:
                choice_of_syrup = int(input(f'Введите одну цифру, соответствующую Вашему выбору:\n {syrup1}\n '))
                if choice_of_syrup in [1, 2, 3, 4, 5, 6]:
                    whole_order += syrup2(choice_of_syrup)
                    break
                elif choice_of_syrup == 7:
                    msg2 = input(
                        f'{name}, к сожалению, в наличие есть только предложенные позиции. Хотите ли выбрать снова или приготовить кофе без сиропа? Ответьте "снова" или "без сиропа" с маленькой буквы без ковычек.')
                    while msg2 != 'снова' and msg2 != 'без сиропа':
                        msg2 = input('Боюсь, я неправильно Вас поняла, введите Ваш ответ еще раз: ')
                    if msg2 == 'снова':
                        continue
                    elif msg2 == 'без сиропа':
                        break

        # цикл while True работает пока клиент не выберет молоко
        while True:
            kind_of_milk = int(input(
                f'На каком молоке приготовить Ваш напиток?\nВведите одну цифру, соответствующую Вашему выбору:\n {milk1}\n '))
            if kind_of_milk == 7:
                print(f'{name}, к сожалению, в наличие есть только предложенные позиции. Сделайте выбор снова.')
            else:
                whole_order += milk2(kind_of_milk)
                break

    # при выборе любого кофе из представленных вариантов нужно выбрать способ выдачи заказа и по желанию добавить к whole_order печенье
    if order in [1, 2, 3, 4, 5]:
        take = int(input(
            f'Возьмете с собой или останетесь в кафе? Введите цифру, соответствующую Вашему выбору:\n {take1}\n '))
        whole_order += take2(take)

        cookie = input('Хотите печенье в подарок? Введите "да" или "нет" с маленькой буквы без ковычек: ')
        if cookie == 'да':
            whole_order += 'с печеньем'

        # на данном этапе предложена проверка заказа
        print('Давайте проверим Ваш заказ: ')
        print(whole_order)
        final = input(
            'Если заказ верный, то введите "да" с маленькой буквы без ковычек, если нет, то введите "нет" с маленькой буквы без ковычек: ')
        if final == 'да':
            print('Спасибо за заказ! Ожидайте.')
        if final == 'нет':
            print('Обновите, пожалуйста, бот и сделайте заказ снова. Спасибо за понимание!')

# если клиент выбрал чай, то далее нужно выбрать размер напитка
if main_choice == 2:
    size = int(input(f'Выберите размер напитка:\n {size1}\n '))
    whole_order += size2(size)

    # цикл while True работает пока клиент не введет запрошенный ответ в требуемом формате;
    # если выбрана цифра 7, то есть два варианта: 1. продолжить - в таком случае нужно заново выбрать напиток, или 2. уйти - тогда бот прекращает работу.

    while True:
        order = int(input(f'Введите одну цифру, соответствующую Вашему выбору:\n {tea1}\n '))
        if order == 7:
            msg = input(
                f' {name}, к сожалению, в наличие есть только предложенные позиции. Вы хотите выбрать другой напиток или сделать заказ в другом месте?\n Ответьте "продолжить" или "уйти" с маленькой буквы без ковычек:\n')
            while msg != 'продолжить' and msg != 'уйти':
                msg = input('Боюсь, я неправильно Вас поняла, введите Ваш ответ еще раз: ')
            if msg == 'продолжить':
                continue
            else:
                if msg == 'уйти':
                    print('До свидания, хорошего дня!')
                    break
        if order in [1, 2, 3, 4, 5, 6]:
            whole_order += str(tea2(order))
            break
    # при выборе любого кофе из представленных вариантов нужно выбрать способ выдачи заказа и по желанию добавить к whole_order печенье
    if order in [1, 2, 3, 4, 5, 6]:
        take = int(input(
            f'Возьмете с собой или останетесь в кафе? Введите цифру, соответствующую Вашему выбору:\n {take1}\n '))
        whole_order += take2(take)

        cookie = input('Хотите печенье в подарок? Введите "да" или "нет" с маленькой буквы без ковычек: ')
        if cookie == 'да':
            whole_order += 'с печеньем'

        # на данном этапе предложена проверка заказа
        print('Давайте проверим Ваш заказ: ')
        print(whole_order)
        final = input(
            'Если заказ верный, то введите "да" с маленькой буквы без ковычек, если нет, то введите "нет" с маленькой буквы без ковычек: ')
        if final == 'да':
            print('Спасибо за заказ! Ожидайте.')
        if final == 'нет':
            print('Обновите, пожалуйста, бот и сделайте заказ снова. Спасибо за понимание!')
