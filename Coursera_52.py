def count__by_10(end):
    count=""
    
    for number in range(0,end+1,10):
        count+=str(number)+" "
        
    return count.strip()

print(count__by_10(100))