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

#--------------Sum of number digits in List

res=list(map(lambda number: sum(int(digit) for digit in str(number)),ls))
print(res)
#------2nd largest and 3rd smallest, even, odd, -ve, +ve number

print("The 2nd largest number in list ls \n",sorted(set(ls))[-2])
print("The third_smallest number in list ls \n",sorted(set(ls))[2])
print("The even numbers in list ls \n", [even for even in ls if even%2==0])
print("The odd numbers in list ls \n", [odd for odd in ls if odd%2!=0])

list1 = [-10, -21, -4, 45, -66, 93]


pos_res=[num for num in list1 if num>=0]
neg_res=[num for num in list1 if num<0]
print("The +ve numbers are :",pos_res)
print("The -ve numbers are :",neg_res)
