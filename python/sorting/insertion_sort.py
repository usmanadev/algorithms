#!/usr/bin/env python
# coding: utf-8

# In[2]:


def insertion_sort(items):
    """Sorts a list of items in ascending order.
    """
    for i, val in enumerate(items[1:]):
        temp = i
        while i >= 0 and val < items[i]:
            items[i + 1] = items[i]
            i -= 1
        items[i + 1] = val
    return items

