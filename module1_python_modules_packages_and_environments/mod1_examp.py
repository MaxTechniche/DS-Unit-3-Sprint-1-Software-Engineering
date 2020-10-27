""" helper function for Data science """

#importing libraries for function into the package
import pandas as pd
import numpy as np 

# define a null count function
def null_count(df):
    count = df.isnull().sum()
    return count

#create a date split function.
def date_split(df2):
    df2['col'] = df2.select_dtypes('datetime')
    df2['year']=df2['col'].dt.year
    df2['month']=df2['col'].dt.month
    df2['day']=df2['col'].dt.day
    df2=df2.drop(columns='col')
    return df2