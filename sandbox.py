import random  # импортируем библиотеку рандом
# https://docs.python.org/3/library/random.html 
import time  # импортируем библиотеку для работы со временем

# Будем использовать ее для подсчета времени работы программы
# https://docs.python.org/3/library/time.html 

# Списки со странами
winter_active_countries = ['Австрия', 'Финляндия', 'Швейцария']  # Список из холодных стран для активного отдыха
vac_list = ['Индия', 'Зимбабмве', 'Танзания']  # Список стран, где нужна вакцина
not_vac_list = ['Южная Корея', 'Иран', 'Индонезия']  # Список стран, где не нужна вакцина
passive_relax = ['Монако', 'Франция', 'Греция']  # Список стран для спокойного отдыха
sea_list = ['Австралия', 'Доминикана', 'Шри-Ланка']  # Список стран у моря
individ_list = ['Грузия', 'Чехия', 'Черногория']  # Cтраны для индивидуальных путешественников
tur_list = ['Турция', 'Китай', 'Италия']  # Страны с турпакетом
not_visa_list = ['Абхазия', 'Азербайджан', 'Карелия']  # Страны безвиз
without_children_list = ['Непал', 'Тибет', 'Словакия']  # Страны для отдыха без детей
little_children = ['Адыгея', 'Крым', 'Архыз']  # Страны для отдыха с маленькими детьми
pay_for_children = ['Турция', 'Франция', 'Аргентина']  # Страны для семейного отдыха с платой за детей
not_pay_for_children = ['Австрия', 'Норвегия', 'Швейцария']  # Страны дети бесплатно

# Списки с корректными вариантами ответа
yes_no_list = ['да', 'нет']
cold_heat_list = ['холод', 'жара']
in_tur_list = ['индивидуально', 'тур-пакет']
sea_mountains_list = ['море', 'горы']
age_of_children = '0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18'.split()


def choix(list_of_countries):  # функция для предложения случайной страны
    c = ''  # переменная для контроля работы цикла
    while c.lower() != 'да':  # метод строки lower для защиты от заглавных букв
        if len(list_of_countries) <= 0:
            print('Извини, идеи закончились :(')  # исход
            break
        country = random.choice(list_of_countries)  # применение метода random.choice
        c = input(f'Что насчет {country}.\
 Хотели бы там побывать? Да или нет? ')
        if c.lower() == 'да':
            print(f'Отлично, я думаю, что {country} - это идеальный\
 вариант для вас.')  # исход
        elif c.lower() == 'нет':
            list_of_countries.remove(country)  # Удаляем страну из списка методом
            continue  # Если пользователь не хочет посетить данную страну, то предлагаем другую


def invalid_input(text, list_of_correct_input, q):  # Защита от неправильного ввода
    while text.lower() not in list_of_correct_input:  # while цикл
        print('Неверный ввод. Выберите вариант из списка.')
        print(*list_of_correct_input)
        text = input(q)
    return text


print('Привет, меня зовут TravelBot, я помогаю с выбором страны \
для отдыха!')  # Привествие пользователя

name = input('Как вас зовут?')

print(f'Очень приятно, {name}.\n Я задам вам несколько вопросов, \
постарайтесь отвечать не задумываясь. Пишите ответы строчными буквами без дополнительных символов')

question = 'Что вам нравится больше: холод или жара? '
begin = time.time()  # начало работы программы
a = input(question)  # Основной вопрос
a = invalid_input(a, cold_heat_list, question)
if a == 'холод':
    question = 'Вам нравится активный отдых? Да или нет? '
    b = input(question)
    b = invalid_input(b, yes_no_list, question)
    if b.lower() == 'да':
        for country in winter_active_countries:  # for цикл
            print(country, end=' ')  # Предлагаем пользователю случайную страну из списка
        print()
        print('Можете отправится в одну из этих стран')  # исход
    elif b.lower() == 'нет':
        print('Что насчет Гренландии? Хотели бы там побывать?')
        question = 'Да или нет? '
        c = input(question)
        c = invalid_input(c, yes_no_list, question)
        if c.lower() == 'нет':
            print('Присмотритесь к курортам России, например Байкал или\
 Архангельск')  # исход
        elif c.lower() == 'да':
            print('Отлично, я думаю, что это идеальный вариант для вас.')  # исход
elif a.lower() == 'жара':
    question = 'Вам нравится активный отдых? Да или нет? '
    b = input(question)
    b = invalid_input(b, yes_no_list, question)
    if b.lower() == 'да':
        question = 'Вас интересуют путешествия по историческим местам?\
 Да или нет? '
        m = input(question)
        m = invalid_input(m, yes_no_list, question)
        if m.lower() == 'нет':
            question = 'Вас интересует путешествие по экзотическим местам?\
 Да или нет? '
            o = input(question)
            o = invalid_input(o, yes_no_list, question)
            if o.lower() == 'да':
                question = 'Имеются ли прививки, необходимые для прибывания\
 в экзотических странах? Да или нет? '
                l = input(question)
                l = invalid_input(l, yes_no_list, question)
                if l.lower() == 'да':
                    choix(vac_list)  # используем функцию для случайной страны
                elif l.lower() == 'нет':
                    choix(not_vac_list)
            elif o.lower() == 'нет':
                question = 'Интересует активный отдых на море или в горах?\
 Море или горы? '
                l = input(question)
                l = invalid_input(l, sea_mountains_list, question)
                if l.lower() == 'море':
                    choix(sea_list)
                elif l.lower() == 'горы':
                    question = 'Имеется ли виза? Да или нет? '
                    m = input(question)
                    m = invalid_input(m, yes_no_list, question)
                    if m.lower() == 'нет':
                        choix(not_visa_list)
                    elif m.lower() == 'да':
                        question = 'Берете ли детей? Да или нет? '
                        k = input(question)
                        k = invalid_input(k, yes_no_list, question)
                        if k.lower() == 'нет':
                            choix(without_children_list)
                        elif k.lower() == 'да':
                            question = 'Сколько вашим детям лет? '
                            j = input(question)
                            j = invalid_input(j, age_of_children, question)
                            j = int(j)
                            if j > 3 and j < 18:  # сложное условие
                                i = input('Готовы ли вы заплатить за детей?\
 Да или нет? ')
                                if i.lower() == 'да':
                                    choix(pay_for_children)
                                elif i.lower() == 'нет':
                                    choix(not_pay_for_children)
                            elif j == 0 or j == 1 or j == 2 or j == 3:  # сложное условие
                                choix(little_children)
        elif m == 'да':
            question = 'Хотите путешествовать индивидуально или с тур-пакетом?\
 (Индивидуально или тур-пакет) '
            o = input(question)
            o = invalid_input(o, in_tur_list, question)
            if o == 'индивидуально':
                choix(individ_list)
            elif o == 'тур-пакет':
                choix(tur_list)
    elif b == 'нет':
        choix(passive_relax)
end = time.time()  # Конец работы программы
print(f'Я подсказал вам страну для отдыха за {end - begin} секунд\n Рад помочь!')  # Считаем время работы программы