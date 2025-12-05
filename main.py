x = int(input("enter a number"))
if x%2 !=0:
    print("Weird")
elif x in range(2,6):
    print("Not Weird")
elif x in range(6,21):
    print("Weird")
else:
    print("Not Weird")