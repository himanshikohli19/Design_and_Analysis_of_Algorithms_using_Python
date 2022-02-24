# MergeSort in Python
#Time Complexity: O(N*log(N))

def mergeSort(array):
    if len(array) > 1:
        Mid = len(array)//2
        Left_arr = array[:Mid]
        Right_arr = array[Mid:]
        
        mergeSort(Left_arr)
        mergeSort(Right_arr)

        i = j = k = 0

        while i < len(Left_arr) and j < len(Right_arr):
            if Left_arr[i] < Right_arr[j]:
                array[k] = Left_arr[i]
                i += 1
            else:
                array[k] = Right_arr[j]
                j += 1
            k += 1

        while i < len(Left_arr):
            array[k] = Left_arr[i]
            i += 1
            k += 1

        while j < len(Right_arr):
            array[k] = Right_arr[j]
            j += 1
            k += 1


# Driver program
if __name__ == '__main__':
    array = [6, 5, 12, 10, 9, 1,16, 25, 2, 100, 9, 16]
    print("Original Array: ", array) 
    mergeSort(array)
    print("Sorted array is: ", array)
    