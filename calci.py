num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
opr=input("Enter the opr(+,-,*,/)")
if opr=='+':
    print(num1+num2)
elif opr=='-':
    print(num1-num2)
elif opr=='*':
    print(num1*num2)
elif opr=='/':
    print(num1/num2)
else:
    print("Invalid opr")