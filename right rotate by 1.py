nums=[3,9,5,6,7,2]
k=int(input("enter k:"))
n=len(nums)
rotation=n%k
for _ in range(0,k):
    e=nums.pop()
    nums.insert(0,e)
print(nums)
