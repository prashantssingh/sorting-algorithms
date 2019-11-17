def bubbleSort(arr):
    arrLen = len(arr) - 1

    for i in range(arrLen):
        for j in range(arrLen - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr 