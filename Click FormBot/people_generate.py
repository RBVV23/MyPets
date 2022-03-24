from pywinauto import application
from random import choice, choices, randint

with open('little_mails.txt') as f:
    all_mails = f.read().split('\n')

i = randint(0, len(all_mails))
email = all_mails[i]

with open('male_names.txt') as f:
    male_names = f.read().split('\n')

print('МУЖСКИЕ ИМЕНА:')
print(male_names)
print('\tИтого:', len(male_names))

with open('male_surnames.txt') as f:
    male_surnames = f.read().split('\n')

print('МУЖСКИЕ ФАМИЛИИ:')
print(male_surnames)
print('\tИтого:', len(male_surnames))

with open('male_patronymics.txt') as f:
    male_patronymics = f.read().split('\n')

print('МУЖСКИЕ ОТЧЕСТВА:')
print(male_patronymics)
print('\tИтого:', len(male_patronymics))

with open('female_names.txt') as f:
    female_names = f.read().split('\n')

print('ЖЕНСКИЕ ИМЕНА:')
print(female_names)
print('\tИтого:', len(female_names))

with open('female_surnames.txt') as f:
    female_surnames = f.read().split('\n')

print('ЖЕНСКИЕ ФАМИЛИИ:')
print(female_surnames)
print('\tИтого:', len(female_surnames))

with open('female_patronymics.txt') as f:
    female_patronymics = f.read().split('\n')

print('ЖЕНСКИЕ ОТЧЕСТВА:')
print(female_patronymics)
print('\tИтого:', len(female_patronymics))

# with open('female_names.txt') as f:
#     names = f.read().split('\n')
#
# # names = names[:]
# # names = names + names2
# names = list(set(names))
# #
# names.sort()
# # names = names[1:]
# print(names)
# print(len(names))
#
# # names = list(map(lambda x: x[1:], names))
# # names = list(map(lambda x: x[:-1], names))
#
# print(names)
# print(len(names))
#
# with open('female_names.txt', 'w') as f:
#     names = map(lambda x: x + '\n', names)
#     f.writelines(names)

names = []
surnames = []
patronymics = []
cats = []
kid_cats = []
kid_descs = []
sexs = []
ages = []
question_nums = []

N = 9
emails = choices(all_mails, k=N)
for n in range(N):
    sex = choice(['М', 'М', 'М', 'Ж', 'Ж', 'Ж', 'Ж', 'Ж'])
    sexs.append(sex)
    age = randint(17, 60)
    ages.append(age)
    if sex == 'М':
        n1 = randint(0, len(male_names)-1)
        name = male_names[n1]
        # print(n1)
        n2 = randint(0, len(male_surnames)-1)
        surname = male_surnames[n2]
        # print(n2)
        n3 = randint(0, len(male_patronymics)-1)
        patronymic = male_patronymics[n3]
        # print(n3)
    if sex == 'Ж':
        n1 = randint(0, len(female_names)-1)
        name = female_names[n1]
        # print(n1)
        n2 = randint(0, len(female_surnames)-1)
        surname = female_surnames[n2]
        # print(n2)
        n3 = randint(0, len(female_patronymics)-1)
        patronymic = female_patronymics[n3]
        # print(n3)
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