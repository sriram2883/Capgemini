#password strength checker
def checkpassword(password):
    if len(password) < 8:
        return "Password is too short"
    elif len(password)>8:
        if not any(i.isupper() for i in password):
            return "Password must have at least one uppercase letter"
        if not any(i.islower() for i in password):
            return "Password must have at least one lowercase letter"
        if not any(i.isdigit() for i in password):
            return "Password must have at least one digit"
        special_characters = "!@#$%^&*()-+"
        if not any(i in special_characters for i in password):
            return "Password must have at least one special character"
        return "Password is strong"
password = input("Enter a password: ")
