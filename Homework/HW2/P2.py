def flatten_nested_list(nested_lst, low, high):
    lst = []
    if low >= high:
        return lst[low]
    else:
        for i in nested_lst:    
            if isinstance(i,list): 
                lst.extend(flatten_nested_list(i, 0, len(nested_lst)-1))
            else:
                lst.append(i)

        return lst
        
# print(flatten_nested_list([1, [2, 3], 4, [5, [6, [7, [8]]]]], 0,3))