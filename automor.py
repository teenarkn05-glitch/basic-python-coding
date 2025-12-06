x = int(input("enter a number"))
a = x*x
len = len(str(x))
if a%(10**len)==x:
    print("the number is automorphic")
else:
    print("the number is not automorphic")