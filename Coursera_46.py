input = "Four score and seven years ago "
for c in input:
    if c.lower() in ['a','e','i','o','u']:
        print(c)
        
print([c for c in input if c.lower() in ['a','e','i','o','u']])        

for c in range (len(input)):
    if c in ['a','e','i','o','u']:
        print(c)