#!/usr/bin/env python
# coding: utf-8

# In[1]:


pwd


# In[2]:


cd OneDrive


# In[3]:


cd Desktop


# In[10]:


filename="sequence.fasta"


# In[11]:


from Bio import SeqIO
from Bio.SeqUtils import GC


# In[13]:


seq_object=SeqIO.read(filename, "fasta")
sequence=seq_object.seq


# In[14]:


len(sequence)


# In[15]:


print(sequence[0:20])


# In[16]:


gc_content=GC(sequence)


# In[17]:


print(gc_content)


# In[18]:


round(gc_content,2)


# In[21]:


sequence1="ATTTGTCGGTTGCGGGCCTTTAAAATATATGGGCCGCTGAATGGGCCCGCAAATGTCGTGATGCCTAAGTGGCGGCGAAATTGTAGATAGTACGTCGCTGA"
print(GC(sequence1))


# In[ ]:




