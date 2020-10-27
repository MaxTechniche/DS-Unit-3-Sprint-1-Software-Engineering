""" helper function for Data science """

#importing libraries for function into the package
import pandas as pd
import numpy as np 

class MyDataFrame:
    def __init__(self, df):
        self.df = df

    # define a null count function
    def nulls(self):
        count = self.df.isnull().sum()
        return count

    #create a date split function.
    def date_split(self):
        self.df['col'] = self.df.select_dtypes('datetime')
        self.df['year'] = self.df['col'].dt.year
        self.df['month'] = self.df['col'].dt.month
        self.df['day'] = self.df['col'].dt.day
        self.df = self.df.drop(columns='col')
        return self.df