


def count_appearance(lst,val):
    def count_appearance_helper(lst,low,high,val):
        if (low == high):
            if (lst[low] == val):
                return 1
            else:
                return 0
        else:
            rest_count = count_appearance_helper(lst,low+1,high,val)
            if (lst[low] ==  val):
                return (rest_count + 1)
            else:
                return (rest_count)
    if (len(lst) == 0):
        return 0
    else:
        return count_appearance_helper(lst,0,len(lst)-1)




count_appearance([2,4,6,4,1,7,4,2],2,6,4)


       #Assume when calling count appearance on a smaller range of low and high 
       # then it would return the number of times val shows in that indicated sublist
    
when claling power with a smaller exposnent it wold retunr the power we desired