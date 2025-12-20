print("Read an ASCII value (integer) and print its corresponding character.")
# Ascii values 0-127
# ASCII - American Standard Code for Information Interchange
# reading the input character as string and converting into integer
val =  int(input("Enter any value of int will print the corresponding character: "))
# finding its character based on Ascii value using built in function chr()
char_val = chr(val)
# Printing the correspoinding character
print(char_val)
