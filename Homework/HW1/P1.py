#1a)
def harmonic(n):
    result = 0.0
    for i in range(1,n+1):
        #print("i = ",i)
        #print("1//i " + str(float(1 // i)))
        result+= (1 / float(i))
    return result


print(harmonic(5))


#1b)
def harmonic2(n):
    result = sum([(1 / float(i))  for i in range(1,n+1)])
    return result

print(harmonic2(5))


