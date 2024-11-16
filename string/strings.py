# reverse the sentense

string = "geeks quiz practice code"

s=string.split()[::-1]
l=[]
for i in s:
    l.append(i)
    
print(" ".join(l))

# remove the white spaces

print("".join(string.split()))

#How to Remove Letters From a String in Python

print(string.replace("g","k"))

#Python program to print even length words in a string
 even=string.split()

for word in even:
  if len(word) %2==0:
    print(word)

#Uppercase Half String

st="".join(string.split())
half_idx=len(st)//2
new_string=st[half_idx:]+st[:half_idx].upper()

print(new_string)

#Capitalize the first and last character of each word in a string
string = "geeks quiz practice code"
st=""
for i in string.title().split():
    st+=(i[:-1]+i[-1].upper())+' '
    
print(st)
