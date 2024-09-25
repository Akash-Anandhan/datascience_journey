import pandas as pd
import numpy as np
ser=[10,20,30,40,50]
df=pd.Series(ser)
print(df)

df =pd.read_csv("MostPopularProgrammingLanguages.csv")
#printing the whole datset
print(df.to_string())
print("--------------------------------------------------------")
#printing head values of the dataset
print(df.head().to_string())
print("--------------------------------------------------------")
#printing the min alues of each columns
print(df.min())
print("--------------------------------------------------------")
#printing the max elements in each column
print(df.max())
print("--------------------------------------------------------")
#print the null elements of each column
print(df.isnull())
print("--------------------------------------------------------")
#printing the sum of null elements in each row
print(df.isnull().sum())
print("--------------------------------------------------------")
#clear all the null elements in the dataset
df.dropna()


column_name = "Python Worldwide(%)"
#converting the colum in the csv file to array using numpy
arr = df[column_name].to_numpy()


#printing the minimum value using numpy
min_value = np.min(arr)
print("minimum value in the python worldwide column is ",min_value)
print("--------------------------------------------------------")
#printing the maximum element using the numpy with the converted array from colum
print(np.max(arr))