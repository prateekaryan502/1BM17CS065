# ls=[3,4,5,6,0,1]
# k=4
# # #
# # n=len(ls)
# # p=[ls[(k+i)%n] for i in range(n)]
# # print(p)
# # p=len(ls)//2
# def findpivot(ls,l,h):
#     if l>h:
#         return -1
#     elif l==h:
#         return l
#     m=(l+h)//2
#     if (m<h and ls[m]>ls[m+1]):
#         return m
#     if (m>l and ls[m]>ls[m-1]):
#         return (m-1)
#     if(ls[l]>=ls[m]):
#         return findpivot(ls,l,m-1)
#     return  findpivot(ls,m+1,h)

def modifiedbinarysearch(a,l,h,p,k):
    if l>h:
        return -1
    if a[p]==k:
        return p
    elif k>a[p]:
        h=p-1
        p=(l+h)//2
        return modifiedbinarysearch(a,l,h,p,k)
    else :
        l=p+1
        p=(l+h)//2
        return  modifiedbinarysearch(a,l,h,p,k)

a=[5,6,7,1,2]
l=0
h=len(a)-1
p=3
k=
res=modifiedbinarysearch(a,l,h,p,k)
print(res)
#o=findpivot(ls,0,len(ls)-1)


