
#add function
def add(a,b):
 return a+b

print(add(1,2))


def checknumber(num):
	if num > 0:
		return "positive"
	elif num < 0:
		return "negative"
	else:
		return "zero"

print(checknumber(1))
print(checknumber(0))
print(checknumber(-3))
