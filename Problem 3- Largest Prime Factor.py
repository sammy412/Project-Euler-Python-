import math
def primeFactors(n):
     
    while n % 2 == 0:
        primelist.append(2)
        n = n / 2
    for i in range(3,int(math.sqrt(n))+1,2):
        while n % i== 0:
            primelist.append(i)
            n = n / i
    if n > 2:
        primelist.append(n) 
t=int(input())
for _ in range(t):
    primelist=[]
    n = int(input())
    primeFactors(n)
    print(max(primelist))

