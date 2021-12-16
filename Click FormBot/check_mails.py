from pywinauto import application
from random import randint

mails = []
with open('real_mails.txt') as f:
    mails = f.read().split('\n')
# mails = mails[:-1]

i = randint(0,len(mails))
email = mails[i]

print('Всего адресов в списке: ', len(mails))

mails = list(set(mails))
print('Уникальных адресов в списке: ',len(mails))
mails.sort()

# N= 10
# mails = mails[N:]


# with open('clear_mails.txt', 'w') as f:
#     mails = map(lambda x: x + '\n', mails)
#     f.writelines(mails)
