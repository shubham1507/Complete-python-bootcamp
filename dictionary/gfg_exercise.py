
#find the sum of all items in a dictionary
dict = {'a': 100, 'b': 200, 'c': 300}

def sumDict(mydict):
    ls=[]
    for i in mydict:
        ls.append(mydict[i])
    final=sum(ls)
    
    return final
    
print("sum of itemin dict ",sumDict(dict))

#Finding the Size of the Dictionary in Bytes

import sys

dic1 = {"A": 1, "B": 2, "C": 3}
dic2 = {"Geek1": "Raju", "Geek2": "Nikhil", "Geek3": "Deepanshu"}
dic3 = {1: "Lion", 2: "Tiger", 3: "Fox", 4: "Wolf"}
 
 
 print("size of dic1: "+str(sys.getsizeof(dic1))+" bytes")
