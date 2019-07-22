import math

#doesnt work

def find_primes(n):
    count_divisor = 0
    lst = []
    
    for i in range(n):
        if n < 2:
            lst.append(i)
        for k in range(2, int(math.sqrt(n))+1):
            if n % k == 0:
                count_divisor += 1
        if count_divisor >  1:
            print("This is a list", i)
        else:
            lst.append(i)
   
    return lst
#print(find_primes(8))




#2b)

def primeSieve(sieveSize):
    sieve = [True] * sieveSize
    sieve[0] = False
    sieve[1] = False

    for i in range(2, int(math.sqrt(sieveSize)) + 1):
        pointer = i * 2
    while pointer < sieveSize:
        sieve[pointer] = False
        pointer += i

    primes = []
    for i in range(sieveSize):
        if sieve[i] == True:
            primes.append(i)
    return primes


print(primeSieve(8))

#IN CLASS IMPLEMENTATION

def is_prime(n):
    if n <=1:
        return False
    curr_fator = 2
    while curr_fator * curr_fator <=n:
        if n % curr_fator ==0:
            return False
        curr_fator+=1
    return True

def find_primes(n):
    lst =[]
    for i in range(2,n+1):
        if is_prime(i):
            lst.append(i)
    return lst


print(find_primes(100))


def prime_sieve(n):
    prime_lst = [True] * (n+1)
    #prime_lst[i] ==True iff i is prime
    curr_prime = 2
    while curr_prime <= n:
        while prime_lst[curr_prime] == False:
            curr_prime+=1

        for curr_num in range(2*curr_prime,n+1, curr_prime):
            prime_lst[curr_num] = False

        curr_prime+=1

    return [i for i in range(2, n+1) if prime_lst[i]]
print(prime_sieve(20))