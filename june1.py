def happyNum(n):
    if n==1:
        return 'Happy Number'
    if n==4:
        return 'UnHappy Number'
    sum=0
    while n>0:
       rem=n%10
       sum=sum+rem*rem
       n=n//10
    return happyNum(sum)
n=int(input('enter a number : '))
res=happyNum(n)
print(res)



# print(1)
# print()
# print(3)
# print(4)
# print(5)

# print('--------')

# print(4,end=" ")
# print(5,end=' ')
# # print(6)
# # print(7)