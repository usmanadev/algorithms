#!/usr/bin/env python
# coding: utf-8

# In[28]:


def selection_sort(items):
    """Sorts a list of items into ascending order.
    """
    for i in range(len(items)):
        i_min = i
        for j in range(i + 1, len(items)):
            if items[j] < items[i_min]:
                i_min = j
        if (i_min != i):
            items[i_min], items[i] = items[i], items[i_min]
    return items

