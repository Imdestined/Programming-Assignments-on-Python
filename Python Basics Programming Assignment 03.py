#!/usr/bin/env python
# coding: utf-8

# # Assignment 3 Solutions

# #### 1.Write a Python program to check if a Number is Positive, Negative or Zero ?

# In[1]:


def checkNumber(num):
    if num > 0:
        print('{} is a Postive number'.format(num))
    elif num < 0:
        print('{} is a Negative number'.format(num))
    else:
        print("Number is Zero")
        
num = int(input("Enter a number: "))
checkNumber(num)


# #### 2.Write a Python program to check if a Number is Odd or Even ?

# In[2]:


def checkNumber(num):
    if num%2 == 0:
        print('{} is a Even number'.format(num))
    else:
        print('{} is a Odd number'.format(num))
        
num = int(input("Enter a number: "))
checkNumber(num)


# #### 3.Write a Python program to check  Leap Year ?

# In[3]:


def checkYear(year):
    if (year%4 == 0 and year%100 != 0 or year%400 == 0):
        print(f'{year} is a Leap year')
    else:
        print(f'{year} is not a Leap year')

year = int(input("Enter year: "))
checkYear(year)


# #### 4.Write a Python program to check Prime Number ?

# In[4]:


def isPrime(num):
    flag = False
    for i in range(2,num):
        if num%i ==0:
            flag= True
            break
    if(not flag):
        print(f'{num} is a prime number')
    else:
        print(f'{num} is not a prime number')
        
number = int(input("Enter a number: "))
isPrime(number)


# #### 5.Write a Python program to print all Prime Numbers in an interval of 1-10000 ?

# In[7]:


primeNumbersList = []

def generatePrimeNumbers():
    for x in range(1,10000):
        flag=False
        for y in range(2,x):
            if (x%y ==0):
                flag = True
                break
        if (not flag):
            primeNumbersList.append(x)
        
generatePrimeNumbers()
print(primeNumbersList)

