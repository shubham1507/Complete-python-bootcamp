def divisible_by_3and4(N):
    set1=set(range(0,N,3))
    set2=set(range(0,N,4))
    common= set1.intersection(set2)
    return common
    
    
print(divisible_by_3and4(100))
