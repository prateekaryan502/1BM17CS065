def returnmax(a):
    print("List of integers:",a)
    x=-99999
    for i in a:
        if i >x :
            x=i
    return x

if __name__ == "__main__" :
    n = int(input("Enter number of integers :"))
    a = []
    for i in range(n):
        a.append(int(input()))
    y=returnmax(a)
    print("Max Integer :",y)
