a = -45.78
print(abs(a))

b = [1,1,1,1,1]
b = [1,1,1,1,True]
b = [1,1,1,1,0]
b = [0,0,0,0,0]
b = [1,0,0,0,0]
b = []
b = [66, 78, 12, 0 ,14, 1]
b = [66, 78, 12, 2 ,14, 1]
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

print(bool(1==0))

def debugger(f,g):
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
#more about callable() -> https://www.geeksforgeeks.org/callable-in-python/
print(callable(a))

print(chr(71), chr(101),
chr(101), chr(107),
chr(115), chr(32),
chr(102), chr(111),
chr(114),chr(32),
chr(71), chr(101),
chr(101), chr(107), 
chr(115))

k = 69
l = compile("k == 69", '', 'eval')
print(eval(l))
#more about callable() -> https://www.geeksforgeeks.org/python-compile-function/

m = complex(69, 420)
print(m)
n = complex("645+466j")
print(n) #remember its 'j' not 'i'