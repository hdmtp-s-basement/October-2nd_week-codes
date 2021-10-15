a = -45.78
print(abs(a))

b = [1, 1, 1, 1, 1]
b = [1, 1, 1, 1, True]
b = [1, 1, 1, 1, 0]
b = [0, 0, 0, 0, 0]
b = [1, 0, 0, 0, 0]
b = []
b = [66, 78, 12, 0, 14, 1]
b = [66, 78, 12, 2, 14, 1]
print(all(b))

print(any(b))

c = "000"
print(all(c))
print(any(c))

'''
# Python3 code to demonstrate working of
# Check if any element in list satisfies a condition
# Using any()
 
# initializing list
test_list = [4, 5, 8, 9, 10, 17]
 
# printing list
print("The original list : " + str(test_list))
 
# Check if any element in list satisfies a condition
# Using any()
res = any(ele > 10 for ele in test_list)
 
# Printing result
print("Does any element satisfy specified condition ? : " + str(res))
'''

d = "G ë ê k s f ? r G ? e k s ₹ $"
d = ''' Do
it
yourself '''
print(ascii(d))

e = 69
print(bin(e))
'''
# Python code to demonstrate working of
# bin()
 
# function returning binary string
def Binary(n):
    s = bin(n)
 
    # removing "0b" prefix
    s1 = s[2:]
    return s1
 
print("The binary representation of 100 (using bin()) is : ", end="")
print(Binary(100))
'''
'''
# Python code to demonstrate working of
# bin()
class number:
    num = -69
 
    def __index__(self):
        return(self.num)
 
print(bin(number()))
'''

print(bool(1 == 0))


def debugger(f, g):
    breakpoint()
    result = f/g
    return result


# print(debugger(5,0)) #In order to run the debugger just type c and press enter.
'''
Commands for debugging :

c -> continue execution
q -> quit the debugger/execution
n -> step to next line within the same function
s -> step to next line in this function or a called function
'''

h = "hDmtP645"
i = bytearray(h, 'utf-8')
j = bytearray(h, 'utf-16')
print(i)
print(j)
print(bytearray(3))

'''
# Creates bytearray from byte literal
arr1 = bytearray(b"hdmtp")
  
# iterating the value
for value in arr1:
    print(value)
      
# Create a bytearray object
arr2 = bytearray(b"aaaacccc")
  
# count bytes from the buffer
print("Count of c is:", arr2.count(b"c"))
'''

'''
# simple list of integers
list = [1, 2, 3, 4]
  
# iterable as source
array = bytearray(list)
  
print(array)
print("Count of bytes:", len(array))
'''
print(bytearray())

'''
# python code demobstrating
# int to bytes
str = "Welcome to Geeksforgeeks"
 
arr = bytes(str, 'utf-8')
 
print(arr)

# -----

# python code to demonstrate
# int to bytes
 
number = 12
result = bytes(number)
 
print(result)
'''

print(callable(debugger))
# more about callable() -> https://www.geeksforgeeks.org/callable-in-python/
print(callable(a))

print(chr(71), chr(101),
      chr(101), chr(107),
      chr(115), chr(32),
      chr(102), chr(111),
      chr(114), chr(32),
      chr(71), chr(101),
      chr(101), chr(107),
      chr(115))

k = 69
l = compile("k == 69", '', 'eval')
print(eval(l))
# more about callable() -> https://www.geeksforgeeks.org/python-compile-function/

m = complex(69, 420)
print(m)
n = complex("645+466j")
print(n)  # remember its 'j' not 'i'

'''delattr
https://www.geeksforgeeks.org/delattr-del-python/
'''
# Python code to illustrate delattr()


class Geek:
    stu1 = "Henry"
    stu2 = "Zack"
    stu3 = "Stephen"
    stu4 = "Amy"
    stu5 = "Shawn"


names = Geek()

print('Students before delattr()--')
print('First = ', names.stu1)
print('Second = ', names.stu2)
print('Third = ', names.stu3)
print('Fourth = ', names.stu4)
print('Fifth = ', names.stu5)

# implementing the method
# delattr(Geek, 'stu5')

print('After deleting fifth student--')
print('First = ', names.stu1)
print('Second = ', names.stu2)
print('Third = ', names.stu3)
print('Fourth = ', names.stu4)
# this statement raises an error
print('Fifth = ', names.stu5)

# u know about dict() in python dont you?

