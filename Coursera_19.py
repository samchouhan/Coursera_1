def is_power_of_two(number):
    
    while number % 2 == 0 and number > 1:
        number= number / 2
    
    if number == 1:
        return True
    return False

print(is_power_of_two(0))
print(is_power_of_two(1))