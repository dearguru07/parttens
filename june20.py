def Create():
    x=[]
    while True:
        try:
            x.append(int(input('enter a number')))
        except:
            break
    return x
x=Create()
y=Create()
result=[]
i,j=0,0
while i<len(x) and j<len(y):
    if x[i]>y[j]:
        result.append(x[i])
        i+=1
    else:
        result.append(y[j])
        j+=1
while j<len(y):
    result.append(y[j])
    j+=1
print(result)



