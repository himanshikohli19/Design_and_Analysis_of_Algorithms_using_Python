#with O(n) - unoptimized
def Lsearch(arr,s):
    for i in range(len(arr)):
        if s==arr[i]:
            return "element found at:" + str(i+1)
    return "Element not found"

#driver Code
arr1=[2,5,7,4,10,1,12,50,16,34,50,12]
s=1
print(Lsearch(arr1,s))