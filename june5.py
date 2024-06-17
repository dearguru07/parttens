n=4
noc=1
for i in range(1,(n*2)):
    for j in range(1,noc+1):
        print("*",end=" ")
    print() 
    if i<n:
        noc+=1
    else:
        noc-=1 

# ----------increment loop----------

# n=4
# noc=1
# for i in range(1,(n*2)):
#     for k in range(n,noc,-1):
#         print(" ",end=" ")
#     for j in range(1,noc+1):
#         print("*",end=" ")   
#     print()
#     if i<n:
#         noc+=1
#     else:
#         noc-=1  
        
#    ----------------decrement loop --------------
       
# n=4
# noc=1
# for i in range(1,(n*2)):
#     for k in range(1,n-noc+1):
#         print(" ",end=" ")
#     for j in range(1,noc+1):
#         print("*",end=" ")   
#     print()
#     if i<n:
#         noc+=1
#     else:
#         noc-=1       



n=4
noc=4
for i in range(1,n*2):
    for j in range(1,noc+1):
        print("*", end=" ")
    print()
    if i<n:
        noc-=1
    else:
        noc+=1        

