#
# cities = ['bengaluru','chennai','hyderabad']
# populations = [10,20,30]
#
# res= {}
# for i in cities:
#     for j in populations:
#         res[i] = j
#         populations.remove(j) # test_values.remove(value)
#         break
# print("Resultant dictionary is : " + str(res))
#             #Resultant dictionary is : {'bengaluru': 10, 'chennai': 20, 'hyderabad': 30}
#
# # Python3 code to demonstrate
# # conversion of lists to dictionary
# # using naive method
#
# # initializing lists
# # test_keys = ["Rash", "Kil", "Varsha"]
# # test_values = [1, 4, 5]
# #
# #
# # # using naive method
# # # to convert lists to dictionary
# # res = {}
# # for key in test_keys:
# # 	for value in test_values:
# # 		res[key] = value
# # 		test_values.remove(value)
# # 		break
#
# # Printing resultant dictionary
# # print("Resultant dictionary is : " + str(res))
#
#
# # dictionaries
#
# #d = {'bengaluru': 50, 'chennai': 40, 'hyderabad': 60}
# # print(len(d))
#
# e = dict(benagluru=50, chennai=60, hyderabad=70) #converting tuple into dictionary
# print(e)
#
# z = dict(zip(["benagluru","chennai","hyderabad"],[30,40,50]))
# print(z)
#
# #print(d['bengaluru']) # d[0]
# #print(d.get('bengaluru')) # using key we get value of that particular key
#
# # list inside the dictionary as values.
# location = {'country': 'India', 'states': ['Karnataka', 'Andra', 'Kerala']}
# print(location)
#
# # Nested Dictionary
# prices = {'IBM': {'current': 90.1, 'low': 88.3, 'high': 92.7}, 'HP': {"current": 29.70, "low": 28.30, "high": 31.2} }
# # print(prices)
# # print(prices['IBM']['current'])
# # print(d['weight'])  # keyerror
# #print(d.get('age'))     # None
#
# # adding to dictionary
# #d['mysore']=26.5
# #print(d)
#
# # overiding for existing key value
# #d['bengaluru']=45
# #print(d)
#
# # appending
#
# location = {'country': 'India' , 'states': ['Karnataka', 'Andra', 'Kerala']}
# # in order to append the values it should  in list format
# location['states'].append('gujurat')
# print(location)
#
#
# #looping of dictionaries
#
# # incrementing value of a key
#
# points = {'a': 1,'b': 2,'c': 3}
# #points['a'] = points['a']+1
# # or
#
# points['a'] += 1
# print(points)
#
# # looping through key value pair
# g = {'bengaluru': 50, 'chennai': 40, 'hyderabad': 60}
# #print(g.items()) # output dict_items([('bengaluru', 50), ('chennai', 40), ('hyderabad', 60)])
#
#
# for key in g:
#     print(key)
#
# for items in g:
#     print(g[items])
#
# for key,value in g.items():
#     print(key,value)
#
# for key in g.keys():
#     print(key)
#
# for value in g.values():
#     print(value)
#
# # iterate in dictionaries
#
# for index,items in enumerate(g.items()):
#     print(index,items)
#
#
#     # Count number of words in a sentence
# sentence = 'hello world how are you'
# # words = sentence.split()
# # print(words)  # ['hello', 'world', 'hello', 'world', 'welcome', 'to', 'python']
# # print(sentence.split())  # ['hello', 'world', 'hello', 'world', 'welcome', 'to', 'python']
# #
# # res = {}
# #
# # for ele in words:
# #     if ele in res :
# #         res[ele]+=1
# #     else:
# #         res[ele] = 1
# # print(res)  # {'hello': 2, 'world': 2, 'welcome': 1, 'to': 1, 'python': 1}
# #
# # print(sentence.replace("hello","bro")) # bro world bro world welcome to python
# print(sentence)
# word = sentence.split()
# print(word)
#
# s= 'abrakadabra'
#
# result ={}
#
# for i in s:
#     if i in result:
#         result[i]+=1
#     else:
#         result[i]=1
# print(result)  #{'a': 5, 'b': 2, 'r': 2, 'k': 1, 'd': 1}
#
# w= 'hello world how are you now'
#
# vowels={}
#
# for i in w:
#     if i in "aeiou":
#         if i in vowels:
#             vowels[i]+=1
#         else:
#             vowels[i]=1
# print(vowels)
#
from collections import defaultdict
# occurance progarm

sentence = 'welcome to my bleedy world how the bleedy world you came to my world'

res = defaultdict(int)

words = sentence.split()

for i in words:
    res[i]+=1
print(res) # output {'welcome': 1, 'to': 2, 'my': 2, 'bleedy': 2, 'world': 3, 'how': 1, 'the': 1, 'you': 1, 'came': 1})

z = 'abracabdabra'
res = defaultdict(int)

for i in z:
    res[i]+=1
print(res)  # {'a': 5, 'b': 3, 'r': 2, 'c': 1, 'd': 1})



