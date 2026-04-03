for x in range(7):
    if x%2==0:
        print(x)
        
#As a lisst comprehension
even_numbers= [x for x in range(7) if x%2==0]        
print(even_numbers)