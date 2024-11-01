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

