def is_power_of_two(number):
    while number % 2 == 0:
        number = number / 2
    
    if number == 1:
        return True
    return False    

print(is_power_of_two(1))
print(is_power_of_two(2))   
print(is_power_of_two(8))