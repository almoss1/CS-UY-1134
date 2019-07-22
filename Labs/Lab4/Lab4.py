
#5A)O(n^2)
#5b)
import random
def random_str(n):
    letters = "abcdefghijklmnopqrstuvwxyz"
    s = [random.choice(letters) for i in range(1,n+1)]
    return "".join(s)
    
print(random_str(5))


#6
def powers(base,n):
    base_growth = base
    for i in range(n):
        yield base_growth 
        base_growth = base_growth * base

for val in powers(2,10):
    print(val)


#7
def palindrome(input_string, low, high):
    if low == high:
        return True
    else:
        if input_string[low+1] == input_string[high-1]:
            return palindrome(input_string,low+1,high-1)
        return False

print(palindrome("racecar", 0, 6))




#8

def partition(lst):
    begin =0
    end = len(lst) -1
    pivot = begin
    for i in range(begin+1, end+1):
        if lst[i] <= lst[begin]:
            pivot += 1
            lst[i], lst[pivot] = lst[pivot], lst[i]
    lst[pivot], lst[begin] = lst[begin], lst[pivot]
    return lst



print(partition([42, 17, 81, 77, 68, 22, 55, 10, 90]))