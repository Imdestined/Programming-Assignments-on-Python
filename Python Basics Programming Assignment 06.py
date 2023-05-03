#!/usr/bin/env python
# coding: utf-8

# # Assignment 6 Solutions

# #### 1. Write a Python Program to Display Fibonacci Sequence using Recursion ?

# In[52]:


def genFibonacci(n,a,b):
    if n == 0:
        return 1
    else:
        result = a+b
        print(result, end=', ')
        genFibonacci(n-1,b,result)
in_num = int(input('Enter the length of Series: '))
print('0, 1',end=', ')
genFibonacci(in_num,1,2)


# #### 2. Write a Python Program to Find Factorial of a Number using Recursion ?

# In[37]:


def factorial(num):
    if (num < 1):
        return 1
    else:
        return num*factorial(num-1)
num = int(input('Enter a number: '))
value = factorial(num)
print(f'The Factorial of {num} is {value}')


# #### 3. Write a Python Program to Calculate your Body Mass Index ?

# In[36]:


def calculateBMI():
    in_weight = eval(input('Enter your Weight(kgs): '))
    in_height = eval(input('Enter your Height(mts): '))
    calc_bmi = in_weight/pow(in_height,2)
    if (calc_bmi < 18.5):
        status = 'Underweight'
    elif (calc_bmi >= 18.5 and calc_bmi < 24.9):
        status = 'Healthy'
    elif (calc_bmi >= 24.9 and calc_bmi < 30):
        status = 'Overweight'
    elif (calc_bmi >=30):
        status = 'Suffering from Obesity'
    print(f'Your\'re BMI is {calc_bmi} and status is {status} ')
calculateBMI()


# #### 4. Write a Python Program to Calculate the Natural Logarithm of any Number ?

# In[22]:


import math
def genNatLog():
    in_num = eval(input("Enter a Number:"))
    print(math.log(in_num))

genNatLog()


# #### 5. Write a Python Program for Cube sum of first n Natural Numbers ?

# In[28]:


def cubeOfNaturalNumbers():
    in_num = int(input("Enter the no of Natural Numbers: "))
    result = pow(((in_num * (in_num +1))/2),2)
    print(f'The Cube Sum of First {in_num} Natural Numbers is {result}')

cubeOfNaturalNumbers()