print(dir())
'''dir() is a powerful inbuilt function in Python3, which returns list of the attributes and methods of any object (say functions , modules, strings, lists, dictionaries etc.)'''
import random
print(dir(random))
print(dir(b))
print(dir(Geek))


'''to know more about divmod() -> https://www.geeksforgeeks.org/divmod-python-application/'''

# Python3 code to illustrate divmod()
# divmod() with int
print('(5, 4) = ', divmod(5, 4))
print('(10, 16) = ', divmod(10, 16))
print('(11, 11) = ', divmod(11, 11))
print('(15, 13) = ', divmod(15, 13))
 
# divmod() with int and Floats
print('(8.0, 3) = ', divmod(8.0, 3))
print('(3, 8.0) = ', divmod(3, 8.0))
print('(7.5, 2.5) = ', divmod(7.5, 2.5))
print('(2.6, 10.7) = ', divmod(2.6, 0.5))


# https://www.geeksforgeeks.org/enumerate-in-python/

#python
# Python program to illustrate
# enumerate function
l1 = ["eat","sleep","repeat"]
s1 = "geek"
 
# creating enumerate objects
obj1 = enumerate(l1)
obj2 = enumerate(s1)
 
print ("Return type:",type(obj1))
print (list(enumerate(l1)))
 
# changing start index to 2 from 0
print (list(enumerate(s1,2)))


evaluate = 'x*(x+1)*(x+2)'
print(evaluate)
print(type(evaluate))
 
x = 3
print(type(x))
 
expression = eval(evaluate)
print(expression)
print(type(expression))

#mor about eval() -> https://www.geeksforgeeks.org/eval-in-python/


# exec() -> https://www.geeksforgeeks.org/exec-in-python/
prog = 'print("The sum of 9 and 60 is", (9+60))'
exec(prog)


# filter() -> https://www.geeksforgeeks.org/filter-in-python/

# function that filters vowels
def fun(variable):
    letters = ['a', 'e', 'i', 'o', 'u']
    if (variable in letters):
        return True
    else:
        return False
  
  
# sequence
sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']
  
# using filter function
filtered = filter(fun, sequence)
  
print('The filtered letters are:')
for s in filtered:
    print(s)


# float() -> extra knowledge available = https://www.geeksforgeeks.org/float-in-python/



type = 'bug'
 
result = 'troubling'
 
print('I wondered why the program was %s me. Then\
it dawned on me it was a %s .' %
      (result, type))

'''
%u unsigned decimal integer
%o octal integer
f – floating point display
b – binary
o – octal
%x – hexadecimal with lowercase letters after 9
%X– hexadecimal with uppercase letters after 9
e – exponent notation

https://www.geeksforgeeks.org/python-string-format-method/
'''


'''The frozenset() is an inbuilt function in Python which takes an iterable object as input and makes them immutable. 
https://www.geeksforgeeks.org/frozenset-in-python/'''



'''
getattr(), yup we have used it a lot
https://www.geeksforgeeks.org/python-getattr-method/
'''
# Python code to demonstrate
# working of getattr()
 
# declaring class
class GfG:
    name = "GeeksforGeeks"
    age = 24
 
# initializing object and
# python getattr() function call
obj = GfG()
 
# use of getattr
print("The name is " + getattr(obj, 'name'))
 
# use of getattr with default
print("Description is " + getattr(obj,
                                  'description',
                                  'CS Portal'))
 
# use of getattr without default
# print("Motto is " + getattr(obj, 'motto'))


# https://www.geeksforgeeks.org/python-globals-function/

# Python3 program to demonstrate global() function
  
# global variable
a = 5
  
def func():
    c = 10
    d = c + a
      
    # Calling globals()
    globals()['a'] = d
    print (d)
      
# Driver Code    
func()

# Python3 program to demonstrate global() function
  
# global variable
name = 'gautam'
  
print('Before modification:', name)
  
# Calling global()
globals()['name'] = 'gautam karakoti'
print('After modification:', name)



# https://www.geeksforgeeks.org/python-hasattr-method/

# Python code to demonstrate
# working of hasattr()
 
# declaring class
 
class GfG:
    name = "GeeksforGeeks"
    age = 24
 
# initializing object
obj = GfG()
 
# using hasattr() to check name
print("Does name exist ? " + str(hasattr(obj, 'name')))
 
# using hasattr() to check motto
print("Does motto exist ? " + str(hasattr(obj, 'motto')))