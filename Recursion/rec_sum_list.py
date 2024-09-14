def sum_list(p_ls):
    if not isinstance(p_ls,list):
        return -1
    elif len(p_ls) == 1:
        return p_ls[0]
    else:
        total=p_ls[0]+sum_list(p_ls[1:])
        return total

mylist = [1,2,3,4,5]

print(sum_list(mylist))
