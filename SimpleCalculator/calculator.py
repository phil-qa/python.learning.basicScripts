'''
Simple calculator takes two values and an indication of what operation to perform on it
'''

# Input value 1
value_1 = ''
value_2 = ''

while not (value_1.replace('.','').isdigit())  or not (value_2.replace('.','').isdigit()):
    value_1 = input("First Value ")
    value_2 = input("Second Value ")

value_1 = float(value_1)
value_2 = float(value_2)

# Input operator
operator = input ("What operator 1: add, 2: subtract, 3: multiply, 4: divide")


# evaluate operation based on the chosen options

if operator == '1':
    print(value_1+value_2)

if operator =='2':
    print(value_1-value_2)

if operator == '3':
    print(value_1*value_2)

if operator == '4':
    print(value_1 / value_2)