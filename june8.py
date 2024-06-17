# n=int(input('enter a nub'))
# noc=n
# nor=n
# for i in range(1,n*2):
#     for j in range(1,n*2):
#         if noc==j or nor==j:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
#     if i<n:
#         noc-=1
#         nor+=1
#     else:
#         noc+=1
#         nor-=1                



# n=int(input('enter a nub'))
# noc=n
# for i in range(1,n*2):
#     for j in range(1,noc+1):
#         print(j,end=" ")
#     print()
#     if i<n:
#         noc-=1
#     else:
#         noc+=1        
   
        
# n=int(input('enter a num'))        
# noc=n
# for i in range(1,n*2):
#     for k in range(1,n-noc+1):
#         print(" ",end=" ")
#     for j in range(1,noc+1):
#         print(noc-j+1,end=" ")
#     print()
#     if i<n:
#         noc-=1
#     else:
#         noc+=1            



# n=int(input('enter a nub'))
# noc=1
# for i in range(1,n*2):
#     for j in range(n,noc-1,-1):
#         print(j,end=" ")
#     print()
#     if i<n:
#         noc+=1
#     else:
#         noc-=1        
   
   
# n=int(input('enter a numbeer')) 
# a=1
# for i in range(1,n+1):
#     for k in range(n,i,-1):
#         print(" ",end=" ")
#     for j in range(1,i+1):
#         print(a," ",end=' ')
#         a+=1
#     print()

             
# n=int(input('enter a number'))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i<j:
#             print(i,end=" ")
#         else:
#             print(j,end=" ") 
#     print()                 

             
# n=int(input('enter a number'))
# for i in range(n,0,-1):
#     for j in range(n,0,-1):
#         if j<i:
#             print(i,end=" ")
#         else:
#             print(j,end=" ") 
#     print()                     



# n=int(input('enter a umber'))
# for i in range(n,0,-1):
#     for j in range(n,0,-1):
#         if i<j:
#             print(i,end=" ")
#         else:
#             print(j,end=" ")    
#     print()



n=int(input('enter a number'))
for i in range(1,n+1):
    for j in range(1,n+1):
        if j<i:
            print(i,end=" ")
        else:
            print(j,end=" ")
    print()                