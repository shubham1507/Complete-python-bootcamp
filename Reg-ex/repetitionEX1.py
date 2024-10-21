""
Repetition EX1
Write a Python function that matches a string that has an 'A' followed by zero or more 'B's.

Input

text_match("A")
text_match("ABC")
text_match("ABBC")
Output

Matched
Matched
Matched
"""

import re

def text_match(text):
    regex_pattern=re.compile(r'AB*')
    mo=regex_pattern.search(text)
    
    if mo == None:
        return 'Not matched'
    else:
        return 'Matched'
        
print(text_match('ABABBBBAABB'))
