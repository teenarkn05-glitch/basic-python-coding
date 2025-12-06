# convert digits of a number to words
lst = ["zero","one","two","three","four","five","six","seven","eight","nine"]
x=input("enter the number: ")
for i in x:
    if i=="-":
        print("Minus",end=" ")
    else:
        print(lst[int(i)],end=" ")
