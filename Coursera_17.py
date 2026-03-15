def multiplication_table(number):
    #intialize the variable
    multiplier = 1
    
    while number <= 5:
        result = number * multiplier
        
        if result > 25:
            break
        print(str(number) + " x " + str(multiplier) + " = " + str(result))
            
        multiplier += 1
        
multiplication_table(4)