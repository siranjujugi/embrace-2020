import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle
import random

with open('test.csv', 'w') as f:
    print("YearsExperience,Salary", file=f)

    years = 0
    salary = 40000

    for i in range(50):
        print(f"{years:.1f},{salary:.2f}", file=f)
        years += random.randrange(2, 7, 1)/10
        salary *= (1 + random.randrange(1, 6)/100)

dataset = pd.read_csv('test.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.33, random_state = 0)

regressor = LinearRegression()
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)

pickle.dump(regressor, open('model.pkl','wb'))
