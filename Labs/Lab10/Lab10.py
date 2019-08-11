from ChainingHashMap import ChainingHashMap
#problem 2
def list_intersection(lst1, lst2):
    new_lst = []
    ht = ChainingHashMap()
    for i in range(len(lst1)):
        ht.hash_function(lst[1])
    for j in range(len(lst2)):
        ht.hash_function(lst2[j])
    for ind in range(ht.table_size):
        for ind_table in ht.table:
            if ht.table[ind_table] >= 2:
                new_lst.append(ht.table[ind_table])

    #Runtime is theta(n^2)

#problem 3
def mode_of_list(lst):
    max_count =0
    ht = ChainingHashMap()
    for i in range(len(lst1)):
        ht.hash_function(lst[1])

   for ind in range(ht.table_size):
        for ind_table in ht.table:
            ##need to implement 


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
    pass



