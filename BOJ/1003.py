def fibonacci(n):
    global zero_count
    global one_count
    global dp
    if(dp.get(n)!=None):
        return dp[n]
    if(n==0):
        zero_count+=1
        dp[n] = [zero_count, one_count]
        return dp[n]
    elif(n==1):
        one_count+=1
        dp[n] = [zero_count, one_count]
        return dp[n]
    
    a = fibonacci(n-1)
    zero_count = 0
    one_count = 0
    b = fibonacci(n-2)
    
    dp[n] = [a[0]+b[0], a[1]+b[1]]
    return dp[n]


repeat_num = int(input())
dp = {}
for i in range(repeat_num):
    input_num = int(input())
    zero_count = 0
    one_count = 0
    fibonacci(input_num)
    print(dp[input_num][0], dp[input_num][1])
