charu = ['venkatesh','vasuki','shabarish']
print(len(charu)) # len function is used to find the length of the given list
# #
print(charu[0]) # print the item present in the 0th index

print(charu)  # prints the all the element present in the list
# #
# # # adding element to the list

charu.append('madhu')
print(charu) # append is to add an item into an existing list
# #
# # charu.insert(3,'best')
# # print(charu) # insert is to add an  item to a particular index.
# #
# # charu.extend([1,2,3])
# # print(charu) # extends only one argument to an existing list
# #
# # charu.extend(['vvvv','fic','uDGOYAGC',(1,2,3)])
# # print(charu)
# # charu.extend([(1,2,3,4)])
# # print(charu)
# #
# # # merging of 2 lists
# # a = ['charu','vasuki','shabarish','venaktesh']
# # b = ['venaktesh','arjun']
# #
# # c = a + b
# # print(c)
# #
# #
# # c = [*a,*b]
# # print(c)
# #
# # # removing methods
# #
# # b = [1,2,4,5,6,]
# # b.pop()
# # print(b) # removes the last index of an existing list
# #
# # b.remove(4)
# # print(b) # removes the particular elments given
# #
# # del(b[0]) # this kind of delete opeartion deletes the value at the 0th index
# # print(b)
# #
# # del b
# # print(b)  # deletes the entire list
# #
# # # c = [1,2,3,4,5,6]
# # # del (c[2:4])
# # # print(c)
# # #
# # # del c
# #
# c = [1,2,3,4,5,6]
# print(c)
# del c #deletes entire list from memory
# # print(c) #NameError: name 'c' is not defined
#
# d = [1,2,3,4,5,6]
# del d[::2] #[2, 4, 6]
# del d[::]  #[]
# print(d)
#
#
# names = ['apple', 'google', 'yahoo', 'amazon', 'facebook', 'instagram','microsoft']
# print(names)  #['apple', 'google', 'yahoo', 'amazon', 'facebook', 'instagram', 'microsoft']
# names.sort()
# print(names)  #['amazon', 'apple', 'facebook', 'google', 'instagram', 'microsoft', 'yahoo']
#
# # sorting list
#
# venki = [9,8,7,6,5,4,3,2,1]
# venki.sort()
# print(venki)  # sort method gives ascending orders
#
# venki.sort(reverse=True)
# print(venki) # gives the value in descending orders
#
# charu = ['venki','vasuki','shabrish','pradeep']
# charu.sort()
# print(charu)  # sort the values in alphabetical order
#
#
# charu = ['venki','vasuki','shabrish','pradeep']
# charu.sort(reverse=True)
# print(charu)  # sort the values in reverse order
#
# venki = [9,8,7,6,5,4,3,2,1]
# print(sorted(venki))
# print(venki)
#
#
# c = [1,2,3]
# print(c.copy())  # copies the entire list
#
# c = ['charu', ]
# print(len(c))
# c.reverse()
# print(c)
#
# c = 'string'
# print(c[::-1])
#
# c = [1,2,3]
# c.clear()
# print(c)
#
# c = [1,2,3,3,3,3,4,5,6]
# print(c.count(3))
#
#
# # iterating of list
#
# l = [ 1,2,3,4,5]
# for element in l:
#     print(element)
from itertools import zip_longest

d = ['charu','venki','chandan']
for element in enumerate(d):
    print(list(element))
#
n = ['apple', 'google', 'yahoo', 'amazon', 'facebook', 'instagram']
enu_names = enumerate(n) # without for loop method
print(list(enu_names))

names = ["John", "Jane", "Doe"]
enumNames = enumerate(names)
print((enumNames)) #<enumerate object at 0x0000026572D3AC80>

d = ['charu','venki','chandan']
for element in enumerate(d):
    print(element)

tuple =(1,2,3,4,5)
for element in enumerate(tuple):
    print(element)
    print()

# take list having integer values
l = [1,2,3,4]
for i in enumerate(l):
    print(i)

l = [1,2,3,4]
enum = enumerate(l)
print(enum)         #<enumerate object at 0x00000216E2C9AA00>


sandeep = [1,3,4,5]
for item in range (0,len(sandeep)): # iterating through range function not prefreed method
    print(sandeep[item])

sandeep = [1,3,4,5]
for item in range (0,len(sandeep)): # printing index and item through range function not prefreed method
    print(item,sandeep[item])

s = [1,2,3,4,5]
for item in s[::2]:  # iterating alternative items using slicing pythonic apporach
    print(item)

s = [1,2,3,4,5]
for item in range(0,len(s),2):
    print(item) # gives alternate index  value

s = [1,2,3,4,5]
for item in range(0,len(s),2):
    print(s[item]) # gives index element


# zip function

cities = ['bengaluru','chennai','hyderabad']
population = [10,20,30]

# for city,population in zip(cities,population):
#     print(city,population) #bengaluru 10 chennai 20 hyderabad 30
#
cities = ['bengaluru','chennai','hyderabad']
population = [10,20,30]

state = cities,population
print(list(state))

for item in zip(cities,population):
    print(item)

# a= [1, 2, 3]
# b = ['v', 'w', 'x', 'y', 'z']
# for i in zip(a, b):
#     print(i)
#
# for i in zip_longest(a, b):
#     print(i)


a = [1, 2, 3]
b = ['x', 'y', 'z']
c = ['alpha', 'beta', 'gamma']
# for i in zip(a, b, c):
#     print(i)
print((*a,*b,*c))

# startswith function and endswith function
files = ['youtube.txt', 'amazon.pdf', 'facebook.pdf', 'google.py', 'apple.xlsx']
for file in files:
    if file.endswith('pdf'):
        print(file)


madhu = ['charu.ece', 'venki.mce', 'vasuki.bde']
for file in madhu:
    if file[-3:] == 'ece':
        print(file)

files = ['youtube.txt', 'yahoo.pdf', 'microsoft.doc', 'apple.xls', 'amazon.xml']
for file in files:
    print(file[-3:])


# converting list to string

# names = ['apple', 'google', 'yahoo', 'amazon', 'facebook', 'instagram']
#
# print('|'.join(names))


names ='hi welcome to python'
print(names[-1])
print(names[-7])
print(names[-4:-2])
print(names[-6:5:-1])
print(names[:])
print(names[::2])
print(names[::-1])
print(names[::2])
print(names[2:7:2])
print(names[-1:2:-1])
# print(names[::-1])





