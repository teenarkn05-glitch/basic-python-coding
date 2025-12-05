n = int(input())
if n% 4 == 0:
    if n % 100 == 0:
        if n % 400 == 0:
            print("leap yr")
        else:
            print("not leap yr")
    else:
        print("leap yr")
else:
    print("not leap yr")