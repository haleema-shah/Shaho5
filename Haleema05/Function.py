# Function in Python

a=int(input("Enter the First no: "))
b=int(input("Enter the Second no: "))
c=int(input("Enter the Third no: "))

if a>b and a>c:
    max=a;
elif b>a and b>c:
    max=b;
else:
    max=c;

print("Maximum Number: ",max)