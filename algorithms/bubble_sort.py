def bubbleSort(arr):
    arrLen = len(arr) - 1

    for i in range(arrLen):
        swapped = False
        for j in range(arrLen - i):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if not swapped:
            break
        
    return arr 