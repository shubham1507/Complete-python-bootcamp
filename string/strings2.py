#length of string

a = "geeks"

print(len(a))

#Reverse Words in a Given String in Python
s = "Python is a gen lang"
reversed = ' '.join(s.split()[::-1])
print(reversed)

#How to Remove Letters From a String in Python

s = "hello world"

rem_ith = s.replace("o","")

print(rem_ith)

#Avoid Spaces in string length

space_avoided = s.replace(" ","")
print(space_avoided)

#Python program to print even length words in a string
s = "This is a python language"

get_words=s.split()
even_len = [word for word in get_words if len(word)%2==0]

print(" ".join(even_len))

#Uppercase Half String

s= "shubham"
i= len(s)//2
print(s[:i].upper()+s[i:])

#capitalize the first and last character of each word in a string
print(s.capitalize().replace(s[-1],s[-1].upper()))

sentense= " This is something very big"

splitted=sentense.split()
print(splitted)
capitalize=[word.capitalize().replace(word[-1],word[-1].upper()) for word in splitted ]
print(" ".join(capitalize))

#check if a string has at least one letter and one number

s = "geeksforgeeks"

al = any(c.isalpha() for c in s)
dt = any(d.isdigit() for d in s)

if al and dt:
    print("yes")
 
else:
    print("no")

#Accept the strings which contains all vowels Using all()

s = "Geeksforgeeks"
v = 'aeiou'

if all(i in s.lower() for i in v):
    print(True)
else:
    print(False)
    
#Count the Number of matching characters in a pair of string

s1 = "VISHAKSHI"
s2 = "VANSHIKA"

res=len(set(s1.lower()).intersection(set(s2.lower())))
print(res)

#Count number of vowels using sets in given string
s = "Python Programming"
vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

count = sum(1 for ch in s if ch in vowels)
print(count)

#Remove All Duplicates from a Given String in Python

res=""
seen=set()

for char in s:
    if char not in seen:
        seen.add(char)
        res+=char
        
print("unique chr is: ", res)


#check if a string contains any special character

import re 

def run(string):
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if(regex.search(string) == None):
        print("String dosnt have special char")
    else:
        print("String have special char")
        
if __name__ == '__main__':
    string = "Geeks!@#$%forGeeks"
    run(string)
