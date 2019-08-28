def merge(a,l,mid,h):
    i,j,k=l,mid+1,l
    while(i<=mid and j<=h):
        if (a[i]<a[j]):
            temp[k]=a[i]
            k+=1
            i+=1
        else :
            temp[k]=a[j]
            k+=1
            j+=1
    while(i<=mid):
        temp[k]=a[i]
        k+=1
        i+=1
    while(j<=h):
        temp[k]=a[j]
        k+=1
        j+=1
    for i in range(l,h+1):
        a[i]=temp[i]

def mergesort(a,l,h):
    if(l<h):
        mid=(l+h)//2
        mergesort(a,l,mid)
        mergesort(a,mid+1,h)
        merge(a,l,mid,h)



a=[5,6,2,3,4,22,43,1]
temp=[0]*(len(a))
print(a)
mergesort(a,0,len(a)-1)
print(a)
