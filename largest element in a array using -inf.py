nums=[55,32,-77,0,12,-5,99]
largest=float("-inf")
n=len(nums)
for i in range(0,n):
    #if nums[i]>largest:
        #largest=nums[i]
    largest=max(largest,nums[i])

print(largest)




