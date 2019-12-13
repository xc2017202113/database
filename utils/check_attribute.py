


def check_username(username):
    #status = True
    username = str(username)
    if len(username) == 0 or len(username)>10:
        return False

    for chars in username:
        if not chars.isdigit() and not chars.isalpha():
            return False

    return True

def check_password(password):
    password = str(password)
    if len(password) == 0 or len(password)>10:
        return False

    has_digit = False
    has_alpha = False

    for chars in password:
        print(chars)
        if chars.isalpha():
            has_alpha = True

        if chars.isdigit():
            has_digit = True

        if not chars.isdigit() and not chars.isalpha():
            return False

    if not (has_digit and has_alpha):
        print(has_alpha)
        print(has_digit)
        print("-------")
        return False

    return True

def check_email(email):
    email = str(email)

    if len(email) != len("2017202113@ruc.edu.cn"):
        return False

    if email[len("2017202113"):] != "@ruc.edu.cn":
        return False

    school_numer = str(email[:len("2017202113")])
    for chars in school_numer:
        if not chars.isdigit():
            return False


    return True



