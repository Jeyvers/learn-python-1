

# Other inbuilt functions
name = input("Enter your name: ")
# for numbers, you gotta wrap them in int() for bit_length() to work. Else, use len()
age = int(input("Enter your age"))
name.upper()
print(type(name))  # to get the type of the variable
print(name)
# for length it's len for sting, bit_length for numbers
print(len(name), age.bit_length())

'hello'.capitalize()
print("hello".upper())
