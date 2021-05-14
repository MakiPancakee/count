# Import modules
import json
import pandas as pd

# load the json objects, storing them in a variable 'data' and 'data2'
with open('fr.json', encoding="utf8") as json_file:
    data = json.load(json_file)
    
with open('fr_1.json', encoding="utf8") as json_file:
    data2 = json.load(json_file)

def get_the_key(d):
    stack = list(d.items())
    
    #       Counting the words 
    def word_count(str):
        words = str.split()
        counts = 0
        
        for word in words:
            counts += 1

        return counts, words
    


    while stack:
        k, v = stack.pop()
#         
        if isinstance(v, dict):
            stack.extend(v.items())
            
#             Remove the non-alphabetical characters (like {0})
            def nospecialchar(text):
                import re
                text = re.sub(r'[^A-Za-z0-9 ]+', '', text)
                return text
            
        else:
            print(word_count(" %s" % (nospecialchar(v))))
           
            

get_the_key(data)
get_the_key(data2)