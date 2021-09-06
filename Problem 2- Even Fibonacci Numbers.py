nums={1:1,2:2}
def fib(n):
    #if n<=2:
        #return 1
    if n in nums:
        return nums[n]
    else:
        num=fib(n-1)+fib(n-2)
        nums[n]=num
        return num
t=int(input())
for i in range(t):
    sum=0
    n=int(input())
    fib(n)
    llist=list(nums.values())
    for i in llist:
        if(i%2==0 and i<n):
            sum+=i
    print(sum)
    
