#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Q1 Write a python program to scrape data for “Data Analyst” Job position in “Bangalore” location. You
#have to scrape the job-title, job-location, company_name, experience_required. You have to scrape first 10
#jobs data.

# let's first install the selenium library
get_ipython().system(' pip install selenium')
# Let's now import all the required libraries.
import selenium
import pandas as pd
from selenium import webdriver
# let's first connect to the web driver
driver = webdriver.Chrome(r"C:\Users\Anchal\Downloads\chromedriver_win32\chromedriver.exe")
url = "https://www.shine.com/"
driver.get(url)
# finding element for job search bar
search_job = driver.find_element_by_xpath("//input[@class='iconH-zoom-white']")
search_job

# write on search bar
search_job.send_keys('Data Scientist')

# finding element for job location bar
search_loc=driver.find_element_by_id('form-control')
search_loc.send_keys("Bangalore")

search_btn= driver .find_element_by_xpath("//button[@class='btn']")
search_btn

# clicking  using xpath function
search_btn=driver.find_element_by_class_name('btn')
search_btn.click()

#so let's extract all the tags having the job titles
title_tag=driver.find_elements_by_xpath("//a[@class='title fw500 ellipsis']")
title_tag

# extract the text of the job title  from the tags
job1_titles=[]
for i in title_tag:
    if i.text is None:
        job1_titles.append('Not')
    else:
        job1_titles.append(i.text)
job1_titles[:10]   


# lets extract all the tags having company names
company_tag=driver.find_elements_by_xpath("//a[@class='subTitle ellipsis fleft']")
company_tag


# Now we will extract the text from the tags by looping over these tags
companies1_names=[]

for i in company_tag:
    companies1_names.append(i.text)
companies1_names[:10]  


# lets extract all the tags having locations
locations_tag=driver.find_elements_by_xpath("//li[@class='fleft grey-text br2 placeHolderLi location']/span")
locations_tag


locations1_list=[]
for i in locations_tag:
    locations1_list.append(i.text)
locations1_list[:10]  


job1=pd.DataFrame({})
job1['title']=job1_titles[:10]
job1['company_name']=companies1_names[:10]
job1['location']=locations1_list[:10]




# In[3]:


#Q2:Write a python program to scrape data for “Data Scientist” Job position in“Bangalore” location. You
#have to scrape the job-title, job-location, company_name. You have to scrape first 10 jobs data.
#This task will be done in following steps:



import selenium
import pandas as pd
from selenium import webdriver
# let's first connect to the web driver
driver = webdriver.Chrome(r"C:\Users\Anchal\Downloads\chromedriver_win32\chromedriver.exe")
url = "https://www.shine.com/"
driver.get(url)
# finding element for job search bar
search_job = driver.find_element_by_xpath("//input[@class='placeholder']")
search_job
# write on search bar
search_job.send_keys('Data Scientist')
# findin
jobs=pd.DataFrame({})
jobs['title']=job_titles[:10]
jobs['company']=companies_names[:10]
jobs['experience_required']=experience_list[:10]
jobs['location']=locations_list[:10]g element for job location bar
search_loc=driver.find_element_by_id('qsb-location-sugg')
search_loc.send_keys("Bangalore")
search_b
# Now we will extract the text from the tags by looping over these tags
companies_names=[]

for i in company_tags:
    companies_names.append(i.text)
companies_names[:10]  
jobs=pd.DataFrame({})
jobs['title']=job_titles[:10]
jobs['company']=companies_names[:10]
jobs['location']=locations_list[:10]tn= driver .find_element_by_xpath("//button[@class='btn']")
search_btn
# clicking  using xpath function
search_btn=driver.find_element_by_xpath("//button[@class='btn']")
search_btn.click()
#so let's extract all the tags having the job titles
title_tags=driver.find_elements_by_xpath("//a[@class='title fw500 ellipsis']")
title_tags
# extract the text of the job title  from the tags
job_titles=[]
for i in title_tags:
    if i.text is None:
        job_titles.append('Not')
    else:
        job_titles.append(i.text)
job_titles[:10]  
# lets extract all the tags having company names
company_tags=driver.find_elements_by_xpath("//a[@class='subTitle ellipsis fleft']")
company_tags
# Now we will extract the text from the tags by looping over these tags
companies_names=[]

for i in company_tags:
    companies_names.append(i.text)
companies_names[:10]  
jobs=pd.DataFrame({})
jobs['title']=job_titles[:10]
jobs['company']=companies_names[:10]
jobs['location']=locations_list[:10]


# In[1]:


#Q3 Q3: In this question you have to scrape data using the filters available on the webpage
#You have to use the location and salary filter.
#You have to scrape data for “Data Scientist” designation for first 10 job results.
#You have to scrape the job-title, job-location, company name, experience required.
#The location filter to be used is “Delhi/NCR”. The salary filter to be used is “3-6” lakhs



import selenium
import pandas as pd
from selenium import webdriver


# let's first connect to the web driver
driver = webdriver.Chrome(r"C:\Users\Anchal\Downloads\chromedriver_win32\chromedriver.exe")

url = "https://www.shine.com/"
driver.get(url)

# finding element for job search bar
search_job = driver.find_element_by_xpath("//input[@class='sugInp']")
search_job

# write on search bar
search_job.send_keys('Data Scientist')

search_btn= driver .find_element_by_xpath("//button[@class='btn']")
search_btn

