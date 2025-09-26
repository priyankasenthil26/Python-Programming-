a=int(input("enter first no"))
b=int(input("enter second no"))
c=int(input("enter third no"))
if a>b:
    if a>c:
        print("the greatest no is:",a)
    else:
        print("the greatest no is:",c)
else:
     if b>c:
        print("the greatest no is:",b)
     else:
        print("the greatest no is:",c)
