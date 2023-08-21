#!/usr/bin/env python
# coding: utf-8

# In[4]:


pip install pymongo


# In[3]:


import pymongo


# In[1]:


pip install pymongo


# In[2]:


import pymongo


# In[8]:


client=pymongo.MongoClient("mongodb+srv://admin:admin123@sanjay.zmjzfmd.mongodb.net/")


# In[9]:


db=client["mydb"]


# In[10]:


collection=db["mycoll"]


# In[11]:


data=[{"name":"sanjay","age":"22","city":"chennai"},{"name":"akash","age":"22","city":"chennai"},{"name":"gerwin","age":"21","city":"chennai"}]


# In[12]:


inserted_document=collection.insert_one(data[0])


# In[13]:


print("inserted:",inserted_document.inserted_id)


# In[14]:


inserted_documents=collection.insert_many(data[1:])


# In[15]:


print("inserted:",inserted_documents.inserted_ids)


# In[17]:


result=collection.find()
for document in result:
    print(document)


# In[18]:


update_query={"name":"gerwin"}
new={"$set":{"age":22}}
collection.update_one(update_query,new)
print("document updated successfully")


# In[19]:


delete={"name":"sanjay"}
collection.delete_one(delete)


# In[ ]:




