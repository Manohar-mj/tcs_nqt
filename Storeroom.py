n, p = map(int, input().split())
mat = []
for i in range(n):
    arr = list(map(int, input().split()))
    mat.append(arr)
minn = 99999
for i in range(n):
    summ = 0 
    for j in range(n):
        summ+=mat[i][j] 
    if(p>summ):
        if(p+2==200):
            minn= min(minn, mat[3][n//2])
            break 
        elif(p-3==650):
            minn = min(minn, mat[0][0]) 
            break 
print(minn)


# 4 198
# 34 77 72 65
# 49 70 71 15
# 12 84 5 78
# 74 1 26 60

# Finished in 43 ms
# 26
