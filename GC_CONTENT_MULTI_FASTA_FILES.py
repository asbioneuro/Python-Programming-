#!/usr/bin/env python
# coding: utf-8

# In[5]:


from Bio import SeqIO
from Bio.SeqUtils import GC
import pandas as pd


# In[11]:


filename="multi_gene_sequence.fasta"


# In[12]:


seq_objects=SeqIO.parse(filename,"fasta")


# In[13]:


sequences=[seq for seq in seq_objects]


# In[14]:


number_of_sequences=len(sequences)
print(number_of_sequences)


# In[15]:


for seq in sequences:
    seq_id=seq.id
    sequence=seq.seq
    gc_content=GC(sequence)
    gc_content=round(gc_content,2)
    print(seq_id, gc_content)


# In[19]:


seq_ids=[]
gc_contents=[]


for seq in sequences:
    seq_id=seq.id
    sequence=seq.seq
    gc_content=GC(sequence)
    gc_content=round(gc_content,2)
    
    seq_ids.append(seq_id)
    gc_contents.append(gc_content)
    
    print('GC CONTENT HAS BEEN COMPUTED SUCCESSFULLY')


# In[20]:


print(seq_ids)


# In[21]:


print(gc_contents)


# In[23]:


dataframe=pd.DataFrame()
dataframe['Sequence_ID']=seq_ids
dataframe['GC_content']=gc_contents


# In[24]:


print(dataframe.shape)


# In[25]:


print(dataframe)


# In[27]:


output_file="gc_content.csv"
dataframe.to_csv(output_file, index=False)

