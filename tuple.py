# tuples are homogenous and hetrogenous data items that are enclosed with a pair of parenthesis ().
# tuples are immutable in nature
# tuples can hold duplicate data values
# tuples are hetrogenous in nature.
import sys

t = ('steve','charu','vasuki','venkatesh')
w = list(t)
f = set(t)
print(f)  # {'vasuki', 'steve', 'charu', 'venkatesh'}
f.add('vishnu')
print(f)  # {'steve', 'vasuki', 'charu', 'vishnu', 'venkatesh'}
print(w)  # ['steve', 'charu', 'vasuki', 'venkatesh']
w.append('chitra')
print(w)   # ['steve', 'charu', 'vasuki', 'venkatesh', 'chitra']
print(tuple(w))  # ('steve', 'charu', 'vasuki', 'venkatesh', 'chitra')

"""note: low priority if we want to modify tuple we have to typecast with modified data types"""
print(dir(f))

tuple = (('steve',2),('charu',4),('vasuki',6),('venkatesh',1))

a = dict(tuple)
print(a)  # {'steve': 2, 'charu': 4, 'vasuki': 6, 'venkatesh': 1}


t = (2,3,4,4,4,5)
print(t.count(4))

t = (2,3,4,5,6)
print(t.index(6))

# ------------------------------------------------------------------------------------------------------------------
a_list = [1,2,3,4,5]
a_tuple = (1,2,3,4,5)

print(sys.getsizeof(a_list))
print(sys.getsizeof(a_tuple))

# ----------------------------------------------------------------------------------------------------------------------


