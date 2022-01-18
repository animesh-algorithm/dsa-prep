def pattern(N):
    if N==0:    return
    helper(N)
    print()
    pattern(N-1)
    
def helper(N):
    if (N==0):  return
    print("*", end="")
    helper(N-1)

pattern(5)