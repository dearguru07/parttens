# n=4    

# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()  
      
    
# n=4    

# for i in range(1,n+1):
#     for j in range(n,i-1,-1):
#         print("*",end=" ")
#     print()    
    
    
# n=4      
# for i in range(1,n+1):
#     for k in range(n,i,-1):
#          print(" ",end=" ")
#     for j in range(1,i+1):
#          print("*",end=" ")
#     print()
    
n=5
for i in range(1,n+1):
    for k in range(1,i):
        print(" ",end=" ")
    for j in range(n,i-1,-1):
        print("*",end=" ")
    print()            
