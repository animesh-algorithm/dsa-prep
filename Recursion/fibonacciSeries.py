def fibonacciSeries(n):
    if n==0 or n==1:
        return n
    res = fibonacciSeries(n-1)+fibonacciSeries(n-2)
    print(res, end=" ")
    return res

print(fibonacciSeries(5))
    