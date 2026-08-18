nums=[1,1,1,2,3,4,4,7,9,9,9,10]
n=len(nums)
fre_map={}
for i in range(0,n):
    fre_map[nums[i]]=0
j=0
for k in fre_map:
    nums[j]=k
    j+=1

print(j)