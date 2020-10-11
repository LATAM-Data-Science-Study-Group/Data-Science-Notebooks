import pandas as pd

df = pd.read_csv('pokemon_data.csv')
print(df)

#df_xlsx = pd.read_excel('pokemon_data.xlsx')
#print(df_xlsx.head(3))

#df = pd.read_csv('pokemon_data.txt', delimiter='\t')
#print(df)

#df['HP'] #select a series/column from a dataset


ufo = pd.read_csv('ufo-sightings.csv')
print(ufo)


movies = pd.read_csv('http://bit.ly/imdbratings')
print(movies)


orders = pd.read_table('http://bit.ly/chiporders')
print(orders)


drinks = pd.read_csv('http://bit.ly/drinksbycountry')
print(drinks)


print(movies.head()) # examine the first 5 rows


print(ufo.tail()) # examine the last 5 rows


df.shape   # Shape of the dataset as matrix


ufo.info()


movies.dtypes


df.describe(include='all')     #calculate summary statistics


ufo.columns


ufo['City']        # select the 'City' Series using bracket notation
#ufo.City          # or equivalently, use dot notation


movies.genre.nunique()


movies.genre.unique()


# loc  - [index/bool,'column names']
# iloc - [index/bool,index position]  


# row 0, all columns
ufo.loc[1, :]


# rows 0 and 1 and 2, all columns
ufo.loc[[0, 1, 2], :]


# rows 0 through 2 (inclusive), all columns
ufo.loc[0:2, :]


# rows 0 through 2 (inclusive), columns 'City' and 'State'
ufo.loc[0:2, ['City', 'State']]


# rows 0 through 2 (inclusive), columns 'City' through 'State' (inclusive)
ufo.loc[0:2, 'City':'State']


# rows in positions 0 and 1, columns in positions 0 and 3
ufo.iloc[[0, 1], [0, 3]]


# rows in positions 0 through 2 (exclusive), columns in positions 0 through 4 (exclusive)
ufo.iloc[0:2, 0:4]


# rows in positions 0 through 2 (exclusive), all columns
ufo.iloc[0:2, :]


# read a specific column
df.columns 
print(df.iloc[2,1])



# sort the 'title' Series in ascending order (returns a Series)
movies.title.sort_values().head()

# sort in descending order instead
#movies.title.sort_values(ascending=False).head()


movies.sort_values('title', ascending=False).head()


df.sort_values(['Type 1', 'HP'], ascending=[False,True])


movies.sort_values(['star_rating', 'duration','content_rating'],ascending=[False,True,True]).head(10)


# Create a new series inside the orignal series

ufo['Location'] = ufo.City + ', ' + ufo.State     # Create a new series inside the orignal series
ufo.head()

# df = df.drop(columns=['Total'])

#df['Total'] = df.iloc[:, 4:10].sum(axis=1)

#cols = list(df.columns)
#df = df[cols[0:4] + [cols[-1]]+cols[4:12]]

#df.head(5)


df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']
df.head()


# rename a column

df.rename(columns={'Name':'Pokemon'}, inplace = True )  
df.head()


# remove columns

ufo.drop(['City', 'State'], axis=1, inplace=True)       # Column axis=1  &  Row axis=0
ufo.head()


# df.to_csv('modified.csv', index=False)

#df.to_excel('modified.xlsx', index=False)

df.to_csv('modified.txt', index=False, sep='\t')





movies.duration


movies.duration >= 200


movies[movies.duration >= 200] 


movies[movies.duration >= 200].title #spicifying movies titles only which are greater than 200 minutes


movies[(movies.duration >=200) & (movies.genre == 'Drama')]


movies[(movies.duration >=200) | (movies.genre == 'Drama')].head()


movies[(movies.genre == 'Crime') | (movies.genre == 'Drama') | (movies.genre == 'Action')].head(10)


new_df = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 70)]

#new_df.reset_index(drop=True, inplace=True)

new_df

#new_df.to_csv('filtered.csv')



orders.item_name.str.contains('Chicken').head()


orders[orders.item_name.str.contains('Chicken')].head()  # Filtering data with string 'Chicken'


# create a DataFrame only containing movies with a high 'star_rating'
top_movies = movies.loc[movies.star_rating >= 9, :]
top_movies


# 'isnull' returns a DataFrame of booleans (True if missing, False if not missing)

ufo.isnull().tail()
#ufo.isnull().sum()


# 'nonnull' returns the opposite of 'isnull' (True if not missing, False if missing)

ufo.notnull().tail()
#ufo.notnull().sum()


# use the 'isnull' Series method to filter the DataFrame rows

ufo[ufo.City.isnull()].head()


ufo.dropna(how='any')          # if 'any' values are missing in a row, then drop that row
#ufo.dropna(how='any').shape


ufo.dropna(how='all')       # if 'all' values are missing in a row, then drop that row (none are dropped in this case)
#ufo.dropna(how='all').shape


# if 'any' values are missing in a row (considering only 'City' and 'Shape Reported'), then drop that row

ufo.dropna(subset=['City', 'Shape Reported'], how='any').shape


# if 'all' values are missing in a row (considering only 'City' and 'Shape Reported'), then drop that row

ufo.dropna(subset=['City', 'Shape Reported'], how='all').shape


ufo['Shape Reported'].value_counts()               # 'value_counts' does not include missing values by default
#ufo['Shape Reported'].value_counts(dropna=False)   # explicitly include missing values


ufo['Shape Reported'].fillna(value='VARIOUS', inplace=True)   # fill in missing values with a specified value
#ufo['Shape Reported'].value_counts().head()                   # confirm that the missing values were filled in


# calculate the mean beer servings for each continent
drinks.groupby('continent').describe()['beer_servings']


# other aggregation functions (such as 'max') can also be used with groupby
drinks.groupby('continent').beer_servings.max()


import matplotlib.pyplot as plt
get_ipython().run_line_magic("matplotlib", " inline")


drinks.groupby('continent').mean().plot(kind='bar')


# replace all of the column names by overwriting the 'columns' attribute

ufo_cols = ['city', 'colors_reported', 'shape_reported', 'state', 'time','Location']
ufo.columns = ufo_cols
ufo.columns


# replace all spaces with underscores in the column names by using the 'str.replace' method

ufo.columns = ufo.columns.str.replace(' ', '_')
ufo.columns


# replace the column names during the file reading process by using the 'names' parameter

ufo = pd.read_csv('ufo.csv', header=0, names=ufo_cols)
ufo.columns



