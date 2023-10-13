# В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. 
# Ваша задача перевести его в one hot вид. 
# можете ли вы это сделать без get_dummies?

import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)

data = pd.DataFrame({'whoAmI': lst})
one_hot_data = pd.DataFrame()

unique_values = data['whoAmI'].unique()

for value in unique_values:
    column_name = 'is_' + value
    one_hot_data[column_name] = (data['whoAmI'] == value).astype(int)

data_encoded = pd.concat([data, one_hot_data], axis=1)

data_encoded.head()