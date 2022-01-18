def pattern(N):
    if N==0:    return
    pattern(N-1)
    helper(N)
    print()

def helper(N):
    if (N==0):  return
    print("*", end="")
    helper(N-1)

pattern(5)

# *
# **
# ***
# ****
# *****