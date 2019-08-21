def function1(a,k):
    n=len(a)
    for i in range(n):
        min=i
        for j in range(i+1,n):
            if a[j]<a[min]:
                min=j
        a[i],a[min]=a[min],a[i]
    print(a[k-1])


def function2(a,k):
    n=len(a)
    for i in range(n):
        max=i
        for j in range(i+1,n):
            if a[j]>a[max]:
                max=j
        a[i],a[max]=a[max],a[i]
    print(a[:k])

ls=[7,10,4,3,20,15]
ls2=[1, 23, 12, 9, 30, 2, 50]
k=3
function1(ls,k)
function2(ls2,k)



