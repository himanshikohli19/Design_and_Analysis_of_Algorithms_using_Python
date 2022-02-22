# Bubble Sort
#Time Complexity: O(N^2)

def bubbleSort(arr):
	for i in range(len(arr)):
		for j in range(len(arr)-i-1):
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]
	
	return arr

# Driver code to test above
arr = [89, 167, 24, 64, 34, 25, 12, 22, 11, 90, 67, 78]
print("Original List: ", arr)
print("Sorted List: ",bubbleSort(arr))

