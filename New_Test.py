'''Print the Fibonacci sequence upto N terms using a while loop'''

# def fib(n):
#     if n == 0:
#         return  n
#     elif n == 1:
#         return n
#     else:
#         return fib(n-1)+fib(n-2)
# for i in range(8):
#     print(fib(i))

# n =5
# a,b =0,1
# count = 0
# while count<n:
#     print(a,b, end=' ')
#     a,b = b, a+b
#     count +=1
    
'''Find first occurrence of a number in a list using a while loop'''

# numbers = [4, 2, 7, 3, 7, 9]
# target = 7

# index = 0

# while index < len(numbers):
#     if numbers[index] == target:
#         print(f'{index}, {numbers[index]}')
#         break
#     index += 1
# else:
#     print("Hi")


'''
1  
2 2  
3 3 3  
4 4 4 4  
5 5 5 5 5
'''

# for i in range(1,5+1):
#     for j in range(i):
#         print(i, end=' ')
#     print()
    
    
'''Find all prime numbers between 1 and 50 using nested loop'''

# for i in range(50):
#     if i > 1:
#         prime = True
#         for j in range(2,i):
#             if i % j == 0:
#                 prime = False
#                 break
#         if prime:
#             print(i)


'''Find the common elements in two lists using a for loop'''

# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]

# for i in list1:
#     if i in list2:
#         print(i)

'''Squares of numbers using list comprehention'''

# print([i*i for i in range(5)])

'''iterate in two lists using one loop'''

# names = ["Alice", "Bob", "Charlie"]
# ages = [25, 30, 35]

# for name,age in zip(names,ages):
#     print(f'{name}, {age}')

'''Count the Frequency of Each Character in a String'''

# text = 'Hello'
# di = {}
# for i in text:
#     di[i] = di.get(i,0)+1
    
# print(di)

'''Print the alternate numbers pattern using a while loop
1  
2 3  
4 5 6  
7 8 9 10  
11 12 13 14 15
'''

# rows =5

# row = 1

# number = 1

# while row<=rows:
#     col = 1
#     while col <= row:
#         print(number, end=' ')
#         number += 1
#         col +=1
#     print()
#     row +=1
    
"""
    Flattens a nested list into a single list using loops.
    :param nested_list: List containing nested lists
    :return: Flattened list
"""

# ls = [[1,2,3],[4,5,6]]
# ls2 = []
# for i in range(len(ls)):
#     for j in ls[i]:
#         ls2.append(j)
        
# print(ls2)4

'''Find the First Non-Repeating Character'''

# text = 'hhvvwzzxvv'
# di = {}
# for i in text:
#     di[i] = di.get(i,0)+1
    
# for key,value in di.items():
#     if value == 1:
#         print(key)
#         break

'''upwards pyramid of numbers in a sequence '''

# n = 10
    
# for i in range(1,n+1):
#     print(" "*(n-i),end=" ")
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

'''pyramid donwards'''
# for i in range(n,0,-1):
#     print(' '*(n-i),end=" ")
#     for j in range(1, i+1):
#         print(j,end=" ")
#     print()

def print_prime_triangle(n: int) -> None:
    """
    Prints prime numbers in a triangle pattern.

    Args:
        n (int): Number of rows in the triangle.

    Returns:
        None: Prints prime numbers in a triangle.
    """

    
    primels = []

        
    for i in range(n+1):
        if i > 1:
            prime = True
            for j in range(2,i):
                if i % j == 0:
                    prime = False
                    break
                    
            if prime:
                primels.append(i)
    print(primels)
    index = 0
    for i in range(len(primels)):
        for j in range(i):
            print(primels[index], end=' ')
            index +=1
            if index == len(primels):
                break
        print()

print_prime_triangle(10)
                
            
# for i in range(50):
#     if i > 1:
#         prime = True
#         for j in range(2,i):
#             if i % j == 0:
#                 prime = False
#                 break
#         if prime:
#             print(i)

'''Print the alternate numbers pattern using a while loop
1  
2 3  
4 5 6  
7 8 9 10  
11 12 13 14 15
'''

rows = 5

number = 1

row = 1

while row <=rows:
    col = 1
    while col<row:
        print(number, end=' ')
        number +=1
        col +=1
    print()
    row+=1
    

'''Upwards pryramid'''

n = 10

for i in range(1,n+1):
    print(' '*(n-i), end=' ')
    for j in range(1,i+1):
        print(j, end=" ")
    print()
        
        
# for i in range(1,n+1):
#     space = ' '*(2*n - i)
#     starts = '*'*(2*i-1)
    
#     print(space+starts)

for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

Abz = 'ABCDEF'
letter = 'G'
if 'A'<=letter<='F':
    print(letter)