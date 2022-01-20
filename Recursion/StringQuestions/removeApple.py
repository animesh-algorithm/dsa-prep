s = "bcd app f g appapple"

def removeApple(s):
    if s == "":
        return s
    if not s.startswith("apple"):
        return s[0] + removeApple(s[1:])
    return removeApple(s[5:])

def removeAppNotApple(s):
    if s == "":
        return s
    if s.startswith("app"):
        if s.startswith("apple"):
            return s[0] + removeAppNotApple(s[1:])
        else:
            return removeAppNotApple(s[3:])
    return s[0] + removeAppNotApple(s[1:])

print(removeAppNotApple(s))
