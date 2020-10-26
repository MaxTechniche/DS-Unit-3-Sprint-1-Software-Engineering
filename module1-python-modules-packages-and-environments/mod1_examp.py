""" helper function for Data science """

#importing libraries for function into the package
import pandas as pd
import numpy as np 

# define a null count function
def null_count(df):
    count = df.isnull().sum()
    return count

#create a date split function.
def date_split(df):
    df['col'] = df.select_dtypes('datetime')
    df['year']=df['col'].dt.year
    df['month']=df['col'].dt.month
    df['day']=df['col'].dt.day
    df=df.drop(columns='col')
    return df