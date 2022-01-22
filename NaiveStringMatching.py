str1="himanshikohlishikohliKoHLi"
pattern="koh"
n=len(str1)
m=len(pattern)
for i in range(0,n-m+1):
    j=0
    while(j<m):
        if str1[i+j] != pattern[j]:
            break
        j+=1
    if j==m:
        print("Pattern found at position: ",i+1)

