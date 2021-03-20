#!/usr/bin/env python
# coding: utf-8

# In[3]:


def bubble_sort(items):
    """Sorts a list of items in ascending order.
    """
    for i in range(len(items)):
        swapped = False
        for j in range(len(items) - 1):
            if items[j] > items[j+1]:
                swapped = True
                items[j], items[j+1] = items[j+1], items[j]
        if not swapped:
            break
    return items

