def binarysearch(arr,l,h,k):
    mid=(l+h)//2
    x=arr[mid]
    while(l<h):
        print("h")
        if x==k:
             return 1
             break
        elif k>x:
            l=mid+1
            binarysearch(arr,l,h,k)
        else :
            h=mid-1
            binarysearch(arr,l,h,k)
    if(l>=h):
        return -1

if __name__ == "__main__":
    #n=input() #number of test cases
    #x=input().split(" ") #number of elements and number to find
    print("Prateek")
    arr=[1,2,3,4,0]
    l=0
    h=4
    k=4
    ans=binarysearch(arr,l,h,k)
    print(ans)
