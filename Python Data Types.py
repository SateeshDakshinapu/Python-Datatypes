#!/usr/bin/env python
# coding: utf-8

# # list

# In[32]:


# Creating a list
my_list = [1, 2, 3, 4, 5]
print(f"Initial list:{my_list}")


# In[33]:


# Adding an element to the list
my_list.append(6)
print(f"List after adding an element:{my_list}")


# In[34]:


# Removing an element from the list
my_list.remove(3)
print(f"List after removing an element:{my_list}")


# In[35]:


# Modifying an element in the list
my_list[2] = 10
print(f"List after modifying an element{my_list}")


# # Dictionary

# In[36]:


# Creating a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}
print(f"Initial dictionary:{my_dict}")


# In[37]:


# Adding an element to the dictionary
my_dict['d'] = 4
print(f"Dictionary after adding an element:{my_dict}")


# In[38]:


# Removing an element from the dictionary
del my_dict['b']
print(f"Dictionary after removing an element:{my_dict}")


# In[44]:


# Modifying an element in the dictionary
my_dict['a'] = 10
print(f"Dictionary after modifying an element:{my_dict}")


# # set

# In[67]:


my_set = {1, 2, 3, 4, 5}
print("Initial set:", my_set)


# In[68]:


# Adding an element to the set
my_set.add(6)
print("Set after adding an element:", my_set)


# In[69]:


# Removing an element from the set
my_set.discard(3)
print(f"Set after removing an element:{my_set}")


# In[70]:


# Sets do not have an index, so modifying specific elements isn't straightforward
# We can remove an element and add a new one to simulate a modification
my_set.discard(4)
my_set.add(10)
print(f"Set after modifying an element:{my_set}")






