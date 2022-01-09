#with O(n/2) - optimized
def Lsearch(arr,s):
    left=0
    right=len(arr)-1
    while left!=((len(arr))//2)+1 or right!=((len(arr))//2)+1:
        if arr[left]==s:
            return "Element found at: "+str(left+1)+" position (using left side search)"
        if arr[right]==s:
            return "Element found at: "+str(right+1)+" position (using right side search)"
        left+=1
        right-=1

    return "Element not found!"

#driver Code
arr1=[2,5,7,4,10,1,12,50,16,34,50,120,100,14,56,67,78,89,98,99,36,177,134,245,567,33,23]
s=245
print(Lsearch(arr1,s))