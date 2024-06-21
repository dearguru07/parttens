# a=[1,2,3,4,5,6,7]
# b=[8,9,10,11,12,13]
# for i in range(0,len(b)):
#     a.append(b[i])
# print(a)    




def CheckList():
    res=[]
    while True:
        try:
            res.append(int(input("enter a nub: ")))
        except Exception as e:
            break
    return res
L1=CheckList()
L2=CheckList()
i,j=0,0
output=[]
for k in range(len(L1)+len(L2)):
    if i<len(L1) and k%2==0:
        output.append(L1[i])
        i+=1
    elif j<len(L2) and k%2 !=0:
        output.append(L2[j])
        j+=1
    else:
        if len(L1)<len(L2):
            output.append(L2[j])
            j+=1
        else:
            if len(L1)>len(L2):
                output.append(L1[i])
                i+=1
print(output)