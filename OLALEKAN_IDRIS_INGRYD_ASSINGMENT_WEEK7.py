#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import statistics #importing the stat module to calculate some stats methods


#list of temperatures of patients
temp =[16,17,18,19,20,36,37,37,38,39,40,41,43,44,45,46,47,48,49,50]


#mean of temperature
mean = statistics.mean(temp)

#median of temperature
median = statistics.median(temp)

#Mode of temperature
mode = statistics.mode(temp)

#Range of temperature
Range = max(temp)-min(temp)

#StandardDeviation of temperature
stndard_dev =statistics.stdev(temp)

#Variance of temperature
Var = statistics.variance(temp)

# mean_dev = statistics.mdev(temp)
print(f"Mean:{mean:.2f}")
print(f"Median:{median:.2f}")
print(f"Mode:{mode:.2f}")
print(f"Range:{Range:.2f}")
print(f"Standard_Deviation:{stndard_dev:.2f}")
print(f"Variance:{Var:.2f}")

