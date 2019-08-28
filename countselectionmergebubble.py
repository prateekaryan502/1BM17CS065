
def merge(a,l,mid,h):
    global countm
    i,j,k=l,mid+1,l
    while(i<=mid and j<=h):
        if (a[i]<a[j]):
            countm+=1
            temp[k]=a[i]
            k+=1
            i+=1
        else :
            countm+=1
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

def selectionsort(a):
    global counts
    n=len(a)
    for i in range(n):
        min=i
        for j in range(i+1,n):
            if a[j]<a[min]:
                counts+=1
                min=j
            else :
                counts+=1
        a[i],a[min]=a[min],a[i]

def bubblesort(a) :
    n=len(a)
    for i in range(n):
        for j in range(i,n):
            if(a[i]>a[j]):
                a[i],a[j]=a[j],a[i]
                global countb
                countb+=1
            else :
                countb+=1

a=[5,6,2,3,4,22,43,1]
b=[5,6,2,3,4,22,43,1]
c=[5,6,2,3,4,22,43,1]
temp=[0]*(len(a))
countm,counts,countb=0,0,0
mergesort(a,0,len(a)-1)
selectionsort(b)
bubblesort(c)

print("No. of comparisons in bubble sort",countb)
print("No. of comparisons in merge sort",countm)
print("No. of comparisons in selection sort",counts)