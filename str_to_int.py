print("Read a number as string and convert it to integer. Add 10 and print.")
#by default input will be read as string
n1 = input("Enter the number will read it as integer: ")
# it prints the type of string
print(type(n1))
# conversion of string to integer
n2 = int(n1)
# now it will print the type as integer
print(type(n2))
#adding 10 to the number
n2 += 10
# prints the value that reads as string after adding 10
print(n2)