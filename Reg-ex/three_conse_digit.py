"""
Find Three Consecutive Digits
Implement a function which takes a string as a parameter to find out whether there is three consecutive digits or not. If there is three consecutive digits, the function will return first occurence otherwise 'Not found'.

Example

text = 'My phone number is: 234-456-8765'
find_three_con(text)
Output

234
"""

import re

def find_three_con(text):
    matching_obj=re.search('\d\d\d',text)
    
    if matching_obj=='None':
        return 'Not found'
    else:
        return matching_obj.group()
        
text = 'My phone number is: 234-456-8765'

print(find_three_con(text))


    
    
