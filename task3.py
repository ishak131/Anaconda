#!/usr/bin/env python
# coding: utf-8

# In[2]:


import networkx as nx
G = nx.Graph()
G.add_nodes_from([1,2,3,4,5,6])
G.add_edges_from([(1,2),(2,3),(1,3),(1,4),(2,5),(3,6)])
nx.draw(G, with_labels=True,
       node_color='pink',
        node_size=1300,
        font_color='black',
        font_size=20,
        edge_color='blue',
        
       )


# In[ ]:





# In[7]:


nx.has_path(G, 3, 5)


# In[8]:


nx.has_path(G, 4, 6)


# In[9]:


nx.all_simple_paths(G, 3, 4)


# In[10]:


list(nx.all_simple_paths(G, 3, 4))


# In[27]:


list(nx.all_simple_paths(G, 1, 6))


# In[16]:


nx.shortest_path_length(G, 2, 4)


# In[22]:


nx.shortest_path(G,2,4)


# In[28]:


nx.is_connected(G)


# In[40]:


G=nx.Graph()
nx.add_cycle(G,(1,2,3 , 4 , 5, 6))
G.add_edge(7,8)
nx.draw(G, with_labels=True,
       node_color='red',
        node_size=1300,
        font_color='black',
        font_size=20,
        edge_color='blue',
        
       )


# In[41]:


nx.is_connected(G)


# In[43]:


nx.has_path(G ,6,7)


# In[47]:


nx.shortest_path(G , 3,6)


# In[48]:


nx.number_connected_components(G)


# In[49]:


list(nx.connected_components(G))


# In[50]:


c=list(nx.connected_components(G))
len(c[0])


# In[53]:


c=list(nx.connected_components(G))
len(c[1])


# In[59]:


max(nx.connected_components(G), key=len)


# In[55]:


min(nx.connected_components(G), key=len)


# In[78]:


code_nodes = max(nx.connected_components(G), key=len)
core = G.subgraph(code_nodes)
nx.draw(core, with_labels=True,
       node_color='green',
        node_size=1300,
        font_color='red',
        font_size=20,
        edge_color='blue',
        
       )


# In[75]:


Di = nx.DiGraph()
Di.add_edges_from([
    (1,2),
    (2,3),
    (3,2), (3,4), (3,5),
    (4,2), (4,5), (4,6),
    (5,6),
    (6,4),
])
nx.draw(Di, 
        with_labels=True,
        node_color='yellow',
        node_size=1500,
        font_color='red',
        font_size=20,
        edge_color='blue',
       )


# In[79]:


nx.has_path(Di , 1,2)


# In[80]:


nx.has_path(Di ,2 ,1)


# In[87]:


nx.shortest_path(Di , 2,5)


# In[88]:


list(nx.all_simple_paths(Di , 2 ,5))


# In[83]:


nx.shortest_path(Di ,5 , 2)


# In[85]:


nx.is_strongly_connected(Di)


# In[90]:


nx.is_weakly_connected(Di)


# In[92]:


list(nx.weakly_connected_components(Di))


# In[93]:


list(nx.strongly_connected_components(Di))


# In[5]:


G = nx.read_graphml('D:/FirstCourseNetworkScience/datasets/openflights/openflights_usa.graphml.gz')
G.nodes['IND']


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[97]:


G.nodes['IND']['name']


# In[ ]:




