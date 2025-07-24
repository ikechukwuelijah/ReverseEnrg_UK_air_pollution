#"""


#Task: Crop the file to delete any records before 00:00 1 Jan 2010 (1262304000).
#"""


# I imported pandas lib.
import pandas as pd

# import data, I used the acronym 'baqd' to represent bristol air quality data, delimeter used for seperation
baqd = pd.read_csv("bristol-air-quality-data.csv", sep = ";",  low_memory = False)



# In[11]:


# I checked the data types
baqd.dtypes


# In[12]:


# I checked for data head

baqd.head()


# In[13]:


# I confirmed number of rows

index = baqd.index
number_of_rows = len(index)
print(" The file bristol-air-quality-data.csv" + " has " + str(number_of_rows) + " Lines.")


# In[15]:


# a. Crop the file to delete any records before 00:00 1 Jan 2010 (1262304000).

baqd_cropped = baqd[(baqd['Date Time'] >= '2010-01-01T00:00:00+00:00')]
index = baqd_cropped.index
number_of_rows = len(index)
print("The file bristol-air-quality-data.csv" + " has " + str(number_of_rows) + "Lines.")


# In[16]:


# I have my crop.csv

baqd_cropped.to_csv ("crop.csv", sep = ";", index = False)


# In[18]:


# I showed number of cropped file for final confirmation

print("crop.csv" + " has " + str(len(baqd_cropped.index)) + " lines.") 

