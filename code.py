import numpy as np
import pandas as pd
import os
import math

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
print(data_set.sample(5))

def describe_data():
    # print(data_set.describe(include='all'))
    print(data_set.sample(5))

def median():

    values = []

    for index, row in data_set.iterrows():

        total_sqft = row['TotalBsmtSF'] + row['GrLivArea']

        if row['Neighborhood'] in values:
            pass
        else:
            values += row['Neighborhood']

        if row['YrSold'] == 2006 and total_sqft >= total_sqft:
            # print(index, row['Neighborhood'], row['YrSold'], row['TotalBsmtSF'] + row['GrLivArea'], row['SalePrice'])

        else:
            pass

math


if __name__ == '__main__':
    iterate()


