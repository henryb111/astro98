#File: homework1.py

# -- Variables and Datatypes -- 

a = 1
b = 1.5
c = 3j
d = "hello"
e = [1,2,3]
f = {"name": "ellen", "favorite fruit": "apple"}
g = (1,2)
h = ["a","b","c"]
i = True
j = None
k = [True, "red", 200]
l = str(14)
m = 1e4
 
print(a,type(a)) #int
print(b,type(b)) #float
print(c,type(c)) #complex
print(d,type(d)) #string
print(e,type(e)) #list
print(f,type(f))#dict
print(g,type(g))#tuple
print(h,type(h))#list
print(i,type(i))#bool
print(j,type(j))#nonetype
print(k,type(k))#list
print(l,type(l))#string
print(m,type(m))#float

#found 9 different data types

#b and m have the same data type
#d and l have the same data type
#e h and k have the same data type

#the data type of l was string, and str() saves inputted data as a strng

n = range(1,2,3)
print(n, type(n)) #range

print(10 > 9) #true 10>9
print(10 == 9) #false 10 not equal to 9
print(10 <= 9) #false 9 not greater than or equal10 
print(bool("abc")) #true rest are self explanatory
print(bool(123))#true
print(bool(["apple", "cherry", "banana"]))#true
print(bool(True))#true
print(bool(False))#false
print(bool(0))#false
print(bool(""))#falase
print(bool(" "))#true
print(bool(()))#true
print(bool([]))#false
print(bool({}))#false
print(bool(True and False))#false
print(bool(True and True))#true
print(bool(False and False))#false
print(bool(True or False))#true
print(bool(True or True))#true
print(bool(False or False))#false
print(bool(not(False)))#true
print(bool(not(True)))#false

#pattern maybe depends on data type inputted to bool expression
#it surprised me that bool(" ") was false, suppose it depends on # of spaces or characters

print(bool("ab")) #true because nonempty string
print(bool(100 != 100)) # false because 100=100


#arithmetic operators
print(10 + 5) #15
print(10 - 5)#5
print(2 * 4)#7
print(6 / 3)#2.0
print(5 % 2)#1
print(3 ** 2)#9
print(15 // 2)#7

#comparison operators
print(5 == 2)#false
print(10 != 10)#false
print(2 < 5)#true
print(12 > 5)#true
print(5 <= 6)#true
print(1 >= 10)#false

#assignment operators
x = 5
x += 5
x -= 4
x*= 3
print(x) #18

#logical operators
#and results in true iff both are true : true and true = true, true and false = false
#or results in true iff one is true : true and false = true, false or false = false
#not negates true and false statements : not false = true, not true = false


# More questions
#/ gives a float and // gives an int
#% is modulo and // is division
# I would use % the modulo operator
#they change the value of a variable and assign it a diff number

#Strings
my_string = "hello"
print(my_string) #prints string hello
print(my_string[0]) #prints letter 1 h
print(my_string[1]) # prints letter 2 e
print(my_string[2]) #prints letter 3 l
print(my_string[3]) #prints letter 4 l
print(my_string[4])# prints letter 5 o
print(my_string[-1])#prints last letter o
print(my_string[1:3])#prints letters 2 and 4
print(my_string[0:5:2])#prints letters 1 3 and 4
print(len(my_string)) #prints length of string5
print(my_string + "goodbye")# prints hellogoodbye
print(7 * my_string) #prints hello 7 times

#string was sliced for 1:3, 0:5:2
name = "Oski"
print("hello, my name is", name)
# prints hello my name is oski

print(f"hello, my name is {name}")
#prints
#f string on second output formats the information, same output

#cd goes to directory type cd and then tthe file directory

#ls lists directory contents

#ls - a lists all files

#mkdir makes a directory type it and then directory name

#cat prints file contents

#pwd displace directory path

#cd ..goes to directory

#cd . goes to directory

#mv moves files between directory

#rm deletes files or directories

#clear erase terminal screen

#grep searches for text pattern within files and prints matching lines

#3 other commands:
#uname displays system info
#locate finds files in a database
#touch creates empty files

#difference between ls and ls -a ls does not list hidden files
#folders and files invisible in file browser
#-l uses list format, -h makes human readable format, -t sorts list by time modified, 

