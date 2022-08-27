#!/usr/bin/env python
# coding: utf-8

# In[12]:


#The approach of this question is finding the Hours and Minutes Value of first alarm by finding the Minimum value of hours.
#Then we can find the time difference by keeping the hours and minutes difference of sleeping time and first alarm time.


t = int(input())
while t>0:
    n,h,m = map(int, input().split(" "))
    arr = [] #we will be making a list of all the alarm timing
    for i in range(n):
        arr.append(list(map(int,input().split(" ")))) #Hours and minutes of every alarm will be in form of sub lists of main list
    arr.sort() #Sorted the array to get the timing of first alarm
    h1 = arr[0][0] #Hours value of first alarm
    m1 = arr[0][1] #Minutes Value of second alarm
    if h<=h1: #If the first alarm timing lies within the same day of sleeping i.e. Vlad slept and woke up at same day(same 24 hours timing)
        hf = h1 - h - 1 #hf represents the hours of sleep. -1 to negate the minutes of sleep
        hm = (60-m) + m1 #hm represents the minutes of sleep.
        if hm>=60: #If hm value is greater than 60
            hf = hf+1 #Then value of hf is changed
            hm = hm%60 #Value  of hm is negated
    else: #If the first alarm timing does not lie within the same day of sleeping i.e. Vlad did not sleep and wake up at same day(same 24 hours timing)
        hf = (24-h) + h1 -1 #First day 24 hours cycle is completed first then rest of the hours added. -1 to negate the minutes of sleep.
        hm = (60-m) + m1  #hm represents the minutes of sleep
        if hm>=60: #If hm value is greater than 60
            hf = hf+1 #Then value of hf is changed
            hm = hm%60 #Value  of hm is negated
    print(hf,hm) #We get the value of Hours and Minutes of sleep
    t =  t-1


# In[ ]:




