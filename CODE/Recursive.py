def count_up(start, end):
    for i in range(start, end+1):
        print(i)

def count_up1(start, end):
    if start == end:
        print(end)
    else:
        print(start)
        count_up1(start+1,end)


def count_up2(start,end):
    if start == end:
        print(end)
    else:
        count_up2(start,end-1)
        print(end)


def count_up3(start,end):
    if start == end:
        print(end)
    else:
        mid = (start+end) //2
        count_up3(start,mid)
        count_up3(mid+1,end)



def count_down(low,high):
        if low == high:
                print(high)
        else:
                count_down(low+1,high)
                print(low)                

def count_down2(low,high):
        if low == high:
                print(high)
        else:
                print(high)    
                count_down(low,high-1)
                

def count_up_and_down(low,high):
        if low == high:
                print(high)
        else:
                print(low)
                count_up_and_down(low+1,high)
                print(low)


def factorial(n):
        if n ==1:
                return 1
        else:
                return n * factorial(n-1)


def power(x,n):
        if n ==0:
                return 1
        else:
                return x * power(x,n-1)

def power2(x,n):
        if n ==0:
                return 1
        else:
                #x**n = x**(n/2) * x**(n/2)
                powerpart1  = power2(x, n//2)
                powerpart2 = power2(x, n//2)
                result = powerpart1 * powerpart2
 #               if n % 2 == 1:
 #                       result* = x
                return result



print("\ncount_up1")
count_up1(1,10)
print("\ncount_up2")
count_up2(1,10)
print("\ncount_up3")
count_up3(1,10)
print("\ncount_down")
count_down(1,10)
print("\ncount_down2")
count_down2(1,10)
print("\ncount_up_and_down")
count_up_and_down(1,5)

print("Factorial " + str(factorial(3)))
print("Power " + str(power(2,2)))