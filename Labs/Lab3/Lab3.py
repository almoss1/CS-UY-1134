#Question 1

def first1(lst):
    high = len(lst) -1
    low= 0
    while low <=high:
        mid = (low+high) //2

        if lst[mid] == 1 and (mid == 0 or lst[mid -1]==0):
            return mid
        elif lst[mid] == 1:
            high = mid -1
        else:
            low = mid+1
    return -1

    

#Question 2
def e_approximation(n):
    if n == 0:
        return 1
    else:
        e = 1
        curr_fact = 1
        for i in range(1,n+1):
            curr_fact *= i
            e += 1/ float(curr_fact)
        return e


# Question 3

def two_sum(lst, target):
    lookup = {}
    for cnt, num in enumerate(lst):
        if target - num in lookup:
            return lookup[target-num], cnt
        lookup[num] = cnt 


#Question 4
def split_neg_pos(lst):
    left = 0
    for i in range(len(lst)):
        if lst[i] < 0:
            lst[i], lst[left] = lst[left], lst[i]
            left+=1
    return lst
            

#Question 5
def move_zeros(lst):
    left = 0
    for i in range(len(lst)):
        if lst[i] != 0:
            lst[i], lst[left] = lst[left], lst[i]
            left+=1
    return lst
    
#Question 6
def find_min(lst):
    if len(lst) == 1:
        return lst
    else:
        return min(lst[0], find_min(lst[1:]))

#in class
# theta(n^2) 
def find_min(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        min1 = lst[0]
        min2 = find_min(lst[1:])
        if min1 < min2:
            return min1
        else:
            return min2

#Get a better running time
#theta(n) constant work and n nodes in the tree
def find_min(lst,start,end):
    if start == end:
        return start
    else:
        firstnum = lst[start]
        minofrest = find_min(lst,start+1, end)
        if firstnum < minofrest:
            return firstnum
        else:
            return minofrest



def find_min(lst):
    def find_min_helper(lst,start,end):
    if start == end:
        return start
    else:
        firstnum = lst[start]
        minofrest = find_min(lst,start+1, end)
        if firstnum < minofrest:
            return firstnum
        else:
            return minofrest
    return find_min_helper(lst, 0, len(lst)-1)



print(first1([0,0,0,0,0,0,0,1,1,1]))
print(e_approximation(99))
print(split_neg_pos([-7,5,-3,4,2]))
print(two_sum([1,3,6,2],9))
print(move_zeros([0,7,0,1,2,0,5,0,2,8,0,0]))
print(find_min([1,2,3,4,5]))

#DONT GRADE
from math import factorial 
#Question 2
def e_approximation(n):
    result = 0
    for i in range(1,n+1):
        if n ==0:
            return 1
        else:
            result += (1 / float(factorial(i)))
            #print('result is '+ str(result))
    return 1 + result
