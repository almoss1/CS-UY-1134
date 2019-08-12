from ChainingHashMap import ChainingHashMap
#problem 2
def list_intersection(lst1, lst2):
    new_lst = []
    ht = ChainingHashMap()
    for i in range(len(lst1)):
        ht.hash_function(lst[i])
    for j in range(len(lst2)):
        ht.hash_function(lst2[j])
    for ind in range(ht.table_size):
        curr_bucket = ht.table[ind]
        for ind_table in curr_bucket:
            if curr_bucket[ind_table] >= 2:
                new_lst.append(curr_bucket[ind_table])

    #Runtime is theta(n^2)

#problem 3
def mode_of_list(lst):
    max_count =0
    num = None
    ht = ChainingHashMap()
    for i in range(len(lst1)):
        ht.hash_function(lst[1])
        count =0
    for ind in range(ht.table_size):
        curr_bucket = ht.table[ind]
        for ind_table in curr_bucket:
            count += 1
            if count > max_count:
                max_count = count 
                num = curr_bucket[ind_table]
    return num
#runtime is theta(n^2)
#You could use a binary search tree map that holds all the same digits together so it would be
#easy to tell which number was displayed the most


#problem 4
def two_sum(lst, target):
    seen_num = ChainingHashMap()
    for i in range(len(lst)):
        try:
            if seen_num[target-lst[i]]:
                return (seen_num[target-lst[i]], i)
        except:
            seen[lst[i]] = 1
    return (None, None)

#problem 5
def is_anagram(str1, str2):
    ht = ChainingHashMap()
    str1_count = 0
    str2_count= 0
    for i in str1:
        str1_count += ord(i)
    for j in str2:
        str2_count += ord(j)

    if ht.hash_function(str1_count) == ht.hash_function(str2_count):
        return True
    return False

