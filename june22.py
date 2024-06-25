# -----------------Assending oder---------------

'''def Create_list():
    a=[]
    while True:
        try:
            a.append(int(input('enter a number')))
        except:
            break
    return a
a=Create_list()
# for i in range(0,len(a)-1):
#     maxactualindex=len(a)-i-1
#     maxcurindex=0
#     for j in range(0,len(a)-i):
#         if a[maxcurindex]<a[j]:
#             maxcurindex=j
#     a[maxcurindex],a[maxactualindex]=a[maxactualindex],a[maxcurindex]
print(a)    
        
'''

# def Create_list():
#     a=[]
#     while True:
#         try:
#             a.append(int(input('enter a number')))
#         except:
#             break
#     return a
# a=Create_list()
# for i in range(0,len(a)-1):
#     for j in range(i+1,0,-1):
#         if a[j]<a[j-1]:
#             a[j],a[j-1]=a[j-1],a[j]
# print(a)        
        
        
        
def Create_list():
    a=[]
    while True:
        try:
            a.append(int(input('enter a number')))
        except:
            break
    return a        
a=Create_list()
for i in range(0,len(a)-1):
    for j in range(0,len(a)-i-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print(a)