"""

Repetition EX2
Write a Python function that matches a string that 
has an 'A' followed by TWO to THREE 'B'.

Input

text_match("A")
text_match("ABC")
text_match("ABBC")
Output

Not matched
Not matched
Matched
"""

import re

def text_match(text):
    regex=re.compile(r'AB{2,3}')
    mo=regex.search(text)
    if mo == None:
        return 'Not matched'
    else:
        return 'matched'
        
print(text_match('ABBC'))
