import numpy as np 
import pandas as pd

# to display all columns without truncations
pd.set_option('display.max_columns', None)

# extract and read data with pandas 
# we use the .read_csv() from the pandas library

netflix_data = pd.read_csv('netflix.csv')


# show the first five rows
# we use the .head()

print(netflix_data.head(5))

# show the last five rows
# we use the .tail()

print(netflix_data.tail(5))

# show the number of rows and columns
# we use .shape

print(netflix_data.shape)

# checking for inconsistent values
print(netflix_data.isnull().values.any())
print('\n')

# listing columns with nan values 
columns_nan = netflix_data.columns[netflix_data.isnull().any()].tolist()


print(columns_nan)
print("\n")

# printing the names of columns
print(netflix_data.columns.tolist())
print("\n")

# cleaning \ removing inconsistent values
netflix_data.replace('...', pd.NA)

netflix_data.dropna(subset=['director', 'cast', 'country', 'date_added', 'rating', 'duration'], inplace=True)

print(netflix_data.isnull().values.any())
print("\n")

# printing the datatypes of columns
print(netflix_data.dtypes)
print("\n")

# to give you the data type within a data frame
print(netflix_data.info())
print("\n")

# to summarize the data
print(netflix_data.describe())
print("\n")

# find the id and director of house of cards
h_o_c = netflix_data.loc[netflix_data['title'] == 'House of cards',
                         ['show_id', 'director']]

print(h_o_c)
print("\n")

# find the different movies released 2010


# check for the values in a particular column
print(netflix_data['title'].unique())
print(netflix_data['release_year'].unique())

yr2010 = netflix_data.loc[netflix_data['release_year'] == 2010]
movies2010 = yr2010[yr2010['type'] == 'Movie']

# print(yr2010)
# print("\n")

print(movies2010)
print("\n")

argent = netflix_data[netflix_data['country'] == 'Argentina' & netflix_data['type'] == 'TV Show']
