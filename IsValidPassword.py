import string


def isValidPassword(password):
    special_chars = string.punctuation
    print(special_chars)

    if len(password) < 10:
        print("Password has less than 10 characters.")
        return False
    elif len(password) < 15:
        print("Password has more than 15 characters.")
        return False
    elif any(char.isspace() for char in password):
        print("Password should not contain spaces.")
        return False
    elif '.' in password:
        print("Password should not contain a dot ('.'")
        return False
    elif not any(char.isupper() for char in password):
        print("Password should contain at least one uppercase letter.")
        return False
    elif not any(char.islower() for char in password):
        print("Password should contain at least one lowercase letter.")
        return False
    elif not any(char.isdigit() for char in password):
        print("Password should contain at least one digit.")
        return False
    elif not any(char in special_chars for char in password):
        print(f"Password should contain at least one special character from the keyboard: {special_chars}")
        return False
    else:
        print("Valid password.")
        return True


password = input("Enter Password = ")
print(isValidPassword(password))


