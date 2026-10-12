marks = [44, 64, 54, 74, 34, 104]

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    smaller = []
    larger = []
    
    for x in arr:
        if x < pivot:
            smaller.append(x)
        elif x > pivot:
            larger.append(x)
            
    return quicksort(smaller) + [pivot] + quicksort(larger)

print(quicksort(marks))
