s1="bqdrcvefgh"
s2="abcvdefgh"
l1=len(s1)
l2=len(s2)
a=[[0]*(l1+1)]*(l2+1)
for i in range(l2+1):
    for j in range(l1+1):
        if i==0 or j==0:
            a[i][j]=0
        elif s1[j-1]==s2[i-1]:
            a[i][j]=a[i-1][j-1]+1
        elif s1[j-1]!=s2[i-1]:
            a[i][j]=max(a[i-1][j],a[i][j-1])
print(a[l2][l1])