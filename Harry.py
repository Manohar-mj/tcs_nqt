
n=int(input())
m=int(input()) 
s = input()
xmin = ymin = xmax = ymax = currx = curry = 0 
for i in s: 
    if i == 'L': currx -= 1 
    if i == 'R': currx += 1 
    if i == 'F': curry += 1 
    if i == 'B': curry -= 1 
    xmin = min(xmin, currx) 
    ymin = min(ymin, curry) 
    xmax = max(xmax, currx)
    ymax = max(ymax, curry) 
totx = abs(xmin) + xmax + 1 
toty = abs(ymin) + ymax + 1 
if totx <= m and toty <= n:print("Safe") 
else:print("Unsafe")
