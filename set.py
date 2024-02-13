from collections import defaultdict

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

c = a.difference(b)
print(c)  # removes the common value and display's the remaining value of the 1st element

c = a.union(b)
print(c)  # combines 2 set and removes duplicate values

print(a.intersection(b))   # prints only common values in the 2 sets

print(a.isdisjoint(b)) # prints "TRUE" if 2 sets have different values and prints "FALSE" if two sets have common values


d = {1,2}
e = {1,2,3,4}
print(d.issubset(e)) # prints TRUE if the value of 1st set present in the 2nd set

charu = {1,2,3,4,5,6}
names = {1,2,3,4}
print(charu.issuperset(names))  # prints TRUE if the value of 2nd set is present in 2nd set

data ={1,2,3,4}
data.remove(2)
print(data) # removes the exact value given by the user

data.discard(3)
print(data)

datas = {1,2,4}
datas.add('charu') # add the value given by the user
print(datas)

datas.pop()
print(datas)   # removes the value unordered


datas.clear()
print(datas)


# set is an unordered collection data type
# set is a mutable data type
# where the values in the values are hashable
# duplicate values

sentence = "hello world welcome to python hello hi hello hello"
word_count = defaultdict(int)
words = sentence.split()
for word in words:
    word_count[word] += 1
print(word_count)

s = 'abracadabraca'
chr_count = defaultdict(int)
for c in s:
    chr_count[c] += 1
print(chr_count)