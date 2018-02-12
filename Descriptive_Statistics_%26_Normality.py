
# coding: utf-8

# In[169]:


import numpy as np


# In[170]:


import matplotlib.pyplot as plt 


# In[171]:


get_ipython().magic('matplotlib inline')


# In[176]:


bernoulli = np.random.binomial(1,.5, 100)


# In[209]:


plt.hist(bernoulli)
plt.axvline(bernoulli.mean(), color='b', linestyle='solid', linewidth=2)
plt.axvline(bernoulli.mean() + bernoulli.std(), color='b', linestyle='dashed', linewidth=2)
plt.axvline(bernoulli.mean()-bernoulli.std(), color='b', linestyle='dashed', linewidth=2) 
plt.show()


# In[195]:


np.mean(bernoulli)


# In[190]:


np.std(bernoulli)


# In[ ]:


#Helpful to understand two possible outcomes of an event. 


# In[111]:


binomial = np.random.binomial(20, 0.5, 100)


# In[207]:


plt.hist(binomial)
plt.axvline(binomial.mean(), color='b', linestyle='solid', linewidth=2)
plt.axvline(binomial.mean() + binomial.std(), color='b', linestyle='dashed', linewidth=2)
plt.axvline(binomial.mean()-binomial.std(), color='b', linestyle='dashed', linewidth=2) 
plt.show()


# In[79]:


np.mean(binomial)


# In[85]:


np.std(binomial)


# In[ ]:


#Helpful to count the number of successes when an event with two possible outcomes is repeated many times. 


# In[86]:


gamma = np.random.gamma(5, 1, 100)


# In[210]:


plt.hist(gamma)
plt.axvline(gamma.mean(), color='b', linestyle='solid', linewidth=2)
plt.axvline(gamma.mean() + gamma.std(), color='b', linestyle='dashed', linewidth=2)
plt.axvline(gamma.mean()-gamma.std(), color='b', linestyle='dashed', linewidth=2) 
plt.show()


# In[198]:


np.mean(gamma)


# In[155]:


np.std(gamma)


# In[156]:


#Represents the time unti an event (when event starts out unlikely), becomes more likely, then becomes more likely again, 
#and less likely afterward. 


# In[157]:


poisson = np.random.poisson(3, 100)


# In[211]:


plt.hist(poisson)
plt.axvline(poisson.mean(), color='b', linestyle='solid', linewidth=2)
plt.axvline(poisson.mean() + poisson.std(), color='b', linestyle='dashed', linewidth=2)
plt.axvline(poisson.mean()-poisson.std(), color='b', linestyle='dashed', linewidth=2) 
plt.show()


# In[93]:


np.mean(poisson)


# In[94]:


np.std(poisson)


# In[ ]:


#Represents the amount of time an event happens in a particular interval of time. 


# In[212]:


beta = np.random.beta(5, 1, 100)
plt.hist(beta)
plt.axvline(beta.mean(), color='b', linestyle='solid', linewidth=2)
plt.axvline(beta.mean() + beta.std(), color='b', linestyle='dashed', linewidth=2)
plt.axvline(beta.mean()-beta.std(), color='b', linestyle='dashed', linewidth=2) 
plt.show()


# In[99]:


np.mean(beta)


# In[100]:


np.std(beta)


# In[ ]:


#To model the behavior of random variables limited to intervals of finite length in a wide variety of disciplines.


# In[101]:


negative_binomial = np.random.negative_binomial(5, 1, 100)


# In[213]:


plt.hist(negative_binomial)
plt.axvline(negative_binomial.mean(), color='b', linestyle='solid', linewidth=2)
plt.axvline(negative_binomial.mean() + negative_binomial.std(), color='b', linestyle='dashed', linewidth=2)
plt.axvline(negative_binomial.mean()-negative_binomial.std(), color='b', linestyle='dashed', linewidth=2) 
plt.show()


# In[103]:


np.mean(negative_binomial)


# In[104]:


np.std(negative_binomial)


# In[ ]:


#Frequency distribution of the possible number of successful outcomes in a given number of trials in each of which
#there is the same probaility of success. 


# In[ ]:


#The skewed distributions have means and standard deviations further away from each other; whilst the "normal" distributions
#have a central tendency. But these other distributions are still useful with large amounts of data and serve their 
#specific purposes. #np.random.NORMAL 


# In[33]:


#Additionally


# In[133]:


var1 = np.random.normal(5,.5, 100)


# In[134]:


var2 = np.random.normal(10, 1, 100)


# In[135]:


var3 = var1+var2


# In[215]:


mean = np.mean(var3)


# In[216]:


sd = np.std(var3)


# In[217]:


plt.hist(var3)
plt.axvline(x=mean, color='black')
plt.axvline(x=mean+sd, color='red')
plt.axvline(x=mean-sd, color='red')
plt.show()


# In[ ]:


#Random seed will generate various results; results skew slightly in this normal distribution. 

