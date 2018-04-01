import pandas as pd
import os

def common_name(year):
    data_path = f'{os.getcwd()}\\names\\'
    names = pd.read_csv(data_path + 'yob' + str(year) + '.txt', names=['name', 'gender', 'count'])
    return names

def most_common_name(years_list):
    data = list(map(common_name, years_list))
    data = pd.concat(data)
    data = (data.groupby('name').sum())
    most_common_name = data.sort_values(by=['count'], ascending=False).head(3)
    return most_common_name.reset_index()['name'].values

years = [1900, 1950, 2000]
print(most_common_name(years))
