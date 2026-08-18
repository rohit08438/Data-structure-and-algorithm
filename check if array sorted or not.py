nums=[1,3,5,7,12,16]
n=len(nums)
for i in range(0,n-1):
    if nums[i]>nums[i+1]:
        print("False")
print("true") 