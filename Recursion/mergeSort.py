arr = [5,4,3,2,1]

def mergeSort(arr):
    if (len(arr) == 1):
        return arr
    mid = len(arr)//2
    left = mergeSort(arr[0:mid])
    right = mergeSort(arr[mid:len(arr)])
    return mergeTwoSortedArray(left, right)


def mergeTwoSortedArray(A, B):
    i = 0
    j = 0
    res = []
    while (i < len(A)) and (j < len(B)):
        if A[i] < B[j]:
            res.append(A[i])
            i+=1
        else:
            res.append(B[j])
            j+=1
    while (i < len(A)):
        res.append(A[i])
        i+=1
    while (j < len(B)):
        res.append(B[j])
        j+=1
    return res

print(mergeSort(arr))