# clicking  using xpath function
search_btn=driver.find_element_by_class_name('btn')
search_btn.click()

#so let's extract all the tags having the job titles
title_t1=driver.find_elements_by_xpath("//a[@class='title fw500 ellipsis']")
title_t1

# extract the text of the job title  from the tags
job_titles=[]
for i in title_t1:
    if i.text is None:
        job_titles.append('Not')
    else:
        job_titles.append(i.text)
job_titles[:10]  

# lets extract all the tags having company names
company_t1=driver.find_elements_by_xpath("//a[@class='subTitle ellipsis fleft']")
company_t1


# Now we will extract the text from the tags by looping over these tags
companies_names=[]

for i in company_t1:
    companies_names.append(i.text)
companies_names[:10]  

# so lets extract  all the tags having the experience required data
experience_t1=driver.find_elements_by_xpath("//li[@class='fleft grey-text br2 placeHolderLi experience'] //span")
experience_t1


# no we will extract the text  from these tags only by one by looping over these tags
experience_list=[]
for i in experience_t1:
    experience_list.append(i.text)
experience_list[:10]  


# So lets extract all the tags having locations
locations_t1=driver.find_elements_by_xpath("//li[@class='fleft grey-text br2 placeHolderLi location']/span")
locations_t1


#Now we wil extract the text from these tags only by one by looping over these tags
locations_list=[]
for i in locations_t1:
    locations_list.append(i.text)
locations_list[:10]   

jobs2=pd.DataFrame({})
jobs2['title']=job_titles[:10]
jobs2['company']=companies_names[:10]
jobs2['experience_required']=experience_list[:10]
jobs2['location']=locations_list[:10]









# In[2]:


#Q4Scrape data of first 100 sunglasses listings on flipkart.com. You have to scrape four attributes:
# Brand
# ProductDescription
# Price
# The attributes which you have to scrape is ticked marked in the below image.

# let's first connect to the web driver
driver = webdriver.Chrome(r"C:\Users\Anchal\Downloads\chromedriver_win32\chromedriver.exe")


url="https://www.flipkart.com/"
driver.get(url)

# finding element for job search bar
search_g= driver.find_element_by_xpath("//input[@type='text']")
search_g


# write on search bar
search_g.send_keys('sunglasses')

search_btn=driver.find_element_by_xpath("//button[@class='L0Z3Pu']")
search_btn

search_btn=driver.find_element_by_class_name('L0Z3Pu')
search_btn.click()

B_name=[]
Price=[]
P_desc=[]
Discount=[]

for i in range(3):
    b_name=driver.find_elements_by_xpath("//div[@class='_2WkVRV']")
    p_desc=driver.find_elements_by_xpath("//a[@class='IRpwTa']")
    price =driver.find_elements_by_xpath("//div[@class='_25b18c']")
    discount=driver.find_elements_by_xpath("//div[@class='_3Ay6Sb']")
    
    for j  in b_name:
        B_name.append(j.text)
    B_name[:100]    
    
    
    
    for k in p_desc:
        P_desc.append(k.text)
    P_desc[:100] 
    
    
    for l in price:
        Price.append(l.text)
    Price[:100] 
    
    3
    for t in discount:
        Discount.append(t.text)
    Discount[:100]
    
    B_name[:100]
    
    sun_gl=pd.DataFrame({})
sun_gl['Brand_name']=B_name[:100]
sun_gl['P_price']=Price[:100]
sun_gl['Pr_desc']=P_desc[:100]
sun_gl['P_discount']=Discount[:100]

sun_gl


# In[4]:


#Q6  Scrape data forfirst 100 sneakers you find whenyou visit flipkart.com and search for “sneakers” inthe search field.
# You have to scrape 3 attributes of each sneaker:
# Brand
# ProductDescription
# Price
# As shown in the below image, you have to scrape the above attributes.

# let's first connect to the web driver
driver = webdriver.Chrome(r"C:\Users\Anchal\Downloads\chromedriver_win32\chromedriver.exe")

url="https://www.flipkart.com/"
driver.get(url)

# finding element for job search bar
search_g= driver.find_element_by_xpath("//input[@type='text']")
search_g

# write on search bar
search_g.send_keys('sunglasses')

search_btn=driver.find_element_by_xpath("//button[@class='L0Z3Pu']")
search_btn

search_btn=driver.find_element_by_class_name('L0Z3Pu')
search_btn.click()

B_name=[]
Price=[]
P_desc=[]
Discount=[]

for i in range(3):
    b_name=driver.find_elements_by_xpath("//div[@class='_2WkVRV']")
    p_desc=driver.find_elements_by_xpath("//a[@class='IRpwTa']")
    price =driver.find_elements_by_xpath("//div[@class='_25b18c']")
    discount=driver.find_elements_by_xpath("//div[@class='_3Ay6Sb']")
    
    for j  in b_name:
        B_name.append(j.text)
    B_name[:100]    
    
    
    
    for k in p_desc:
        P_desc.append(k.text)
    P_desc[:100] 
    
    
    for l in price:
        Price.append(l.text)
    Price[:100] 
    
    
    for t in discount:
        Discount.append(t.text)
    Discount[:100]
    
    B_name[:100]
    
    sun_gl=pd.DataFrame({})
sun_gl['Brand_name']=B_name[:100]
sun_gl['P_price']=Price[:100]
sun_gl['Pr_desc']=P_desc[:100]
sun_gl['P_discount']=Discount[:100]

sun_gl


# In[ ]:




