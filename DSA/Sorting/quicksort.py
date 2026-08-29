import random
def Quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    left = [ i for i in arr if i < pivot]
    right = [i for i in arr if i > pivot]
    middle = [i for i in arr if i == pivot]
    return Quicksort(left) + middle + Quicksort(right)

arr = list(map(int,input().split()))
print("Before sorting",arr)
print("After sorting",Quicksort(arr))

