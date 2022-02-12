def printN(N):
    if N==0:
        return
    printN(N-1)
    print(N)

def printNReverse(N):
    if N==0:
        return
    print(N)
    printNReverse(N-1)

printNReverse(5)