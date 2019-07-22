#1 Binary Search

def binary_search(lst, val,low,high):
    if low + 1 == high:
        return None
    if lst[low] == val:
        return low
    if lst[high] == val:
        return high 
    mid  = (low+high) // 2
    if lst[mid] == val:
        return mid
    elif val > lst[mid]:
        return binary_search(lst,val, mid, high)
    elif val < srt_lst[mid]:
        return binary_search(lst, val, low, mid)

print(binary_search([1,2,3,4,7,8,9,13],4,0,7))



#2 Nested Sum
def nested_sum(lst):
    if not isinstance(lst, list):
        return lst
    else:
        total = 0 
        for i in lst:
            total += nested_sum(i)
        return total

print(nested_sum([1, [2, [3], [4, 5]], [6, 7]]))




#3 Selection Sort
#Part 1

"""
def find_min(lst, low, high):
    if low == high:
        return lst[low]
    else:
        if lst[low] < lst[high]:
           return find_min(lst, low, high-1)
        else:
            return find_min(lst, low+1, high)

def selection_sort(lst):
    low =0
    for i in range(len(lst)-1):
        mini = find_min(lst,low, len(lst)-1)
        low += 1
        print(mini)
        lst[i], lst[mini] = lst[mini], lst[i]
    return lst


print(selection_sort([1,4,2,7,44,3,88]))
"""
def selection_sort(lst):
    for i in range(len(lst)): 
        min_idx = i 
        for j in range(i+1, len(lst)): 
            if lst[min_idx] > lst[j]: 
                min_idx = j       
        lst[i], lst[min_idx] = lst[min_idx], lst[i] 
    return lst

print(selection_sort([2,3,5,1,8,2,5,9]))



#Part 2


def find_min_index(lst , low , high ): 
    if low == high: 
        return low  
    minimum = find_min_index(lst, low+ 1, high) 
    return (low if lst[low] < lst[minimum] else minimum) 


print(find_min_index([2,2,3,6,1,7,8,9],0,7))

def selection_sort(lst, low, high):  
    if low == high: 
        return low 
    minimum_ind = find_min_index(lst, low+1, high) 
    if minimum_ind != low: 
        lst[minimum_ind], lst[low] = lst[low], lst[minimum_ind] 

    selection_sort(lst, low+1, high ) 
    
print(selection_sort([7,4,9,3,6,8],0,5))



#4 
def partition(lst, start, end):
    pos = start                         
    for i in range(start, end):        
        if lst[i] < lst[end]:            
            lst[i],lst[pos] = lst[pos],lst[i]
            pos += 1

    lst[pos],lst[end] = lst[end],lst[pos] 
                                         
    return pos

def quicksort(lst, start, end):
    if start == end:
        return start
    else:
        if start < end:                     
            pos = partition(lst, start, end)
            quicksort(lst, start, pos - 1)
            quicksort(lst, pos + 1, end)
    return lst
                             

print(quicksort([3,22,88,1,5,33,98,2,6],0,8))