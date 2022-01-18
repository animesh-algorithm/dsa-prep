import random
A = [6, 5, 4, 3, 2, 1, 12, 10]

def quickSort(A, low, high):
    # base case
    if (low >= high):   return

    # picking the pivot
    pivot = random.choice(A)
    s = low
    e = high

    while (s <= e):
        # checking for violation
        while A[s] < pivot:
            s+=1
        while A[e] > pivot:
            e-=1
        # swapping
        if s <= e:
            A[s], A[e] = A[e], A[s]
            s+=1
            e-=1
    # recursive calls for two subarrays
    quickSort(A, low, e)
    quickSort(A, s, high)

quickSort(A, 0, len(A)-1)
print(A)