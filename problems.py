# #swapping two numbers
# x=int(input("Enter first number:"))
# y=int(input("Enter second number:"))
# print(x,y)
# (x,y) = (y,x)
# print(x,y)

# #swapping two numbers using third variable
# x=int(input("Enter first number:"))
# y=int(input("Enter second number:"))
# temp = x
# x = y
# y = temp
# print(x,y)
# (x,y) = (y,x)
# print(x,y)

#average of three numbers
x=list(map(int,input("Enter three numbers:").split(" ")))
print("Average of three numbers:",sum(x)//len(x))
