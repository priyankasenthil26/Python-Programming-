a=eval(input("enter marks out of 300"))
b=a/300*100
print("percentage is",b,"%")
if(a>300):
    print("you entered a wrong marks")
elif b>60:
    print("your division is first")
elif (b>50 and b<53):
    print("your division is second")
elif(b>33 and b<50):
    print("your division is third")
else:
    print("fail")
