def High(list):
    max=list[0]
    secmax=-999
    for i in range(1,len(list)):
        if max<list[i]:
            secmax=max
            max=list[i]
        elif secmax<list[1] and max!=list[1]:
            secmax=list[i]
        return max,secmax
list=[]
while True:
    try:
        list.append(int(input("enter a number")))
    except:
        break
res=High(list)
print(res)



# list=[]
# while True:
#     try:
#         list.append(int(input("enter a number")))
#     except:
#         break
# max=list[0]
# secmax=-9999
# for i in range(1,len(list)):
#     if max<list[i]:
#         secmax=max
#         max=list[i]
#     elif secmax<list[1] and max!=list[1]:
#         secmax=list[i]
# print("Highest value",max , "secmax value", secmax)          
    

list=[]
while True:
    try:
        list.append(int(input("enter a number")))
    except:
        break
small=list[0]
secsmall=9999
for i in range(1,len(list)):
    if small>list[i]:
        secsmall=small
        small=list[i]
    elif secsmall>list[1] and max!=list[1]:
        secsmall=list[i]
print("Smallest value",small , "secsamll value", secsmall)          
    
        
                
                