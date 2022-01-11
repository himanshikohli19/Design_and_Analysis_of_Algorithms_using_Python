#Iterative Method for Binary Search
def Bsearch(arr,s,left,right):
    if right>=1:
        mid=(left+right)//2
        if arr[mid]==s:
            return mid+1
        elif arr[mid]>s:
            return Bsearch(arr,s,left,mid-1)
        else:
            return Bsearch(arr,s,mid+1,right)
    else:
        return -1


#Driver code
arr=[2,5,7,8,9,10,12,15,17,19,23,45,56,58,67,69,70,73,76,78,79,89,98,99,102,134,156]
s=7
left=0
print(len(arr))
right=len(arr)-1
res=(Bsearch(arr,s,left,right))
if res!=-1:
    print("Element is present at: ",res)
else:
    print("Element not found")