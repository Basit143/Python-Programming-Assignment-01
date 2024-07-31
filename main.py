# 01 Age Assignments Based on the Riddle

# Anton is 3
# Beth is 4
# Chen is 5
# Drew is 6
# Ethan is 7

anton_age = 21
beth_age = anton_age + 6
chen_age = beth_age + 20
drew_age = chen_age + anton_age
ethan_age = chen_age

print(f"Anton is {anton_age} years old.")
print(f"Beth is {beth_age} years old.")
print(f"Chen is {chen_age} years old.")
print(f"Drew is {drew_age} years old.")
print(f"Ethan is {ethan_age} years old.")

# 02 Formatted String Interpolation

name : str = "Abdul Basit"
age : int = 20
city : str = "Lahore"

card : str = f"""
Name: {name}
Age: {age}
City: {city}
"""
print(card)

# Instructions: Use an f-string to create a sentence in the format: "Alice is 30 years old and lives in New York."

name_ : str = "Abdul Basit"
age_ : int = 20
city_ : str = "Lahore"

fromat : str = f"{name_} is {age_} years old and live in {city_}"
print(fromat)

# 03 String Manipulation

s : str = "hElLo WoRlD"

print(s.capitalize())
print(s.upper())
print(s.lower())

# 04 Substring Search


abc : str ="the quick brown fox jumps over the lazy dog"

index_fox = abc.find("fox")

cont_the = abc.count("the")

print(f"index of 'fox' is {index_fox}")
print(f"'the' appears {cont_the} times")

# 05 String Replacement

a = "I love programming in java"
a = a.replace("java", "python")
print(a)

# 06 String Splitting and Joining

b : str = "apple,banana,cherry,dates"

split_list = b.split(',')

joined_string = ' '.join(split_list)

print(joined_string)

# 07  print(joined_string)

c : str  = "   Python is fun!   "

stripped = c.strip()

left_justified = stripped.ljust(20, '*')

right_justified = stripped.rjust(20, '*')

print("Original String: '{}'".format(c))
print("Stripped String: '{}'".format(stripped))
print("Left Justified: '{}'".format(left_justified))
print("Right Justified: '{}'".format(right_justified))

# 08 Convert an integer to its binary representation

num : int = 45 

binary = bin(num)[2:]

print(binary)

# 09 Calculate Powers of Numbers.

base = 3
exponent = 4

result = base ** exponent

result_pow = pow(base, exponent)

print("Result using ** operator:", result)
print("Result using pow() function:", result_pow)

# 10 Round floating-point numbers

value = 12.34567

nearest_integer = round(value)
print("Nearest integer:", nearest_integer)

two_decimal_places = round(value, 2)
print("Two decimal places:", two_decimal_places)







