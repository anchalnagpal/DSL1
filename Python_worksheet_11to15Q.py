#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#write a python program to find the factorial of a number.

num = int(input("Enter a number: "))    
fact = 1    
if num < 0:    
   print(" Factorial does not exist for negative numbers")    
elif num == 0:    
   print("The factorial of 0 is 1")    
else:    
   for i in range(1,num + 1):    
       fact = fact*i    
   print("The factorial of",num,"is",factorial)    


# In[ ]:


#12. Write a python program to find whether a number is prime or compositenum = int(input("Enter any number : "))

if num > 1:
   for i in range(2, num):
      if (num % i) == 0:
           print(num, "is NOT a prime number")
           break
  else:
       print(num, "is a PRIME number")
elif num == 0 or 1:
  print(num, "is a neither prime NOR composite number")
else:
   print(num, "is NOT a prime number it is a COMPOSITE number")


# In[ ]:


#Write a python program to check whether a given string is palindrome or not

x = "malayalam"
 w = ""
for i in x:
    w = i + w
 if (x == w):
    print("Yes")
else:
    print("No")


# In[ ]:


#14. Write a Python program to get the third side of right-angled triangle from two given sides

def pythagoras(opposite_side,adjacent_side,hypotenuse):
        if opposite_side == str("x"):
            return ("Opposite = " + str(((hypotenuse**2) - (adjacent_side**2))**0.5))
        elif adjacent_side == str("x"):
            return ("Adjacent = " + str(((hypotenuse**2) - (opposite_side**2))**0.5))
        elif hypotenuse == str("x"):
            return ("Hypotenuse = " + str(((opposite_side**2) + (adjacent_side**2))**0.5))
        else:
            return "You know the answer!"
    
print(pythagoras(3,4,'x'))
print(pythagoras(3,'x',5))
print(pythagoras('x',4,5))
print(pythagoras(3,4,5))


# In[ ]:


#15. Write a python program to print the frequency of each of the characters present in a given string
test_str = "GeeksforGeeks"
 
for i in test_str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
print("Count of all characters in GeeksforGeeks is :\n "
      + str(all_freq))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




