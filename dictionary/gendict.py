"""
Generate Dictionary
Implement a function which takes integer number (n) as a parameter and returns dictionary with keys from 1 to n and values are square of the numbers from 1 to n.

Example

generate_dictionary(5)

Output

{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
#
"""
def generate_dictionary(n):
  dict_for_sq = dict()
  for num in range(1,n+1):
      dict_for_sq[num] = num*num
  return dict_for_sq

opt=generate_dictionary(5)

print(opt)


