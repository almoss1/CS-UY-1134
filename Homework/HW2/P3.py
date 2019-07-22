def permutations(lst, low, high):
    if low == high:
        return [[lst[low]]]
    else:
        lst2 = []
        for i in range(low, high+1):
            lst[i], lst[low] = lst[low], lst[i]
            for j in permutations(lst, low+1, high):
                other = [lst[low]] + j
                lst2.append(other)
            lst[i], lst[low] = lst[low], lst[i]
        return lst2


# print(permutations([1,2,3],0,2))