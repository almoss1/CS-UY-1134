def leonardo(n):
    a = 1
    b = 1
    for _ in range(n):
        yield a
        a, b = b, (a + b + 1)


for i in leonardo(7):
    print(i)

#  When running this code for me it shows "end ='' " is an invalid syntax but im on th latest version of python


# in class implementation
def leonardo_inClass(n):
        prev_leo = 1
        curr_leo =1
        yield prev_leo

        for i in range(n):
                yield curr_leo
                next_leo = prev_leo +  curr_leo + 1
                prev_leo = curr_leo 
                curr_leo = next_leo

for num in leonardo_inClass(7):
        print(num)
