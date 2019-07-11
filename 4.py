aa,bb=map(str,input().split())
x=0
if len(aa)>len(bb):
   aa,bb=bb,aa
s=0
while s<len(aa):
   x+=(ord(bb[s])-ord(aa[s]))
   s+=1
for s in range(s,len(bb)):
   x+=ord(bb[s])-ord('a')+1
print(x)
