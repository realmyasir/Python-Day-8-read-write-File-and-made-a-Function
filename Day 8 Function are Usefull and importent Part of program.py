# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 10:38:38 2023

@author: Web 123
"""

# f=open('yasir.txt','w')
# print(type(f))

# f.write('My name is Yasir abbas\n')
# f.write('My best Friend Name is Aon Muhammad \n')
# f.write('He is lundy baz\n')
# f.close()

# f=open('yasir.txt','r')
# print(type(f))
# print(f.read())
# f.close()


# f=open('yasir.txt','r')

# print(f.readline())
# f.close()

# f=open('yasir.txt','r')
# print(type(f))
# # print(f.readlines())
# content=f.readlines()
# print(content)
# f.close()


# try:
#     with open('yasir.txt', 'r') as f:
#         content = f.readline()
#         if content:
#             print(content)
#             print(type(content))
#         else:
#             print("File is empty.")
# except FileNotFoundError:
#     print("File not found.")
# except Exception as e:
#     print(f"An error occurred: {e}")


# f=open('yasir.txt','a')
# f.write('He is a best friend for girls mind\nHe is black and white man\n')
# f.close()
# f=open('yasir.txt','r')
# print(type(f))
# print(f.read())
# f.close()
# print()

# with open('yasir.txt','r') as f:
#     for line in f.readlines():
#         print(line)
# print()


# Function Start

# print("Hello World!")

# def hello():
#     print('Hello World !')
# hello()

# for i in range(10):
#     hello()
 # passing vaiabls
 
 
 
# def hi(name):
#     for i in range(5):
#         print(f'Hello {name}')
    
# hi('Yasir')

 # fabnocci Series in python!  

# def feb(n):
#     a = 0
#     b = 1
#     for i in range(n):
#         a, b= b, a + b
#     return b
# feb_num=feb(20)
# print(feb_num)

# def feb(n):
#     a = 0
#     b = 1
#     for i in range(n):
#         a, b = b, a + b
#     return a

# fib = feb(20)
# print(fib)


# n=int(input('Enter febnocii Series Limit'))
# n=20
# a,b=0,1
# fib=[]
# for i in range(n):
#     fib.append(a)
#     a,b=b,a+b
#     print(f'Your Enter The Limit {n} Fibonacci Number Are , {fib}')

