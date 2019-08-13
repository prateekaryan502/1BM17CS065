if __name__=="__main__" :
   a=[1,2,3,5,5,5,5,5,6]
   key=1
   s=0
   e=len(a)
   l,u=0,0
   m=(e+s)//2
   while(s<e):
       m = (e + s) // 2
       if a[m]==key:
            print(m)
            l,u=m,m
            while(a[l]==key):
                l=l-1
            while(a[u]==key):
                u=u+1
            break
       elif a[m]>key:
           print("smaller")
           s=m+1
       else :
           print("greater")
           e=m-1

   print(l+1,u-1)
