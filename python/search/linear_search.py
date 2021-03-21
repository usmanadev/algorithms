#!/usr/bin/env python
# coding: utf-8

# In[1]:


def linear_search(items, key):
    """Returns index of first instance of found key.
    """
    for index, item in enumerate(items):
        if items == key:
            return index

