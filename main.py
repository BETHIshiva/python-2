# Harish wants to paint his dog's home that has n boards with different lengths. The length of ith board is given by arr[i] where arr[] is an array of n integers. He hired k painters for this work and each painter takes 1 unit time to paint 1 unit of the board. The problem is to find the minimum time to get this job done if all painters start together with the constraint that any painter will only paint continuous boards, say boards numbered {2,3,4} or only board {1} or nothing but not boards {2,4,5}.
# Input:n = 5,k = 3,arr[] = {5,10,30,20,15},Output: 35
def numberOfPainters(arr, n, maxLen):
    total = 0
    numPainters = 1

    for i in arr:
        total += i

        if (total > maxLen):
            total = i
            numPainters += 1

    return numPainters


def partition(arr, n, k):
    lo = max(arr)
    hi = sum(arr)

    while (lo < hi):
        mid = lo + (hi - lo) // 2
        requiredPainters = numberOfPainters(arr, n, mid)
        if (requiredPainters <= k):
            hi = mid
        else:
            lo = mid + 1

    return lo


arr = [5, 10, 30, 20, 15]
n = len(arr)
k = 3
print(int(partition(arr, n, k)))