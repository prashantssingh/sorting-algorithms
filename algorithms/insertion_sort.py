def insertionSort(arr):
    # for each element in the array
    for index in range(1, len(arr)):
        current = arr[index]
        position = index

        while position > 0 and arr[position-1] > current:
            arr[position] = arr[position-1]
            position -= 1

        arr[position] = current

    return arr