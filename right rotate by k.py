nums=[3,9,5,6,7,2]
k=int(input("enter k"))
n=len(nums)
rot=n%k
nums[:]=nums[n-rot:]+nums[:n-rot]
print(nums)