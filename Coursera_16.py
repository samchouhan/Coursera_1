def sum_of_integer(n):
    if n<1:
        return 0
    
    i=1
    sum=n+i
    while i<n:
        sum+=i
        i+=1
    return sum  

print(sum_of_integer(5))
print(sum_of_integer(10))