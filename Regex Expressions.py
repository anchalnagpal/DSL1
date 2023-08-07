#!/usr/bin/env python
# coding: utf-8

# In[26]:


#Question 1- Write a Python program to replace all occurrences of a space, comma, or dot with a colon.

import re
str = 'Python Exercises, PHP exercises.'
reg=(re.sub("[ ,.]", ":", str))
print(reg)


# In[27]:


# Question 2-  Write a Python program to find all words starting with 'a' or 'e' in a given string.

import re
str = 'Python is not a case sensitive language. It supports ArrayList concepts and have good regex expressions concept.'
list = re.findall("[ae]\w+", str)
print(list)


# In[28]:


#Question 3- Create a function in python to find all words that are at least 4 characters long in a string. The use of the re.compile() method is mandatory.

import re
str="ganu and kaavu both are brothers"
String_pattern=(r"\b\w{4}\b")
regex_pattern=re.compile(String_pattern)
result=regex_pattern.findall(str)
print(result)


# In[29]:


#Question 4- Create a function in python to find all three, four, and five character words in a string. The use of the re.compile() method is mandatory.

import re
str="ganu and kaavu both are brothers"
String_pattern=(r"\b\w{3,5}\b")
regex_pattern=re.compile(String_pattern)
result=regex_pattern.findall(str)
print(result)


# In[56]:


#Question 5- Create a function in Python to remove the parenthesis in a list of strings. The use of the re.compile() method is mandatory.

import re
items = ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]
for item in items:
    print(re.sub(r"\((.*?)\)", r"\1", item))
   


# In[54]:


#Question 6- Write a python program to remove the parenthesis area from the text stored in the text file using Regular Expression

import re
items = ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]
for item in items:
    print(re.sub (r" ?\([^)]+\)", "", item))


# In[32]:


#Question 7- Write a regular expression in Python to split a string into uppercase letters.

import re
text = "ImportanceOfRegularExpressionsInPython"
print(re.findall('[A-Z][^A-Z]*', text))


# In[59]:


#Question 9- Create a function in python to insert spaces between words starting with capital letters or with numbers.

import re
string="RegularExpression1IsAn2ImportantTopic3InPython"
words = re.sub('(\d+(\.\d+)?)', r' \1 ', string).strip()
print(words)


# In[33]:


#Question 11- Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores.

import re
def text_match(text):
        patterns = '^[a-zA-Z0-9_]*$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("The quick brown fox jumps over the lazy dog."))
print(text_match("Python_Exercises_1"))


# In[60]:


#Question 12- Write a Python program where a string will start with a specific number. 

import re
def match_number(string):
    text = re.compile(r"^6")
    if text.match(string):
        return True
    else:
        return False
print(match_number('5-2369342'))
print(match_number('6-2385467'))


# In[36]:


#Question 13- Write a Python program to remove leading zeros from an IP address

import re
ip = "214.04.063.137"
string = re.sub('\.[0]*', '.', ip)
print(string)


# In[37]:


#Question 10- Write a python program to extract email address from the text stored in the text file using Regular Expression.

import re 

string = "Hello my name is Data Science and my email address is xyz@domain.com and alternate email address is xyz.abc@sdomain.domain.com." 
lst = re.findall('\S+@\S+', string)     
print(lst) 


# In[38]:


#Question 8- Create a function in python to insert spaces between words starting with numbers.

import re
string="RegularExpression1IsAn2ImportantTopic3InPython"
words = re.sub('(\d+(\.\d+)?)', r' \1', string).strip()
print(words)


# In[3]:


#Question 15-Write a Python program to search some literals strings in a string

import re
patterns = [ 'fox', 'dog', 'horse' ]
text = 'The quick brown fox jumps over the lazy dog.'
for pattern in patterns:
    print('Searching for "%s" in "%s" ->' % (pattern, text),)
    if re.search(pattern,  text):
        print('Matched!')
    else:
        print('Not Matched!')


# In[4]:


#Question 16-Write a Python program to search a literals string in a string and also find the location within the original string where the pattern occurs

import re
pattern = 'fox'
text = 'The quick brown fox jumps over the lazy dog.'
match = re.search(pattern, text)
s = match.start()
e = match.end()
print('Found "%s" in "%s" from %d to %d ' %     (match.re.pattern, match.string, s, e))


# In[5]:


#Question 17- Write a Python program to find the substrings within a string.

import re
text = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'
for match in re.findall(pattern, text):
    print('Found "%s"' % match)


# In[6]:


#Question 18- Write a Python program to find the occurrence and position of the substrings within a string.

import re
text = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'
for match in re.finditer(pattern, text):
    s = match.start()
    e = match.end()
    print('Found "%s" at %d:%d' % (text[s:e], s, e))


# In[7]:


# Question 19- Write a Python program to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.

import re
def change_date_format(dt):
        return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', dt)
