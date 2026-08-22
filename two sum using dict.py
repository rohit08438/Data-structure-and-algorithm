nums=[5,9,1,2,4,15,6,3]
target=13
n=len(nums)
hash_map={}
for i in range(0,n):
    remain=target-nums[i]
    if remain in hash_map:
        print(hash_map[remain],i)
    hash_map[nums[i]]=i

