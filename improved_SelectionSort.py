'''
Selection Sort - Improved
Idea: keep track of both maximum and minimum and array becomes sorted from both ends.
'''
def improvedSelectionSort(arr):
    for i in range(len(arr)):
        min_index=i
        for j in range(i+1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index=j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr


if __name__ == '__main__':
    arr = [98, 12, 56, 78, 89, 24, 47, 66, 25, 6, 10]
    print('Original Array: ', arr)
    print('Sorted Array: ', improvedSelectionSort(arr))