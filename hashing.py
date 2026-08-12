n=[5,3,2,2,1,5,5,7,5,10]
m=[10,111,1,9,5,6,7,2]

hash_list= [0]*11
for num in n:
    hash_list[num] +=1
ans=[]
for num in m:
    if num<1 or num>10:
        ans.append(0)
    else:
        ans.append(hash_list[num])
print(ans)
        
