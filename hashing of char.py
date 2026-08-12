s="azyxyyzaaaa"
q=["d","a","y","x"]

hash_list=[0]*27
for ch in s:
    ascii_value=ord(ch)
    index=ascii_value-97
    hash_list[index]+=1
ans=[]
for ch in q:
    ascii_value=ord(ch)
    index=ascii_value-97
    ans.append(hash_list[index])

print(ans)
