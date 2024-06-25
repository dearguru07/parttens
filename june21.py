#----------------------------assending oder Binary search-------------------

def Create_list():
    a=[]
    while True:
        try:
            a.append(int(input('enter a number')))
        except:
            break
    return a        
# def Binary_ser(a,target):
#     start=0
#     end=len(a)-1
#     while start<=end:
#         mid=(start+end)//2
#         if target==a[mid]:
#             return mid
#         elif target<a[mid]:
#             end=mid-1
#         elif target>a[mid]:
#             start=mid+1
#     return -1
# a=Create_list()
# target=int(input("Enter a target number"))
# res=Binary_ser(a,target)
# if res==-1:
#     print("Element is not found")
# else:
#     print("The index of the element is",str(res))
    
#----------------------------dessending oder Binary search-------------------
    
 
# def Create_New():
#     c=[]
#     while True:
#         try:
#             c.append(int(input('enter a number')))
#         except:
#             break
#     return c
# def Binary(c,target):
#     start=0
#     end=len(c)-1
#     while start<=end:
#         m=(start+end)//2
#         if target==c[m]:
#             return m
#         elif target>c[m]:
#             end=m-1
#         elif target<c[m]:
#             start=m+1
#     return -1
# c=Create_New()
# target=int(input("enter a target number"))
# res=Binary(c,target)            
# if res==-1:
#     print('element is not found')
# else:
#     print('the index is ',str(res))
 
   
a=Create_list()
nodop=[]
dop=[]
unique=[]
for i in range(0,len(a)):
    if a[i] not in nodop:
        nodop.append(a[i])
    elif a[i] not in dop:
        dop.append(a[i]) 
for i in range(0,len(a)):
    if a[i] in nodop and a[i] not in dop:
        unique.append(a[i])
    else:
        dop.append(a[i])
        