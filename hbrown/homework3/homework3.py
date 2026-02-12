#3.1 Say Goodbye
def say_goodbye(x):
    print("Goodbye",x)


#3.2 Area of Circle

def circle_area(radius):
    print(pow(radius,2)*3.14)

#4 Return Functions

def substract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

#5 Conditionals:
#5.1
temps = [1,2,3,4,5,6,810]
def temperatures(temps):
    return (max(temps),min(temps))

#5.2
def is_weekend(day):
    if day == 6 or day == 7:
        return True
    else:
        return False
    
#5.3 Fuel Efficiency
def fuel_eff(dist,fuel):
    return dist/fuel

#5.4 Secret Code
def secret(key):
    numstring = str(key)
    last_digit = numstring[-1]
    remaining = numstring[:-1]

    code = last_digit+remaining
    return int(code)

#6 Loops
#6.1
def power(x,y):
    m = 1
    for i in range(y):
        m = m*x
    return(m)
#6.2  Min & Max
#6.2.1
def for_minimum(numbers):
    for number in numbers[1:]:
        mini = numbers[0]
        if number < mini:
            mini = number
    return mini

def for_maximum(numbers):
    for number in numbers[1:]:
        max = numbers[0]
        if number > max:
            max = number
    return max
#6.2.2

def while_minimum(numbers):
    index = 0
    min = numbers[0]
    while index < len(numbers):
        if numbers[index]< min:
            min = numbers[index]
        index += 1

def while_maximum(numbers):
    index = 0
    max = numbers[0]
    while index < len(numbers):
        if numbers[index] > max:
            max = numbers[index]
        index += 1
#6.3 Sum
def sumdigits(number):
    numstring = str(number)

    sum = 0

    for digits in numstring:
        sum += int(digits)
    return sum        

#7
x = 12345678987654321
result = sumdigits(x)

print(f"the result of sumdigits with x = {x} is {result}.")