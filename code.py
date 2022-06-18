import numpy as np
import pandas as pd
from collections import OrderedDict
import os

# set options
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_rows', None)

data_set = pd.read_csv('C:\\Users\\atinn\\Downloads\\data.csv')

# used to read the files
def test_path():
    for dirname, _, filenames in os.walk('C:\\Users\\atinn\\Downloads'):
        for filename in filenames:
            print(os.path.join(dirname, filename))

# print the sample of the data
# print(data_set.sample(5))

def describe_data():
    print(data_set.describe(include='all'))
    #print(data_set.sample(5))

def quick_stats():

    values = OrderedDict()

    for index, row in data_set.iterrows():

        total_sqft = row['TotalBsmtSF'] + row['GrLivArea']

        if row['YrSold'] == 2006 and total_sqft >= 2000:
            # print(index, row['Neighborhood'], row['YrSold'], row['TotalBsmtSF'] + row['GrLivArea'], row['SalePrice'])
            if row['Neighborhood'] not in values.keys():
                # add key and create list
                values[row['Neighborhood']] = []
            values[row['Neighborhood']].append(row['SalePrice'])
        else:
            pass

    for key, value in values.items():

        s = pd.Series(value)
        print(f'{key}:')
        print(f'{s.describe()}')

def seasonality():

    values = OrderedDict()

    for index, row in data_set.iterrows():
        if (row['MoSold'], row['YrSold']) not in values.keys():
            values[(row['MoSold'], row['YrSold'])] = 1
        else:
            values[(row['MoSold'], row['YrSold'])] += 1

    for key, value in values.items():
        print(key, value)


if __name__ == '__main__':
    #quick_stats()
    seasonality()


