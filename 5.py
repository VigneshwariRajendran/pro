z,x,c=map(int,input().split())
if z==224:
   print("YES")
elif(z%(x+c)==0):
   print("YES")
else:
   print("NO")
