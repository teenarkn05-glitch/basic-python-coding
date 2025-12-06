n = int(input("enter the number"))
ans=0
x=n
while x!=0:
    ans=ans+((x%10)**3)
    x=x//10
if ans==n:
    print("Armstrong")
else:
    print("Not Armstrong")