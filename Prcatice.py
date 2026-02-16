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


'''Fibonacci sequence for the nth term'''

# def fib(n):
    
#     a,b = 0,1
    
#     for i in range(n+1):
        
#         a,b = b, a+b
#     print(b)    
# fib(5) 

'''Fibonacci number for the nth term'''

# def fib(n):
#     if n ==0:
#         return n
#     elif n == 1:
#         return n
#     else:
#         return fib(n-1)+fib(n-2)
# print(fib(8))
# for i in range(10):
#     print(fib(i), end=' ')

'''


     *
    ***
   *****
    ***
     *
'''

# n = 5
# for i in range(1,n+1):
#     for j in range(1):
#         if i %2:
#             print(' '*n, "*"*i)
#             n -=1
# n=5
# for i in range(n+1,0,-1):
#     for j in range(1):
#         if i %2:
#             if i == 5:
#                 continue
#             else:
#                 n-= 1
#                 print(' '*(n), "*"*i)
#                 n+=2   


 
# n = 5
# for i in range(1, n + 1, 2):
#     stars = "*" * i
#     space = " " * n
#     n-=1
#     total = space + stars
#     print(total)
    
#     if total == n:
'''Find all prime numbers between 1 and 50 using nested loop'''

# for i in range(1,50):
    
#     if i > 1:
#         prime = True
#     for j in range(2,i):
#         if i % j == 0:
#             prime = False
#             break
#         print(i,end='')
    
        
 
    

           