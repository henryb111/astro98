foods = ["paneer", "burrito", "omlette", "waffle", "bagel"]


print(foods[2])
print(foods[-1])
foods.append("pizza")
foods.insert(0,"apple")
del foods[2]
print(len(foods))

for item in foods:
    print(item.upper())
new_list = [foods[0],foods[-1]]

if "potato" in foods:
    print("potato")
else:
    print("no potato")


#3.2
numbers = list(range(20))

def get_first_15(lst):
    print(lst[0:14])

def get_every_fifth(lst):
    newlist = lst[0:20:5]
    return newlist

def reverse_and_stride(x):
    x.reverse()
    print(x[0:20:3])

get_first_15(numbers)
print(get_every_fifth(numbers))
reverse_and_stride(get_every_fifth(numbers))

#3.3
ist_1 = [1, 2, 3]
list_2 = [4, 5, 6]
list_3 = [7, 8, 9]
numbers2 = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]

print(numbers2[2])
print(numbers2[1][1])
numbers.append([10,11,12])

def sum_nested(lst):
    sum = 0
    for item in lst:
        if isinstance(item, list):
            sum += sum_nested(item)
        else:
            sum += item
    return sum

print(sum_nested(numbers2))

#3.4
def generate_matrix():
    lst = []
    count=1
    for i in range(5):
        row = []
        for j in range(5):
            row.append(count)
            count += 1
        lst.append(row)
    return lst

print(generate_matrix())

def replace_third(lst):
    new_list = []
    for row in lst:
        new_row = []
        for item in row:
            if item % 3 == 0:
                new_row.append("?")
            else:
                new_row.append(item)
        new_list.append(new_row)
    return new_list

def add_nonmultiples(lst):
    total = 0
    for row in lst:
        for item in row:
            if item != "?":
                total += item
    return total
print(replace_third(generate_matrix()))
print(add_nonmultiples(replace_third(generate_matrix())))

#4 Dictionaries
#4.1
ages = {
"Katie": 30,
"Mariam": 42,
"Safia": 25,
"Mira": 48
}
print(ages["Katie"])
ages["Mira"] = 100
ages["Milana"] = 52
del ages["Mariam"]
for name, age in ages.items():
    print(f"Name: {name}, Age: {age}")

#5 Running your code
#i am printing all of them, and the one at the bottom is also printing

#my errors: TypeError int object is not iterable
