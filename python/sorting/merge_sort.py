#!/usr/bin/env python
# coding: utf-8

# In[4]:


def merge_sort(items):
    """Sorts a list of items in ascending order.
    """
    if (len(items) < 2):
        return items
    mid = len(items) // 2
    # Recursively split sublists.
    left = merge_sort(items[:mid])
    right = merge_sort(items[mid:])
    return merge(left, right)

def merge(left, right):
    i = j = 0
    m_list = []
    # Iterate through both sublists, appending to merged list whichever's value is lower.
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            m_list.append(left[i])
            i += 1
        else:
            m_list.append(right[j])
            j += 1
    # Append remaining elements.
    m_list += left[i:]
    m_list += right[j:]
    return m_list

