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


