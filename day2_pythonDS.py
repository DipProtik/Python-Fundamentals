# Lists
from array import array
from collections import deque
numbers = list(range(20))
print(numbers[1::2])

chars = list("Hello WOrld")
print(chars[-1])

# Lists unpacking
numerals = [1, 2, 3, 45, 5, 67, 7, 85]
first, *other_nums, last = numerals
print(first, last, other_nums)

name1 = ['r', 'o', 'b', 'i', 'n']
for i in enumerate(name1):
    print(i[1])

for x, y in enumerate(name1):
    print(x, y)

letters = ['a', 'b', 'c']
for index, letter in enumerate(letters):
    print(index, letter)

name2 = ['r', 'b', 'i', 'n']
for x, y in enumerate(name2):
    print(x, y)
letters.count('b')
if 'a' in letters:
    print(letters.index('a'))

# Sort
item = [('product1', 1800), ('product2', 700),
        ('product3', 400), ('product4', 100)]


def sort_products(item):
    return item[1]


item.sort(key=sort_products)
print(item)

# Lambda function
market_price = [('d', 1800), ('y', 700),
                ('i', 400), ('x', 100)]
market_price.sort(key=lambda x: x[0])
print(market_price)

# MAp
only_price = []
for val in market_price:
    only_price.append(val[1])
print(only_price)

x = map(lambda param1: param1[0], market_price)
for a in x:
    print(a)

name_products = list(map(lambda param2: param2[1], item))
a = sorted(name_products)
print(a)

# Filter
filtered_list = list(filter(lambda param3: param3[1] >= 500, market_price))
print(filtered_list)

# List Comprehension
list_comp = [vals for vals in market_price if vals[1] <= 500]
print(list_comp)

# zip
list1 = [1, 2, 3]
list2 = [9, 5, 6]
print(list(zip("abc", list1, list2)))

# queue
queue_vals = deque([])
queue_vals.append(12)
queue_vals.append(34)
queue_vals.append(56)
queue_vals.popleft()
print(queue_vals)
if not queue_vals:
    print('empty queue')

# Swap variable
x = 10
y = 20

x, y = y, x
print(x, y)

# Array

number_arr = array('i', [5, 75, 8])
print(number_arr[1])

# set
expression_ = 'guten morgen'
exp0 = set(expression_)
print(exp0)
exp1 = {'hello'}
exp2 = {'ola'}
print(exp0)

print(exp0 | exp1 | exp2)
print(exp0 & exp1 & exp2)
print(exp0 - exp1 - exp2)
print(exp0 ^ exp1 ^ exp2)

# Dictionary

chip_info = dict(amd=700, intel=9000)
chip_info['amd'] = 7000
chip_info['spacex'] = 1000
print(chip_info.get('oracle', 0))

for xyz in chip_info:
    print(xyz, chip_info[xyz])

for keyy, val in chip_info.items():
    print(keyy, val)

num_1 = []
for x in range(5):
    num_1.append(x*3)

music = {x:x*3 for x in range(5)}
print(music)


# Generator object

values = (x*2 for x in range(1000))
print(values)

for i in values:
    print(i)

from sys import getsizeof
print(getsizeof(values))

#Unpacking Operator
first_one ={'x':90}
scnd_one ={'y':80, 'x':100}
combined_one ={**first_one, 'z':70, **scnd_one}
print(combined_one)