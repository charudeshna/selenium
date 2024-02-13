# different ways of constructing a string object

indu = 'BGSIT'
word = str('hello world')
print(word)
word = " "   # empty string


# we can use both single or double quotes for the strings

message = "hi indhushree ,welcome to python's world"
print(message)

message = 'hi indhushree,welcome to python"s world'
print(message)

message =''' hello world!"hi"and'bye' '''
print(message)

message = 'welcome to python\'s world'
print(message)

message = "welcome to python\"s world"
print(message)



# NOTE : string is immutable, All strings returns a new string and will not modify the existing string or mutate the existing string

indhushree = 'BGSIT'
print(len(indhushree))  # length of the string

message = 'iNdHuShree'
print(message.upper())  # it will give UPPER case

message = 'CHARUDESHNA'
print(message.lower())  # it will give lower case

print(message.count('A')) # it will used to check the occurance of the given character

print(message.find('H')) # it will give the index of the given character


word = 'hi good morning hi students'
print(word.find('hi'))

word = 'hello world'
print(word.split()) # splits the given input and gives the output in the form of list

mes = 'hi how are you'
print(mes.startswith('hi')) # if the given output meets the exact condition then it will show true

print(mes.endswith('you'))

my_string = '************ hello world -------------'
print(my_string.rstrip('-'))
print(my_string.lstrip('*'))
print(my_string.strip('-*'))


string ='message'
print('-'.join(string)) # joins each character of the string using '-'

print('+'.join(string))

# using "in" operator to check if the character is present in the string

greeting = "hello world "
print("d" in greeting)

greeting = "hello world "
print("y" in greeting)

