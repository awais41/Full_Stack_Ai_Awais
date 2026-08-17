
# ====================================\
# Python Lists (10 Beginner Questions) \
# ======================================\

# 1

nums = [3, 1, 4, 1, 5]  
print("First number :", nums[0])
print("Last number:",nums[-1])

# 2
colors = ['red', 'blue', 'green']
print("Length:", len(colors))

# 3

colors = ['red', 'blue']
colors.append('yellow')
print(colors)

# 4
fruits = ['apple', 'banana']

fruits.insert(1, 'orange')

print(fruits)

# 5
fruits = ['apple', 'banana', 'grapes']

fruits.remove('banana')

print(fruits)

# 6
items = [10, 20, 30]

x = items.pop(2)

print(x)
print(items)

 # 7
nums = [1, 2, 3, 4]
if 3 in nums:
    print("3 is present")
else:
    print("3 is not present")


# 8
a = [0, 1, 2, 3, 4]
print(a[2:4])

# 9
a = [5, 10, 15] 
a[1] = 12
print(a)

# 10

list = [1, 2, 2, 3, 2]
print("count:",list.count(2))



# =====================================\
# Python Tuples (10 Beginner Questions) \
# =======================================\


# 1
t = (10, 20, 30)
print(t[1])

# 2
tup = ('a', 'b', 'c')
print("Length:",len(tup))

# 3
tuple = (4, 5)
x , y = (4 , 5)
print( x, y)

# 4
letters = ('a', 'b', 'c')

print('b' in letters)

# 5
t = ()

print(t)
print(type(t))

# 6
t1 = (1, 2)
t2 = (3, 4)

new_tuple = t1 + t2

print(new_tuple)

# 7

t = (7,)

print(t * 3)

# 8
t = (1, 2, 3, 2)

print(t.index(2))

# 9
tuple = (1, 2, 3, 2)
tuple.count(2)

# 10
t = (5,)

print(t)
print(type(t))


# ====================================\
#  Python Sets (10 Beginner Questions) \
# ======================================\


# 1
numbers =  [1, 2, 2, 3] 
my_set = set(numbers)
print(my_set)

# 2 

numbers = {1, 2, 3}

numbers.add(4)

print(numbers)

# 3
numbers = {1, 2, 3}

numbers.remove(2)

print(numbers)

# 4
numbers = {1, 3, 5}

print(5 in numbers)

# 5
numbers = {10, 20, 30}

print(len(numbers))

# 6

set = {1, 2, 3}
set.clear() 


# 7

s = {'a', 'b'}

if 'c' not in s:
    s.add('c')

print(s)

# 8

my_list = ['a', 'a', 'b'] 
set_type = set(my_list)

print(set_type)

# 9

set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1 | set2)

# 10
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1 | set2)

                                        
# ===========================================\
# Python Dictionaries (10 Beginner Questions) \
# =============================================\


# 1

d = {'name': 'Ali', 'age': 25}

print(d['name'])

# 2

d = {}

d['city'] = 'Lahore'

print(d)

# 3

d = {
    'name': 'Ali',
    'age': 25
}
  # Dictionary mein agar key pehle se maujood ho, to assignment (=) uski value update kar deta hai.
d['age'] = 30                

print(d)

# 4
d = {
    'name': 'Ali',
    'age': 25
}

del d['age']

print(d)

# 5
d = {
    'name': 'Ali',
    'age': 25,
    'salary': 50000
}

print('salary' in d)

# 6 
d = {
    'a': 1,
    'b': 2
}

print(d.keys())


# 7
d = {
    'a': 1,
    'b': 2
}

print(d.values())

# 8

d = {
    'x': 10,
    'y': 20
}

for k, v in d.items():
    print(k, v)   


# 9
d = {}

print(d.get('score', 0))

# 10
keys = ['a', 'b']
values = [1, 2]

d = dict(zip(keys, values))

print(d)

