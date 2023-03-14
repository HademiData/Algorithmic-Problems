def linear_search(arr, x):
    """
    Searches for the given element x in the array arr using linear search algorithm.
    Returns the index of the element if found, otherwise returns -1.
    """
    n = len(arr)
    for i in range(n):
        if arr[i] == x:
            return i
    return -1
  
  
 def bubble_sort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n-i-1):

            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

                
                
                
                
import random

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def quicksort(arr, low, high):
    if low < high:
        pivot_index = random.randint(low, high)
        arr[high], arr[pivot_index] = arr[pivot_index], arr[high]
        pivot = partition(arr, low, high)
        quicksort(arr, low, pivot-1)
        quicksort(arr, pivot+1, high)
# example
arr = [5, 9, 1, 3, 8, 4, 7, 2, 6]
quicksort(arr, 0, len(arr)-1)
print(arr)
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
