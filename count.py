# Import modules
import json
import pandas as pd
from collections import Counter
!pip install langid
import langid
!pip install langdetect
from langdetect import detect

# load the json objects, storing them in a variable 'data' and 'data2'
# change fr.json and fr_1.json by the path of your files
with open('fr.json', encoding="utf8") as json_file:
    data = json.load(json_file)
    
with open('fr_1.json', encoding="utf8") as json_file:
    data2 = json.load(json_file)
    
#Transform the data in a dataframe, display all columns to check if there is some nest
df1 = pd.json_normalize(data)
df2 = pd.json_normalize(data2)
pd.set_option('display.max_columns', None)

# Concatenate the two df
df = df1.merge(df2, right_index=True, left_index=True)

# Check if there is any NaN values/If False, there is none
df.isnull().values.any()

# Save the dataframe as a csv in order to transpose it later
df.to_csv('to_transpose.csv')

# Swap rows and columns, will be easier to count the words 
import csv
# Loading a csv containing the data, r for "reading", specify the encoding of the data
a = zip(*csv.reader(open("to_transpose.csv", "r", encoding="utf8")))
# create new csv with the "transpose", w for "writing"
csv.writer(open("data.csv", "w", encoding='utf8')).writerows(a)

# Import new csv with transpose
df_final = pd.read_csv("data.csv")

# rename the columns
df_final = df_final.rename(columns=({'Unnamed: 0': 'category', '0': 'to_translate'}))

# Cleaning the data, uppercase become lowercase, and some regex to replace characters that are not strings
df_final = df_final.apply(lambda x: x.astype(str).str.lower())
df_final = df_final.replace('\d+', '', regex = True)
df_final = df_final.replace('[^\w\s\+]', '', regex = True)

# Add a column with the count of each word in the dataframe
df_final['count'] = df_final['to_translate'].str.split().map(len)
df_final.sample(5)

# Get the number of words you have
print("You have",
      df_final['count'].sum(), "words.")

# Check which words are fr // NOT ACCURATE
ids_langid = df_final['to_translate'].apply(langid.classify)

langs = ids_langid.apply(lambda tuple: tuple[0])
print("Percent of data in French (estimated):")
print((sum(langs=="fr")/len(langs))*100)

for index, row in df_final['to_translate'].iteritems():
    lang = detect(row) #detecting each row
    df.loc[index, 'language'] = lang

# will display the unique values of the column language to see which language we have
df_final['language'].unique()