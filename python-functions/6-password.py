#!/usr/bin/python3

def validate_password(password):
    
    if len(password) < 8:
        return False

    # Check for uppercase, lowercase, and digit
    has_uppercase = False
    has_lowercase = False
    has_digit = False

    for characters in password:
        if characters.isupper():
            has_uppercase = True
        elif characters.islower():
            has_lowercase = True
        elif characters.isdigit():
            has_digit = True
        elif characters.isspace():
            return False

    return has_uppercase and has_lowercase and has_digit