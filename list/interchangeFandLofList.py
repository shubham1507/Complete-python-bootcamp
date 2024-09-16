#Python program to interchange first and last elements in a list

my_list = [1, 2, 3, 4, 5]
#my_list[0],my_list[-1]=my_list[-1],my_list[0]
#print(my_list)

#Interchange first and last elements using Temporary Value

def swapList(ls):
    size=len(ls)
    
    temp=ls[0]
    ls[0]=ls[size-1]
    ls[size-1]=temp
    
    return ls
    
#print(swapList(my_list))

#How To Find the Length of a List in Python

counter=0
for i in my_list:
    counter = counter+1
    
#print("The len of list: "+str(counter))

le=sum(1 for _ in my_list)
#print("The len of list using comprehension: "+str(le))


def ls_using_rec(ls):
    if not ls:
        return 0
    return 1 + ls_using_rec(ls[1:])
    
#print("The len of list using recursion: ", ls_using_rec(my_li))
s = 0
for i, a in enumerate(my_list):
    s+=1
print("The len of list using enumerate: "+str(s))
