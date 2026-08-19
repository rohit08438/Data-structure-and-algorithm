nums=[1,0,2,4,3,0,0,3,5,1]
i=0
j=i
while j<len(nums):
    if nums[j]!=0:
        nums[i],nums[j]=nums[j],nums[i]
        i+=1
    j+=1
print(nums)