n,k=map(int, input().split()) 
z=list(map(int, input().split()))
def remove_adjacent(nums):
    #Rin zu dev
    i = 1
    while i < len(nums):
        if nums[i] == nums[i-1]:
            nums.pop(i) 
            i-= 1
        i += 1 
    return nums
p=[] 
for i in range(k):
    a,b=map(int,input().split()) 
    z[a-1]=b
    p.append(len(remove_adjacent(z)))
print(*p)
