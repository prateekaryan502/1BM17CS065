#program finds square root of a number using linear search
if __name__=="__main__" :
    n=int(input("Enter the number : "))
    # to find the sqrt of this number
    for i in range(n):
        if i*i==n:
            print("Square root of number is : ",i)
            break
    else:
        print("Number is not a perfect square")
