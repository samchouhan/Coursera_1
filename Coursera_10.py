def hint_username(username):
    if len(username) < 3:
        return "Username must be at least 3 characters long."
    elif len(username) > 15:
        return "Username cannot be more than 15 characters long."
    else:
        return "Username is valid."
    
input_username = "jsmith"
print(hint_username(input_username))