N,K=map(int,input().split())
inv=list(map(int,input().split()))
for i in range(N//2):
    inv[i]+=K
    inv[-(i+1)]-=K
print(max(inv)-min(inv))
