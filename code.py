import numpy as np
import pandas as pd
from collections import OrderedDict
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn import linear_model
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

def logistic_regression():

    tr = open('C:\\Users\\atinn\\Downloads', 'r')
    records = tr.readlines()
    tr.close()

    X = [[] for i in range(1460)]
    y = []
    for i in range(1, len(records)):
        for j in range(len(records[i].strip().split(',')) - 1):
            X[i - 1].append(int(records[i].strip().split(',')[j]))
        y.append(int(records[i].strip().split(',')[36]))

    lr = LogisticRegression()
    lr.fit(X, y)

    te = open('C:\\Users\\atinn\\Downloads', 'r')
    records1 = te.readlines()
    te.close()

    XX = [[] for i in range(1459)]
    yy = []
    for i in range(1, len(records1)):
        for j in range(len(records1[i].strip().split(','))):
            XX[i - 1].append(int(records1[i].strip().split(',')[j]))

    yy = lr.predict(XX)

    result = open('predictionresult.csv', 'w')
    print('Writing to File')
    result.write('House No,Predicted Price' + '\n')
    for i in range(len(yy)):
        result.write(str(i + 1) + ',' + str(yy[i]) + '\n')
    result.close()

    yyy = lr.predict(X)
    accuracy = accuracy_score(y, yyy) * 100
    print('model accuracy')
    print(accuracy)

def multiple_regression():
    
    df = pd.read_csv('C:\\Users\\atinn\\Downloads\\data.csv')

    totalArea = df[['TotalBsmtSF']+['GrLivArea']]
    halfBath = df[['BsmtHalfBath']+['HalfBath']]/2
    totalBath = df[['BsmtFullBath']+['FullBath']] + halfBath

    X = df[totalArea, totalBath, ['BedroomAbvGr']] #input data

    # print(X)

    y = df['SalePrice'] #input data

    regr = linear_model.LinearRegression()
    regr.fit(X, y)

    predict = regr.predict([[1500, 3, 4]])

    print(predict)

if __name__ == '__main__':
    '''call functions individually'''
