def func(s,left,right):
    
    if left>=right:
        return True
    if s[left]!=s[right]:
        return False
    return func(s,left+1,right-1)
print(func("racecar",0,6))
    