from pywinauto import application
from pywinauto.keyboard import send_keys
import time
from random import choice, choices, randint

with open('male_names.txt') as f:
    male_names = f.read().split('\n')

with open('male_surnames.txt') as f:
    male_surnames = f.read().split('\n')

with open('male_patronymics.txt') as f:
    male_patronymics = f.read().split('\n')

with open('female_names.txt') as f:
    female_names = f.read().split('\n')

with open('female_surnames.txt') as f:
    female_surnames = f.read().split('\n')

with open('female_patronymics.txt') as f:
    female_patronymics = f.read().split('\n')

with open('real_mails.txt') as f:
    all_mails = f.read().split('\n')

names = []
surnames = []
patronymics = []
cats = []
kid_cats = []
kid_descs = []
sexs = []
ages = []
question_nums = []

td = 3
N = 3
emails = choices(all_mails, k=N)

for n in range(N):
    sex = choice(['М', 'М', 'М', 'Ж', 'Ж', 'Ж', 'Ж', 'Ж'])
    sexs.append(sex)
    age = randint(17, 60)
    ages.append(age)
    if sex == 'М':
        n1 = randint(0, len(male_names)-1)
        name = male_names[n1]
        n2 = randint(0, len(male_surnames)-1)
        surname = male_surnames[n2]
        n3 = randint(0, len(male_patronymics)-1)
        patronymic = male_patronymics[n3]
    if sex == 'Ж':
        n1 = randint(0, len(female_names)-1)
        name = female_names[n1]
        n2 = randint(0, len(female_surnames)-1)
        surname = female_surnames[n2]
        n3 = randint(0, len(female_patronymics)-1)
        patronymic = female_patronymics[n3]
    names.append(name)
    surnames.append(surname)
    patronymics.append(patronymic)
    if age < 18:
        cat = 1
        kid_cat = 1
    elif age >= 18 and age <= 25:
        cat = 2
        kid_cat = choice((1, 2))
    elif age >= 26 and age <= 35:
        cat = 3
        kid_cat = choice((1, 2, 3, 4))
    elif age >= 36 and age <= 45:
        cat = 4
        kid_cat = choice((2, 3, 4))
    elif age >= 46 and age <= 55:
        cat = 5
        kid_cat = choice((3, 4))
    else:
        cat = 6
        kid_cat = choice((3, 4))

    cats.append(cat)
    kid_cats.append(kid_cat)
    if kid_cat == 1:
        kid_desc = 'Ребёнок дошкольного возраста'
        question_num = randint(1,15)
    elif kid_cat == 2:
        kid_desc = 'Ребёнок младшекого школьного возраста (1 - 4 класс)'
        question_num = randint(1,20)
    elif kid_cat == 3:
        kid_desc = 'Ребёнок младшего подросткового возраста (5 - 7 класс)'
        question_num = randint(1,20)
    else:
        kid_desc = 'Ребёнок старшего подросткового возраста (8 класс и старше)'
        question_num = randint(1,20)
    kid_descs.append(kid_desc)
    question_nums.append(question_num)


path = 'C:\Program Files\Google\Chrome\Application'
web = 'https://forms.office.com/r/5wjmhGn7SY'


app = application.Application().start(path + '\chrome.exe ' + web)
time.sleep(10)

for n in range(N):
    # старт заполнения
    send_keys('{TAB 2}' + emails[n], with_spaces=True)
    send_keys('{TAB}', with_spaces=True)
    send_keys('{ENTER}', with_spaces=True)
    time.sleep(td)
    send_keys('{TAB 2}' + surnames[n], with_spaces=True)
    time.sleep(td / 10)
    send_keys('{TAB}' + names[n], with_spaces=True)
    time.sleep(td / 10)
    send_keys('{TAB}' + patronymics[n], with_spaces=True)
    time.sleep(td / 10)

    send_keys('{TAB}', with_spaces=True)
    time.sleep(td / 10)
    send_keys('{SPACE}', with_spaces=True)
    time.sleep(td / 5)
    command = '{DOWN ' + str(cats[n] - 1) + '}'
    send_keys(command, with_spaces=True)

    send_keys('{TAB}', with_spaces=True)
    time.sleep(td / 10)
    send_keys('{SPACE}', with_spaces=True)
    time.sleep(td / 5)
    command = '{DOWN ' + str(kid_cats[n] - 1) + '}'
    send_keys(command, with_spaces=True)

    send_keys('{TAB 2}', with_spaces=True)
    time.sleep(td / 5)
    send_keys('{ENTER}', with_spaces=True)

    send_keys('{TAB 2}', with_spaces=True)
    time.sleep(td / 10)
    send_keys('{SPACE}', with_spaces=True)
    time.sleep(td / 5)
    command = '{DOWN ' + str(question_nums[n] - 1) + '}'
    send_keys(command, with_spaces=True)

    send_keys('{TAB 2}', with_spaces=True)
    time.sleep(td / 5)
    send_keys('{ENTER}', with_spaces=True)

    send_keys('{TAB 2}', with_spaces=True)
    time.sleep(td / 5)
    send_keys('{SPACE}', with_spaces=True)
    time.sleep(td / 10)
    send_keys('{TAB 3'
              '}', with_spaces=True)
    time.sleep(td / 5)

    send_keys('{ENTER}', with_spaces=True)
    time.sleep(5*td)
    send_keys('{ENTER}', with_spaces=True)
    # конец заполнения

for n in range(N):
    print('Почта: ', emails[n])
    print('Пол: ', sexs[n])
    print('Фамилия: ', surnames[n])
    print('Имя: ', names[n])
    print('Отчество: ', patronymics[n])
    print('Возраст: {} (категория №{})'.format(ages[n], cats[n]))
    print(kid_descs[n])
    print('Вопрос #', question_nums[n])
    print()