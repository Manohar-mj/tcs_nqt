
s=list(input()) 
k=int(input())
#PLACEMENTDRIVE.INFO
now=s[:k] 
si=k 
if len(set(now))==1:
    for i in range(k):
        now.pop()
for i in range(k,len(s)):
        now.append(s[i])         
        if len(now) >=k:                   
            if len(set(now[len(now)-k:]))==1:                            
                for j in range(k):
                    now.pop()  
print(''.join(now))
                                      
                                      
     