dt1 = "2026-01-02"
print("Original date in YYY-MM-DD Format: ",dt1)
print("New date in DD-MM-YYYY Format: ",change_date_format(dt1))


# In[8]:


#Question 20- Create a function in python to find all decimal numbers with a precision of 1 or 2 in a string. The use of the re.compile() method is mandatory.


# In[9]:


#Question 21- Write a Python program to separate and print the numbers and their position of a given string.

import re
# Input.
text = "The following example creates an ArrayList with a capacity of 50 elements. Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly."

for m in re.finditer("\d+", text):
    print(m.group(0))
    print("Index position:", m.start())


# In[10]:


#Question 22- Write a regular expression in python program to extract maximum/largest numeric value from a string.

import re
#input
string='ab12cd123ef23'
#seperate number from string
number = re.findall('\d+', string)
#convert it into integer
number = map(int, number)
print("Max_value:",max(number))


# In[11]:


#Question 23- Create a function in python to insert spaces between words starting with capital letters.

import re
def capital_words_spaces(str1):
  return re.sub(r"(\w)([A-Z])", r"\1 \2", str1)

print(capital_words_spaces("RegularExpressionIsAnImportantTopicInPython"))


# In[12]:


# Question 24- Python regex to find sequences of one upper case letter followed by lower case letters

import re
def text_match(text):
        patterns = '[A-Z]+[a-z]+$'
        if re.search(patterns, text):
                return 'Found a match!'
        else:
                return('Not matched!')
print(text_match("AaBbGg"))
print(text_match("Python"))
print(text_match("python"))
print(text_match("PYTHON"))
print(text_match("aA"))
print(text_match("Aa"))


# In[16]:


#Question 25-Write a Python program to remove continuous duplicate words from Sentence using Regular Expression.

import re

def removeDuplicatesFromText(text):
    regex = r'\b(\w+)(?:\W+\1\b)+' 
    return re.sub(regex, r'\1', text, flags=re.IGNORECASE)

str1 =  "Hello hello world world"
print(removeDuplicatesFromText(str1))


# In[17]:


#Question 26-  - Write a python program using RegEx to accept string ending with alphanumeric character.

import re
 
# Make a regular expression to accept string
# ending with alphanumeric character
regex = '[a-zA-z0-9]$'
     
# Define a function for accepting string
# ending with alphanumeric character
def check(string):
 
     # pass the regular expression
     # and the string in search() method
    if(re.search(regex, string)):
        print("Accept")
         
    else:
        print("Discard")
     
 
# Driver Code
if __name__ == '__main__' :
     
    # Enter the string
    string = "ankirai@"
     
    # calling run function
    check(string)
 
    string = "ankitrai326"
    check(string)
 
    string = "ankit."
    check(string)
 
    string = "geeksforgeeks"
    check(string)


# In[71]:


#Question 27-Write a python program using RegEx to extract the hashtags.
import re
text1="""RT @kapil_kausik: #Doltiwal I mean #xyzabc is "hurt" by #Demonetization as the same has rendered USELESS <ed><U+00A0><U+00BD><ed><U+00B1><U+0089> "acquired funds" No wo"""

textList = text1.split()
for i in textList:
    if(i[0] == "#"):
        x = i.replace("#", '')
        print(x)
  


# In[9]:


#Question 28-Write a python program using RegEx to remove <U+..> like symbols

import re

str="@Jags123456 Bharat band on 28??<ed><U+00A0><U+00BD><ed><U+00B8><U+0082>Those who  are protesting #demonetization  are all different party leaders"

result=re.sub(r'[^a-zA-Z0-9 ,*\U+00*\]', '', str)


print(result)





# In[24]:


#Question 29-Write a python program to extract dates from the text stored in the text file.

import re
str = "Ron was born on 12-09-1992 and he was admitted to school 15-12-1999"

pattern = "\d{2}[/-]\d{2}[/-]\d{4}"
dates = re.findall(pattern,str)
 
print("Extract date:", dates)


# In[25]:


#Question 30-Create a function in python to remove all words from a string of length between 2 and 4..
#The use of the re.compile() method is mandatory.

import re
text = "The following example creates an ArrayList with a capacity of 50 elements. 4 elements are then added to the ArrayList and the ArrayList is trimmed accordingly."

word = re.compile(r'\W*\b\w{2,4}\b')
print(word.sub('', text))


# In[76]:


#Question 14- Write a regular expression in python to match a date string in the form of Month name followed by day number and year stored in a text file.
#Sample text :  ' On August 15th 1947 that India was declared independent from British colonialism, and the reins of control were handed over to the leaders of the Country’.
#Expected Output- August 15th 1947


import re
str = " On August 15th 1947 that India was declared independent from British colonialism, and the reins of control were handed over to the leaders of the Country’"

pattern = "\m{August}[ ]\d{th}[/-]\Y{4}"
dates = re.findall(pattern,str)
 
print("Extract date:", dates)



# In[ ]:





# In[ ]:





# In[ ]:




