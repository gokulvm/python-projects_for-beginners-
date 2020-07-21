#!/usr/bin/env python
# coding: utf-8

# # Calculator by python

# ## First create the function for the all maths calculation

# In[1]:


def add(num):  #Addition
    result = 0   #result will be contain the total
    for i in num:
        result= result+i #add the every values one by one
    return result

def sub(num): #Subtraction 
    result = 0
    for i in num:
        result= i-result
    return result

def mul(num):   #Multiplication
    result = 1   #The initialize value should be 1
    for i in num:
        result= result*i
    return result

def div(num):  #Division
    final = True      #in the division denominator value should not be zero,so we need to check that 
    result = num[0]    
    check = num[1:]
    for j in check: 
        if j != 0:  #if denominator value not equal to zero if statement will be true
            for g in check: 
                result = result/g

            return result

        else:   #if the value is zero its return below statement
            return "0 cant be act divisible number"


# ### Now get the input from the user  And Call the function to perform the math

# In[ ]:


print("WELCOME TO THE CALCULATOR BY PYTHON")
print("you need to enter how many numbers did you want to calculate")

sentance  = '''hello user enter,what type of method calculation 
do you want to perform...!!!
    addition        : 1 
    subraction      : 2
    multiplication  : 3 
    division        : 4'''

print(sentance)

cal = int(input("Enter your calculation method : "))

values = int(input("enter how many numbers did you want to calculate : ")) #this will take the length of your total number

numbers = [int(input("enter the numbers you need to calculate : ")) for i in range(values)] #lsit of your numbers to perform

print(numbers)

if cal <= 4:
    if cal==1:
        print(f"your addition answer is : {add(numbers)}")

    elif cal==2:
        print(f"your subraction answer is : {sub(numbers)}")

    elif cal==3:
        print(f"your multiplication answer is : {mul(numbers)}")

    elif cal == 4:
        print(f"your division answer is : {div(numbers)}")

else:
    print("Enter number between 1 to 4")

