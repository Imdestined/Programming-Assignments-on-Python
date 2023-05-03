#!/usr/bin/env python
# coding: utf-8

# ## Question 1: Please write a program using generator to print the numbers which can be divisible by 5 and 7 between 0 and n in comma separated form while n is input by console. Example: If the following n is given as input to the program: 100 Then, the output of the program should be:0,35,70

# In[1]:


def divisible_by_5_and_7(n):
    """
    A generator function that yields numbers between 0 and n that are divisible by both 5 and 7.
    """
    for i in range(n+1):
        if i % 5 == 0 and i % 7 == 0:
            yield i

# Get the value of n from the user
n = int(input("Enter a value for n: "))

# Use the generator to generate the comma-separated list of numbers
result = ",".join(str(i) for i in divisible_by_5_and_7(n))

# Print the result
print(result)


# ## Question 2: Please write a program using generator to print the even numbers between 0 and n in comma separated form while n is input by console. Example: If the following n is given as input to the program:10 Then, the output of the program should be: 0,2,4,6,8,10

# In[3]:


def even_numbers(n):
    """
    A generator function that yields even numbers between 0 and n.
    """
    for i in range(n+1):
        if i % 2 == 0:
            yield i

# Get the value of n from the user
n = int(input("Enter a value for n: "))

# Use the generator to generate the comma-separated list of even numbers
result = ",".join(str(i) for i in even_numbers(n))

# Print the result
print(result)


# ## Question 3: The Fibonacci Sequence is computed based on the following formula:
# f(n)=0 if n=0
# f(n)=1 if n=1
# f(n)=f(n-1)+f(n-2) if n&gt;1
# Please write a program using list comprehension to print the Fibonacci Sequence in comma
# separated form with a given n input by console.
# Example:
# If the following n is given as input to the program:
# 7
# 
# Then, the output of the program should be:
# 0,1,1,2,3,5,8,13

# In[4]:


# Get the value of n from the user
n = int(input("Enter a value for n: "))

# Initialize the Fibonacci sequence
fibonacci = [0, 1]

# Use list comprehension to generate the Fibonacci sequence
[fibonacci.append(fibonacci[i-1] + fibonacci[i-2]) for i in range(2, n+1)]

# Convert the sequence to a comma-separated string and print it
result = ",".join(str(i) for i in fibonacci)
print(result)


# ## Question 4: Assuming that we have some email addresses in the "username@companyname.com"; format,
# please write program to print the user name of a given email address. Both user names and
# company names are composed of letters only.
# Example:
# If the following email address is given as input to the program:
# john@google.com
# Then, the output of the program should be:
# john

# In[5]:


# Get the email address from the user
email = input("Enter an email address: ")

# Split the email address at the "@" symbol and take the first part as the username
username = email.split("@")[0]

# Print the username
print(username)


# ## Question 5: Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have a area function which can print the area of the shape where Shape&#39;s area is 0 by default.

# In[6]:


class Shape:
    def area(self):
        return 0


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2

