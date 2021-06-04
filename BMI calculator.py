#!/usr/bin/env python
# coding: utf-8

# In[7]:


import csv
import json


# In[20]:


with open("C:\\Users\\Tarun\\Desktop\\data.json",'r') as data:
    data_dict= json.load(data)
details = data_dict['person_details']    


# In[22]:


data_file = open('data_file.csv','w')
csv_writer = csv.writer(data_file)


# In[23]:


count = 0
for detail in details:
    if count ==0:
        header = detail.keys()
        csv_writer.writerow(header)
        count += 1
    csv_writer.writerow(detail.values())
    
data_file.close()    
        


# In[25]:


df=pd.read_csv('data_file.csv')      
df


# In[26]:


df['HeightinM'] = df['HeightCm'].div(100)


# In[27]:


df


# In[28]:


df['BMI'] = df['WeightKg'].div(df['HeightinM']).round(2)


# In[29]:


df


# In[41]:


health_risk=[]


# In[42]:


for i in range(0,len(df['BMI'])):
    if(df['BMI'][i]<18.5):
        health_risk.append("Malnutrition")
    elif(df['BMI'][i]>=18.5 and df['BMI'][i]<24.9):
        health_risk.append("Low")
    elif(df['BMI'][i]>=25.0 and df['BMI'][i]<29.9):
        health_risk.append("Enhanced")
    elif(df['BMI'][i]>=30.0 and df['BMI'][i]<34.9):
        health_risk.append("Medium")
    elif(df['BMI'][i]>=35.0 and df['BMI'][i]<39.9):
        health_risk.append("High")
    elif(df['BMI'][i]>=40.0):
        health_risk.append("Very high")
health_risk


# In[43]:


df['Health_Risk'] = health_risk


# In[38]:


overweight_count = 0

for o in range(0,len(df['BMI'])):
    if(df['BMI'][o] >= 25 and df['BMI'][o] < 29.9):
        overweight_count =overweight_count + 1
overweight_count


# In[44]:


df


# In[ ]:




