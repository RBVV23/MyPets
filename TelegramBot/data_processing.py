
my_columns = ['user_id',
              'name',
              'surname',
              'age']

df = pd.DataFrame(columns = my_columns)
# df.append(index='Test', ['0000', 'Имя', 'Фамилия', '15'])
df.loc['test1'] = ['0000', 'Имя', 'Фамилия', int(15)]
df.loc['test2'] = ['0001', 'Имя2', 'Фамилия2', int(12)]
print(df.info())