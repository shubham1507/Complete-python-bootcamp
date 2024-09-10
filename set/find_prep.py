"""
Find Preposition
Implement a function which takes a quote as a parameter to find out which given prepositions have been used in the quote. 
The function should return the set of prepositions that are used in the quote.

Example

quote = """Success is no accident. It is hard work, perseverance, learning, studying, sacrifice and most of all, love of what you are doing or learning to do."""
prep = {"as", "but", "by", "for", "in", "of", "on", "to", "with"}
 
find_prep(quote)
Output

{'of', 'to'}

"""

prep = {"as", "but", "by", "for", "in", "of", "on", "to", "with"}

quote = """Success is no accident. It is hard work, perseverance, learning, studying, sacrifice and most of all, love of what you are doing or learning to do."""


def find_prep(quote):
    found_prep = set()
    quote = set(quote.split(" "))
    found_prep = quote.intersection(prep)
    return found_prep
    
print(find_prep(quote))

