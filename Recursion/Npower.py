def power(num,pow):
    if pow == 1:
        return num
    elif pow == 0:
        return 1
    else:
        return num*power(num,pow-1)   
    
print(power(2,8))
