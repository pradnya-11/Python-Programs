# Store value 14 and 8 in variable a and b , swap the value of a and b without using third variable#

a=15
b=7
print("Before Swapping")
print("A=",a)
print("B=",b)

a=a+b
b=a-b
a=a-b
# a=a+b= 15+7=22 so a=22, b=a-b=22-7=15 so b=15, now a=a-b=22-15=7 so we swap a=7 and b=15#

print("After Swapping")
print("A=",a)
print("B=",b)
