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

