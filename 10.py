import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)

data = pd.DataFrame({'whoAmI': lst})
print('Исходный DataFrame:\n', data.head())

# создаем список уникальных значений в столбце "whoAmI"
unique_vals = data['whoAmI'].unique()

# создаем пустой DataFrame с столбцами для каждого уникального значения
one_hot_data = pd.DataFrame(columns=unique_vals)

# заполняем столбцы значениями 0 или 1 в зависимости от того, соответствует ли значение в строке значению в столбце "whoAmI"
for val in unique_vals:
    one_hot_data[val] = (data['whoAmI'] == val).astype(int)

print('Преобразованный в one-hot формат DataFrame:\n', one_hot_data.head(