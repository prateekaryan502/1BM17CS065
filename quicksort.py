
def quicksort(a,l,h):
    if(l<h):
        j=partition(a,l,h)
        quicksort(a,l,j)
        quicksort(a,j+1,h)

def partition(a,l,h):
    pivot=a[l]
    i,j=l,h
    while(i<j):
        while(a[i]<=pivot):
            i+=1
        while(a[j]>pivot):
            j-=1
        if(i<j):
            a[i-1],a[j-1]=a[j-1],a[i-1]
    a[l],a[j]=a[j],a[l]
    return j
a=[5,4,2,45,53]
print(a)
quicksort(a,0,len(a)-1)
print(a)