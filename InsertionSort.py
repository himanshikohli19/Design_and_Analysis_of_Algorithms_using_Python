#INSERTION SORT
def InsertionSort(arr):
    for i in range(len(arr)):
        key_ele=arr[i]
        j = i-1
        while j >= 0 and key_ele < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key_ele
    
    return arr


#DRIVER CODE
if __name__ == "__main__":
    arr = [98, 12, 56, 78, 89, 24, 47, 66, 25, 6, 10]
    print('Original Array: ', arr)
    print('Sorted Array: ', InsertionSort(arr))
