#our aim is to sort the elements of the array
#we are following divide and conquer strategy to do this
#we are dividing array into smaller lists and then sorting the list
#merge

def merge(l,mid,h):
    i,j,k=0,0,0
    while(i<=m and j<=n):
        if (l1[i]<l2[j]):
            l3[k]=l1[i]
            k+=1
            i+=1
        else :
            l3[k]=l2[j]
            k+=1
            j+=1
    while(i<=m):
        l3[k]=l1[i]
        k+=1
    while(j<=n):
        l3[k]=l2[j]
        k+=1
    return l1
def mergesort(l,h):
    if(l<h):
        mid=(l+h)//2
        mergesort(l,mid)
        mergesort(l,mid)
        merge(l,mid,h)

l1=[1,2,4]
l2=[4,6,7]
l3=mergesort(l1,l2)
print(l3)

