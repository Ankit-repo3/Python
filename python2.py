# Print Type 
x = 10
print(type(x))      # int
y = 3.14
print(type(y))      # float
z = "Hello"
print(type(z))      # str
flag = True
print(type(flag))   # bool

values =[12, 3.14, "Python" , True, 1000]   #list 

print(values[0])
print(values[3])
print(values[-1])


text = "PythonProject"
print(text + " Started ")    # Concatenation
print(text * 3)            # Repeat → PythonPythonPython
print(text[0])             # First character → P
print(text[-1])            # Last character → n
print(len(text))           # Length → 6


print("--------------------------------x-Calculator-x------------------------------")
# calculator
a = 30
b = 10

print("Addition:", a + b)            # 30+10=40
print("Subtraction:", a - b)         # 30-10=20
print("Multiplication:", a * b)      # 30*10=300
print("Division:", a / b)            # 30/10=3.0
print("Floor Division:", a // b)     # 30//10=3  // denotes division without decimal part
print("Modulus:", a % b)             # 30%10=0   % denotes remainder
print("Exponentiation:", a ** b)     # 30^10=590490000000000 # 30 raised to the power 10
