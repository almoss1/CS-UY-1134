def insertion_sort(lst):
    for i in range(1, len(lst)):
        curr = lst[i]
        j =i
        while j >0 and lst[j] > curr:
            lst[i] = lst[j]
            j -= 1
        lst[j] = curr