marks = [44, 64, 54, 74, 34, 104,64]

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    smaller = []
    larger = []
    equal=[]
    
    for x in arr:
        if x < pivot:
            smaller.append(x)
        elif x > pivot:
            larger.append(x)
        else:
            equal.append(x)
    return quicksort(smaller) +equal + quicksort(larger)

print(quicksort(marks))
