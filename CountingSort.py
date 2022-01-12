#Counting Sort

def CountingSort(array):
    size=len(array)
    output=[0]*size
    #Finding out the maximum number in the array.
    maxArray=array[0]
    for i in range(1,len(array)):
        if maxArray<array[i]:
            maxArray=array[i]

    count=[0]*(maxArray+1)

    for i in range(0,size):
        count[array[i]]+=1
    
    for i in range(1,maxArray+1):
        count[i]+=count[i-1]
    
    i=size-1
    while i>=0:
        count[array[i]]-=1
        output[count[array[i]]] = array[i]
        i-=1

    return output

#Driver Code
arr=[10,4,2,6,17,3,13,16,1,12,5]
print("Original Array: ",arr)
print("Sorted Array: ",CountingSort(arr))