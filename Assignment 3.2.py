
# coding: utf-8

# In[1]:


word="ACADGILD"
my_list=[x for x in word]
print(my_list)


# In[5]:


word1="XYZ"
my_list1=[x*i for x in word1 for i in range(1,5)]
print(my_list1)


# In[6]:


set1=[1,2,3]
unique_set=[(x,y) for x in set1 for y in set1]
print(unique_set)


# In[1]:


set2=["x","y","z"]
my_list2=[x*i for i in range(1,5) for x in set2 ]
print(my_list2)


# In[8]:


my_list3=[[j] for i in range(2,5) for j in range(i,i+3)  ]
print(my_list3)


# In[16]:


my_list4=[[j for j in range(i,i+4)] for i in range(2,6)    ]
print(my_list4)

