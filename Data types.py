#!/usr/bin/env python
# coding: utf-8

# # list

# In[4]:


# Creating a list
my_list = [1, 2, 3, 4, 5]
print(f"Initial list:{my_list}")
# Adding an element to the list
my_list.append(6)
print(f"List after adding an element:{my_list}")
# Removing an element from the list
my_list.remove(3)
print(f"List after removing an element:{my_list}")
# Modifying an element in the list
my_list[2] = 10
print(f"List after modifying an element{my_list}")


# # Dictionary

# In[10]:


# Creating a dictionary
my_dict = {'sateesh':201, 'sudheer': 202, 'mohan': 203}
print(f"Initial dictionary:{my_dict}")
# Adding an element to the dictionary
my_dict['basha'] = 204
print(f"Dictionary after adding an element:{my_dict}")
# Removing an element from the dictionary
del my_dict['sudheer']
print(f"Dictionary after removing an element:{my_dict}")
# Modifying an element in the dictionary
my_dict['sateesh'] = 205
print(f"Dictionary after modifying an element:{my_dict}")


# # set

# In[5]:


# Creating a set
my_set = {1, 2, 3, 4, 5}
print(f"Initial set:{my_set}")
# Adding an element to the set
my_set.add(6)
print(f"Set after adding an element:{my_set}")
# Removing an element from the set
my_set.discard(3)
print(f"Set after removing an element:{my_set}")
# Sets do not have an index, so modifying specific elements isn't straightforward
# We can remove an element and add a new one to simulate a modification
my_set.discard(4)
my_set.add(10)
print(f"Set after modifying an element:{my_set}")





