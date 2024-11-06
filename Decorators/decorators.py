def parent(num):
    def f_child():
        return "This is 1st child"
    def s_child():
        return "This is 2nd child"
        
    if num == 1:
        return f_child
    else:
        return s_child

first_child=parent(1)

#print(first_child())

#-------------------
def my_name_decorator(func):
    def wrapper():
        print("My surname  is Joshi ")
        func()
        print("Nitin is my fathers name")
    return wrapper
    
@my_name_decorator    
def son():
    print("My name is Shubham")
    
son()
 
