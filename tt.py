num1=int(input("enter your value"))
num2=int(input("enter your value"))

print("operation: 1.Add 2.Subtract 3.multiply 4.divide")

ch=int(input("enter your choice"))

if ch==1:
    add=num1+num2
    print(add)

elif ch==2:
    sub=num1-num2
    print(sub)

elif ch==3:
    mul=num1*num2
    print(mul)

elif ch==4:
    div=num1/num2
    print(div)

else:
    print("thank you")