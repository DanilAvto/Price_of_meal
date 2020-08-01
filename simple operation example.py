#!/usr/bin/env python
# coding: utf-8

# In[2]:


even = [0,2,4,6,8,10,12,14,16,18,20]
for i in even:
    print(i, end = ' ')
    


# In[3]:


prices = { 
    "spaghetti": 4,
    "lasagna" : 5,
    "hamburger": 2
}
quantity = {
    "spaghetti": 5,
    "lasagna" : 10,
    "hamburger": 0
}

money_spent = 0

for i in prices:
    money_spent = money_spent + (prices[i]* quantity[i])
    
    
print(money_spent)


# In[ ]:




