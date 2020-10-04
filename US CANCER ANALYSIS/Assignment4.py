
# coding: utf-8

# # Assignment 4
# 
# Before working on this assignment please read these instructions fully. In the submission area, you will notice that you can click the link to **Preview the Grading** for each step of the assignment. This is the criteria that will be used for peer grading. Please familiarize yourself with the criteria before beginning the assignment.
# 
# This assignment requires that you to find **at least** two datasets on the web which are related, and that you visualize these datasets to answer a question with the broad topic of **sports or athletics** (see below) for the region of **Ann Arbor, Michigan, United States**, or **United States** more broadly.
# 
# You can merge these datasets with data from different regions if you like! For instance, you might want to compare **Ann Arbor, Michigan, United States** to Ann Arbor, USA. In that case at least one source file must be about **Ann Arbor, Michigan, United States**.
# 
# You are welcome to choose datasets at your discretion, but keep in mind **they will be shared with your peers**, so choose appropriate datasets. Sensitive, confidential, illicit, and proprietary materials are not good choices for datasets for this assignment. You are welcome to upload datasets of your own as well, and link to them using a third party repository such as github, bitbucket, pastebin, etc. Please be aware of the Coursera terms of service with respect to intellectual property.
# 
# Also, you are welcome to preserve data in its original language, but for the purposes of grading you should provide english translations. You are welcome to provide multiple visuals in different languages if you would like!
# 
# As this assignment is for the whole course, you must incorporate principles discussed in the first week, such as having as high data-ink ratio (Tufte) and aligning with Cairo’s principles of truth, beauty, function, and insight.
# 
# Here are the assignment instructions:
# 
#  * State the region and the domain category that your data sets are about (e.g., **Ann Arbor, Michigan, United States** and **sports or athletics**).
#  * You must state a question about the domain category and region that you identified as being interesting.
#  * You must provide at least two links to available datasets. These could be links to files such as CSV or Excel files, or links to websites which might have data in tabular form, such as Wikipedia pages.
#  * You must upload an image which addresses the research question you stated. In addition to addressing the question, this visual should follow Cairo's principles of truthfulness, functionality, beauty, and insightfulness.
#  * You must contribute a short (1-2 paragraph) written justification of how your visualization addresses your stated research question.
# 
# What do we mean by **sports or athletics**?  For this category we are interested in sporting events or athletics broadly, please feel free to creatively interpret the category when building your research question!
# 
# ## Tips
# * Wikipedia is an excellent source of data, and I strongly encourage you to explore it for new data sources.
# * Many governments run open data initiatives at the city, region, and country levels, and these are wonderful resources for localized data sources.
# * Several international agencies, such as the [United Nations](http://data.un.org/), the [World Bank](http://data.worldbank.org/), the [Global Open Data Index](http://index.okfn.org/place/) are other great places to look for data.
# * This assignment requires you to convert and clean datafiles. Check out the discussion forums for tips on how to do this from various sources, and share your successes with your fellow students!
# 
# ## Example
# Looking for an example? Here's what our course assistant put together for the **Ann Arbor, MI, USA** area using **sports and athletics** as the topic. [Example Solution File](./readonly/Assignment4_example.pdf)

# In[2]:

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
get_ipython().magic('matplotlib notebook')
get_ipython().magic('pinfo pd.read_excel')


# In[3]:

cancer_death_rates = pd.read_excel('DeathEstimates (1).xlsx')
cancer_estimates_rates = pd.read_excel('NewCaseEstimates.xlsx',skiprows = 1)
cancer_death_rates_all = cancer_death_rates[['State','Lung and bronchus','Melanoma of the skin','Prostate','All cancer types combined']]
cancer_death_rates = cancer_death_rates[['State','Lung and bronchus','Melanoma of the skin','Prostate']]

cancer_death_rates=cancer_death_rates.set_index('State')
cancer_death_rates = cancer_death_rates.drop(['All U.S. combined','Puerto Rico'])
def change_unknow_value (row):
    data = row[['Lung and bronchus','Melanoma of the skin','Prostate','All cancer types combined']]
    #print ((data['Lung and bronchus'][0]))
    if row['Lung and bronchus'][0] == 'N':
        row['Lung and bronchus'] = '0'
    row['Lung and bronchus']=int(row['Lung and bronchus'])
    if row['Melanoma of the skin'][0] == 'N':
        row['Melanoma of the skin'] = '0'
        #print (row['Melanoma of the skin'])
    row['Melanoma of the skin']=int(row['Melanoma of the skin'])
    if row['Prostate'][0] == 'N':
        row['Prostate'] = '0'
    row['Prostate']=int(row['Prostate'])
    #if row['All cancer types combined'][0] == 'N':
        #row['All cancer types combined'] = '0'  
    #row['All cancer types combined']=int(row['All cancer types combined'])
    #print ((data['Lung and bronchus']))
    #print (row)
    #print ('  ')
    return (row)
    
cancer_death_rates =cancer_death_rates.apply(change_unknow_value ,axis =1)
cancer_death_rates = cancer_death_rates.reset_index()


# In[4]:

#plt.style.use('seaborn-colorblind')
cancer_death_rates.rename(columns={'Lung and bronchus':'Lung Cancer',
                                   'Melanoma of the skin': 'Skin Cancer',
                                   'Prostate': 'Prostate Cancer'},inplace=True)
#fig1 =plt.figure()
#cancer_chart_1 = fig1.add_subplot(111)
cancer_chart_1=cancer_death_rates.plot()
plt.gcf().set_size_inches(10,5)
#plt.tick_params(axis='x', which='major', labelsize=10)
plt.xticks(np.arange(-1,52),cancer_death_rates['State'].values.tolist(),rotation = 90)

plt.xlabel('States of USA')
plt.ylabel('Number of cancer death estmated in year 2020')


# In[ ]:




# In[ ]:




# In[ ]:



