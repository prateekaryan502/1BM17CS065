#to find square root of a number using binary search
if __name__=="__main__" :
    n=int(input("Enter the number : "))
    s=0
    e=n
    a=[i for i in range(n)]
    while(s<=e):
        m=(e+s)//2
        if a[m]*a[m]==n:
            print("Square root of number is :",a[m])
            break
        elif a[m]*a[m]>n:
            s=m+1
        else :
            e=m-1
    if(s>=e):
        print("Number is not a perfect square")
