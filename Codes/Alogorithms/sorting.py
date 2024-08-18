import random 
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Example usage
arr = random.sample(range(1,101),10)
print(arr)
sorted_arr = bubble_sort(arr)
print("Sorted array is:", sorted_arr)
