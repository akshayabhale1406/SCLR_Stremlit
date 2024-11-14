# THIS code is a Linear Regression Model that predicts car prices for CARS24

print("This model has started to work now!!")

print("Let's start!!!!")

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm
from sklearn.preprocessing import MinMaxScaler
df = pd.readcsv("cars24-car-price-cleaned.csv")
df.head()

df["make"] = df.groupby(["make"])["selling_price"].transform("mean")
df["model'] = df.groupby(["model']["selling_price"].transform("mean")

minMAXscaler = MinMaxScaler()

df1=pd.DataFrame(min_max_scaler.fit_transform(df[['year', 'km_driven', 'mileage', 'engine', 'max_power',
       'age', 'make', 'model', 'Individual', 'Trustmark Dealer', 'Diesel',
       'Electric', 'LPG', 'Petrol', 'Manual', '5', '>5']]),columns=['year', 'km_driven', 'mileage', 'engine', 'max_power',
       'age', 'make', 'model', 'Individual', 'Trustmark Dealer', 'Diesel',
       'Electric', 'LPG', 'Petrol', 'Manual', '5', '>5'])
df1["selling_price"]=df["selling_price"]

print("hello!!!!!!!")

df1
