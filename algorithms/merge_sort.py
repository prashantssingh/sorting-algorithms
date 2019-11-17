def merge(leftSubArr, rightSubArr):
    """ Function to merge two arrleftSubArrys """
    result = []
    while len(leftSubArr) != 0 and len(rightSubArr) != 0:
        if leftSubArr[0] < rightSubArr[0]:
            result.append(leftSubArr[0])
            leftSubArr.remove(leftSubArr[0])
        else:
            result.append(rightSubArr[0])
            rightSubArr.remove(rightSubArr[0])
    
    if len(leftSubArr) == 0:
        result += rightSubArr
    else:
        result += leftSubArr

    return result

def mergeSort(arr):
    if len(arr) < 2:
        return arr
    else:
        middle = len(arr)//2
        leftSubArr  = mergeSort(arr[:middle])
        rightSubArr = mergeSort(arr[middle:])
        return merge(leftSubArr, rightSubArr)
