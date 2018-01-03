import time
def sum_of_n_2(n):
    start = time.time()

    sum = 0
    for i in range(1,n+1):
        sum = sum + i 

    end = time.time()

    return sum,end-start

for i in range(5):
    print("sum is %d required %10.7f seconds" %sum_of_n_2(10000))