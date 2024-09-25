"""
Multiply Dictionary Items
Implement a function which takes dictionary as a parameter and returns multiplication of values of this dictionary.

Example
my_dict = {"One" : 1, "Two" : 2, "Three" : 3, "Four" : 4}
multiply_values(my_dict)
Output

24
"""
def multiply_values(di):
  val = 1
  for key in di:
      val = val*di[key]
  return val

my_dict = {"One" : 1, "Two" : 2, "Three" : 3, "Four" : 4}
opt =multiply_values(my_dict)
print(opt)
