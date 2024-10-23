"""
Write a Python function that matches given words in the text and count them.

Words: Love, love, Lovers, lovers

Text: Lovers in love

Lovers in love

Love, love, love, love, love

Love, love, love, love, love

Love, love, love, love, love

Love, love, love, love, love

Lovers loving love just like these lovers are loving love in love

Lovers loving love just like these lovers are loving love in love

Input

text_match(text)
Output

34
"""

import re

def text_match(text):
    regex=re.compile(r'(L|l)ove(rs)?')
    mo_list=regex.findall(text)
    return len(mo_list)
    
