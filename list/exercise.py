ls=[42, 67, 30, 52, 46, 66, 61, 2, 21, 30]
ls[0] = ls[-1]

#print(" interchange first and last elements in a list \n",ls)

#--------------------------------
test_list = ['Gfg', 'is', 'best', 'for', 'Geeks']

# printing original lists
print("The original list is : " + str(test_list))
    
#Character Swap in Python Strings
res=[ sub.replace('G', '-').replace('i', 'I').replace('f','F')    for sub in test_list]

# printing result 
#print ("List after performing character swaps : " + str(res))

#--------------------------------
#clear a list in Python

test_list.clear()

#------------Reversing a List in Python-----------------

ls.reverse()
print(ls)
#OR
print(ls[::-1])

#----------------Python | Cloning or Copying a list

def Clonning(p_ls):
    ls_copy=ls[:]
    return ls_copy
    
ls2=Clonning(ls)
print(ls2)

#OR
import copy

li3=copy.copy(ls)
print(li3)

#-----------------count occurances-------

a = [1, 3, 2, 6, 3, 2, 8, 2, 9, 2, 7, 3]

# Count occurrences of 2
print(a.count(2))

# Count occurrences of 3
print(a.count(3))

#----------------sum and avg of list

import statistics

print(sum(ls))
print(statistics.mean(ls))

