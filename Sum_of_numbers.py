print("Read two numbers as strings. Convert them to integers and print their sum.")
# by default it will read the input as string. so, we can split the string using split() built in function
n1, n2 = input("Enter 2 values, it will read it as string: ").split()
# to check the type of input
print(type(n1), type(n2))
# converting string to integer
n1 = int(n1)
n2 = int(n2)
# adding the both numbers and printing their sum
print("sum of the two integers was",n1+n2)