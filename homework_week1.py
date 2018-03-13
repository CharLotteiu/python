
# coding: utf-8

# In[1]:


2 + 2


# In[4]:


s= "hello"+" world"
s


# In[5]:


s[5]


# In[6]:


s[6]


# In[7]:


s[0:5]


# In[8]:


s="LIU "+"Lingling"
s


# In[9]:


len(s)


# In[10]:


a=[3, 3.14, 'LIU', 1.414+5]
a


# In[11]:


a+a


# In[12]:


a+=a
a


# In[13]:


len(a)


# In[14]:


a[4]


# In[15]:


a.append('Lingling')


# In[16]:


a


# In[17]:


str=a[2]+a[8]
str


# In[18]:


b={3,4,5,6,7}
b


# In[19]:


b.add(3.14)
b


# In[20]:


a={3.14,4}
a & b


# In[21]:


a | b


# In[22]:


a - b


# In[23]:


b - a


# In[24]:


a ^ b


# In[25]:


b ^ a


# In[26]:


d = {'liu':0, 'yi':1, 'wang':5}
d


# In[27]:


len(d)


# In[28]:


d['liu']


# In[29]:


d.keys()


# In[30]:


d['yi']=2
d


# In[32]:


d.items()


# In[33]:


d.values()


# In[35]:


from numpy import array
a = array([1, 2, 3, 4])
a


# In[36]:


a+3


# In[37]:


a+a+a


# In[38]:


line="LIU Lingling"
fields = line.split()
fields


# In[46]:


s = ""
for field in fields:
    s+=field
s


# In[47]:


cd~


# In[43]:


f = open('test.txt','w')
f.write('LIU Lingling\n')
f.write('LIU Zhi\n')
f.close()


# In[60]:


f = open('test.txt')
data = f.read()
strs=data.split()


# In[61]:


strs


# In[62]:


print data

