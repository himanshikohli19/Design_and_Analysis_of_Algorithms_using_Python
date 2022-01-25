#Robin Karp Algorithm - String Matching
d=10
def PatternSearch(pattern, text,q):
    n=len(text)
    m=len(pattern)
    p=t=i=j=0
    h=1
    for i in range(m-1):
        h=(h*d)%q
    for i in range(m):
        p=(d*p + ord(pattern[i]))%q
        t=(d*t + ord(text[i]))%q
    for i in range(n-m+1):
        if p==t:
            for j in range(m):
                if text[i+j]!=pattern[j]:
                    break
            j+=1
            if j==m:
                print("Pattern found at: "+str(i+1))
        
        if i<(n-m):
            t=(d*(t-ord(text[i])*h)+ord(text[i+m]))%q
            if t<0:
                t=t+q

#Driver code
text="ABCCDDAEFGCDDS"
pattern="CDD"
q=13
PatternSearch(pattern, text, q)