# Module
import json

# Open the json file and storing it as a dictionary in "data"
# Change 'fr.json' by the path to your file
with open('fr.json', encoding='utf8') as json_file:
    data = json.load(json_file)
    
# Loading a second file
with open('fr (1).json', encoding='utf8') as json_file:
    data2 = json.load(json_file)
    
# Define a function "word_count" which takes "data" as argument
#  RECURSIVE
def word_count(data):
    # Turning the local variable "total" as a global variable
    global total
    # For Loop that will iterrate in the keys of the data file
    for key in data.keys():
        # "isinstance" will check if the object (here: data[key]) is the type we passed as argument (here: dict)
        if isinstance(data[key], dict):
            # Calling the function inside itself so it will iterrate in all the nest and get all values
            word_count(data[key])
        else:
            # storing the number of words in the 'total' variable (split cut the phrases into words and len takes the number of splitted words)
            total += len(data[key].split())

    return total

total = 0
# Call the function for each file and print the last one in order to obtain the final number
word_count(data)
print(word_count(data2))