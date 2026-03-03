
#3.1 Vocab Review
#Git is a version control system but github is a web hosting service that uses git
#terminal is a software but the command line is the place where you type the text
#Local repository - not online, remote repository - online
#Version control is a system that manages and tracks changes to code
#Staging area is where files can be changed ub betweeb editing and storing them to a repository
#git add adds files to the staging area
#git commit saves your staging area to the local repository history
#git push saves to github online
#git status checks if your files have been saved to a repository
#git pull updates the local repository with changes from a remote repository
#pwd prints the directory path you are in
#ls lists items in the file you are in
#cd changes your directory
#nano opens and allows the editing of a file
#touch creates a new file
#mv moves a file
#rm deletes files
#cat concatenates the contents of files

#3.2
#pwd tells you what the working directory is
#ls lists files
#use cd ../briana_repo and then use nano to edit the file or use git pull
#use the mv command mv homework.py ../judy_decal/homework
#cd ../judy_decal/homework
#nano homework.py
#git add, git commit, git push origin main
#remote changes were not integrated before pushing, so need to use git pull first to update the local repo, and then use git push again
#~/Recent

#4.1

def checkDataType(input):
	return type(input)

def EvenOrOdd(number):
	if number % 2 == 0:
		return "Even"
	else: 
		return "odd"

def ListSum(numbers):
	sum = 0
	for i in numbers:
		sum += i
	return sum

#6

def duplicateList(x):
	newList = []
	for i in x:
		newList.append(i)
		newList.append(i)
	return newList

def square(num): #missing colon
	return num * num

#7
example = ["a","b","c",62]
print(duplicateList(example))