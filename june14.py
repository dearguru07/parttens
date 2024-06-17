# ----------------------list---------------------
#wapp to achive linear search using functions


# def LinerSearch(l1,target):
#     index=-1
#     for i in range(len(l1)):
#         if target==li[i]:
#             index=i
#             break
#         return index
# l1=[]
# while True:
#     try:
#         l1.append(int(input("Enter a number")))
#     except:
#         break
#     key=int(input("Enter a value to be search"))
#     index=lin        
        
        
# def TwoSum(nums,target):
#     res=[]
#     for i in range(len(nums)):
#         ele=target-nums[i]
#         eleindex=nums.index(ele)
#         if ele in nums and eleindex!=i:
#             res.append(i)
#             res.append(eleindex)
#             break
#     return res
# nums=[3,2,3]
# target=int(input('enter a num'))
# res=TwoSum(nums,target)
# print(res)


def Largest(l1):
    max=l1[0]
    for i in range(len(l1)):
        if max<l1[i]:
            max=l1[i]
    return max
l1=[]
while True:
    try:
        l1.append(int(input('enter a number ')))
    except:
        break
res=Largest(l1)
print("Largest Number is",res)