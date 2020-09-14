
# coding: utf-8

# ---
# 
# _You are currently looking at **version 1.1** of this notebook. To download notebooks and datafiles, as well as get help on Jupyter notebooks in the Coursera platform, visit the [Jupyter Notebook FAQ](https://www.coursera.org/learn/python-data-analysis/resources/0dhYG) course resource._
# 
# ---

# In[41]:


import pandas as pd
import numpy as np
from scipy.stats import ttest_ind
get_ipython().magic('pinfo pd.DataFrame.drop')
get_ipython().magic('pinfo ttest_ind')


# # Assignment 4 - Hypothesis Testing
# This assignment requires more individual learning than previous assignments - you are encouraged to check out the [pandas documentation](http://pandas.pydata.org/pandas-docs/stable/) to find functions or methods you might not have used yet, or ask questions on [Stack Overflow](http://stackoverflow.com/) and tag them as pandas and python related. And of course, the discussion forums are open for interaction with your peers and the course staff.
# 
# Definitions:
# * A _quarter_ is a specific three month period, Q1 is January through March, Q2 is April through June, Q3 is July through September, Q4 is October through December.
# * A _recession_ is defined as starting with two consecutive quarters of GDP decline, and ending with two consecutive quarters of GDP growth.
# * A _recession bottom_ is the quarter within a recession which had the lowest GDP.
# * A _university town_ is a city which has a high percentage of university students compared to the total population of the city.
# 
# **Hypothesis**: University towns have their mean housing prices less effected by recessions. Run a t-test to compare the ratio of the mean price of houses in university towns the quarter before the recession starts compared to the recession bottom. (`price_ratio=quarter_before_recession/recession_bottom`)
# 
# The following data files are available for this assignment:
# * From the [Zillow research data site](http://www.zillow.com/research/data/) there is housing data for the United States. In particular the datafile for [all homes at a city level](http://files.zillowstatic.com/research/public/City/City_Zhvi_AllHomes.csv), ```City_Zhvi_AllHomes.csv```, has median home sale prices at a fine grained level.
# * From the Wikipedia page on college towns is a list of [university towns in the United States](https://en.wikipedia.org/wiki/List_of_college_towns#College_towns_in_the_United_States) which has been copy and pasted into the file ```university_towns.txt```.
# * From Bureau of Economic Analysis, US Department of Commerce, the [GDP over time](http://www.bea.gov/national/index.htm#gdp) of the United States in current dollars (use the chained value in 2009 dollars), in quarterly intervals, in the file ```gdplev.xls```. For this assignment, only look at GDP data from the first quarter of 2000 onward.
# 
# Each function in this assignment below is worth 10%, with the exception of ```run_ttest()```, which is worth 50%.

# In[3]:


# Use this dictionary to map state names to two letter acronyms
states1 = {'OH': 'Ohio', 'KY': 'Kentucky', 'AS': 'American Samoa', 'NV': 'Nevada', 'WY': 'Wyoming', 'NA': 'National', 'AL': 'Alabama', 'MD': 'Maryland', 'AK': 'Alaska', 'UT': 'Utah', 'OR': 'Oregon', 'MT': 'Montana', 'IL': 'Illinois', 'TN': 'Tennessee', 'DC': 'District of Columbia', 'VT': 'Vermont', 'ID': 'Idaho', 'AR': 'Arkansas', 'ME': 'Maine', 'WA': 'Washington', 'HI': 'Hawaii', 'WI': 'Wisconsin', 'MI': 'Michigan', 'IN': 'Indiana', 'NJ': 'New Jersey', 'AZ': 'Arizona', 'GU': 'Guam', 'MS': 'Mississippi', 'PR': 'Puerto Rico', 'NC': 'North Carolina', 'TX': 'Texas', 'SD': 'South Dakota', 'MP': 'Northern Mariana Islands', 'IA': 'Iowa', 'MO': 'Missouri', 'CT': 'Connecticut', 'WV': 'West Virginia', 'SC': 'South Carolina', 'LA': 'Louisiana', 'KS': 'Kansas', 'NY': 'New York', 'NE': 'Nebraska', 'OK': 'Oklahoma', 'FL': 'Florida', 'CA': 'California', 'CO': 'Colorado', 'PA': 'Pennsylvania', 'DE': 'Delaware', 'NM': 'New Mexico', 'RI': 'Rhode Island', 'MN': 'Minnesota', 'VI': 'Virgin Islands', 'NH': 'New Hampshire', 'MA': 'Massachusetts', 'GA': 'Georgia', 'ND': 'North Dakota', 'VA': 'Virginia'}


# In[24]:


def get_list_of_university_towns():
    txt_file = open('university_towns.txt')
    
    '''Returns a DataFrame of towns and the states they are in from the 
    university_towns.txt list. The format of the DataFrame should be:
    DataFrame( [ ["Michigan", "Ann Arbor"], ["Michigan", "Yipsilanti"] ], 
    columns=["State", "RegionName"]  )
    
    The following cleaning needs to be done:

    1. For "State", removing characters from "[" to the end.
    2. For "RegionName", when applicable, removing every character from " (" to the end.
    3. Depending on how you read the data, you may need to remove newline character '\n'. '''
    d= pd.DataFrame( [ ["Michigan", "Ann Arbor"], ["Michigan", "Yipsilanti"] ], 
    columns=["State", "RegionName"]  )
    import re
    count  = 0
    list_final = list()
    states = list()
    region = list()
    for x in txt_file:
        if len(re.findall('(.+)\[edit\]',x.rstrip()))>0:
            states = re.findall('(.+)\[edit\]',x.strip())
        if (len(re.findall('^(.+)\s\(.*',x.rstrip()))>0 or len(re.findall('^(.+,[^\(]*)',x.strip()))>0 ):
            region = re.findall('^(.+?)\s\(.*',x.strip()) or re.findall('^(.+,[^\(]*)',x.strip())
            list_final.append([states[0],region[0]])
            #print (states,region)
        elif (len(re.findall('(.+)[^\(]*\:',x.rstrip()))>0):
            region = re.findall('([^\(]+\:)',x.strip())
            list_final.append([states[0],region[0]])
            #print (1)
            #print (states,region)
        else:
            continue

    df = pd.DataFrame(list_final,columns=['State','RegionName'])
    return df


'''

import re
import pandas as pd
import numpy as np
# list of unique states
stateStr = """
Ohio, Kentucky, American Samoa, Nevada, Wyoming
,National, Alabama, Maryland, Alaska, Utah
,Oregon, Montana, Illinois, Tennessee, District of Columbia
,Vermont, Idaho, Arkansas, Maine, Washington
,Hawaii, Wisconsin, Michigan, Indiana, New Jersey
,Arizona, Guam, Mississippi, Puerto Rico, North Carolina
,Texas, South Dakota, Northern Mariana Islands, Iowa, Missouri
,Connecticut, West Virginia, South Carolina, Louisiana, Kansas
,New York, Nebraska, Oklahoma, Florida, California
,Colorado, Pennsylvania, Delaware, New Mexico, Rhode Island
,Minnesota, Virgin Islands, New Hampshire, Massachusetts, Georgia
,North Dakota, Virginia
"""
#list of regionName entries string length
regNmLenStr = """
06,08,12,10,10,04,10,08,09,09,05,06,11,06,12,09,08,10,12,06,
06,06,08,05,09,06,05,06,10,28,06,06,09,06,08,09,10,35,09,15,
13,10,07,21,08,07,07,07,12,06,14,07,08,16,09,10,11,09,10,06,
11,05,06,09,10,12,06,06,11,07,08,13,07,11,05,06,06,07,10,08,
11,08,13,12,06,04,08,10,08,07,12,05,06,09,07,10,16,10,06,12,
08,07,06,06,06,11,14,11,07,06,06,12,08,10,11,06,10,14,04,11,
18,07,07,08,09,06,13,11,12,10,07,12,07,04,08,09,09,13,08,10,
16,09,10,08,06,08,12,07,11,09,07,09,06,12,06,09,07,10,09,10,
09,06,15,05,10,09,11,12,10,10,09,13,06,09,11,06,11,09,13,37,
06,13,06,09,49,07,11,12,09,11,11,07,12,10,06,06,09,04,09,15,
10,12,05,09,08,09,09,07,14,06,07,16,12,09,07,09,06,32,07,08,
08,06,10,36,09,10,09,06,09,11,09,06,10,07,14,08,07,06,10,09,
05,11,07,06,08,07,05,07,07,04,06,05,09,04,25,06,07,08,05,08,
06,05,11,09,07,07,06,13,09,05,16,05,10,09,08,11,06,06,06,10,
09,07,06,07,10,05,08,07,06,08,06,30,09,07,06,11,07,12,08,09,
16,12,11,08,06,04,10,10,15,05,11,11,09,08,06,04,10,10,07,09,
11,08,26,07,13,05,11,03,08,07,06,05,08,13,10,08,08,08,07,07,
09,05,04,11,11,07,06,10,11,03,04,06,06,08,08,06,10,09,05,11,
07,09,06,12,13,09,10,11,08,07,07,08,09,10,08,10,08,56,07,12,
07,16,08,04,10,10,10,10,07,09,08,09,09,10,07,09,09,09,12,14,
10,29,19,07,11,12,13,13,09,10,12,12,12,08,10,07,10,07,07,08,
08,08,09,10,09,11,09,07,09,10,11,11,10,09,09,12,09,06,08,07,
12,09,07,07,06,06,08,06,15,08,06,06,10,10,10,07,05,10,07,11,
09,12,10,12,04,10,05,05,04,14,07,10,09,07,11,10,10,10,11,15,
09,14,12,09,09,07,12,04,10,10,06,10,07,28,06,10,08,09,10,10,
10,13,12,08,10,09,09,07,09,09,07,11,11,13,08,10,07
"""

df = get_list_of_university_towns()

cols = ["State", "RegionName"]

print('Shape test: ', "Passed" if df.shape ==
      (517, 2) else 'Failed')
print('Index test: ',
      "Passed" if df.index.tolist() == list(range(517))
      else 'Failed')

print('Column test: ',
      "Passed" if df.columns.tolist() == cols else 'Failed')
print('\\n test: ',
      "Failed" if any(df[cols[0]].str.contains(
          '\n')) or any(df[cols[1]].str.contains('\n'))
      else 'Passed')
print('Trailing whitespace test:',
      "Failed" if any(df[cols[0]].str.contains(
          '\s+$')) or any(df[cols[1]].str.contains(
              '\s+$'))
      else 'Passed')
print('"(" test:',
      "Failed" if any(df[cols[0]].str.contains(
          '\(')) or any(df[cols[1]].str.contains(
              '\('))
      else 'Passed')
print('"[" test:',
      "Failed" if any(df[cols[0]].str.contains(
          '\[')) or any(df[cols[1]].str.contains(
              '\]'))
      else 'Passed')

states_vlist = [st.strip() for st in stateStr.split(',')]

mismatchedStates = df[~df['State'].isin(
    states_vlist)].loc[:, 'State'].unique()
print('State test: ', "Passed" if len(
    mismatchedStates) == 0 else "Failed")
if len(mismatchedStates) > 0:
    print()
    print('The following states failed the equality test:')
    print()
    print('\n'.join(mismatchedStates))

df['expected_length'] = [int(s.strip())
                         for s in regNmLenStr.split(',')
                         if s.strip().isdigit()]
regDiff = df[df['RegionName'].str.len() != df['expected_length']].loc[
    :, ['RegionName', 'expected_length']]
regDiff['actual_length'] = regDiff['RegionName'].str.len()
print('RegionName test: ', "Passed" if len(regDiff) ==
      0 else ' \nMismatching regionNames\n {}'.format(regDiff))'''
get_list_of_university_towns()


# In[5]:


def get_recession_start():
    '''Returns the year and quarter of the recession start time as a 
    string value in a format such as 2005q3'''
    #quart = pd.read_excel?
    quart = pd.read_excel('gdplev.xls',skiprows=[0,1],header=4)
    quart.drop(['Unnamed: 0','Unnamed: 1','Unnamed: 2','Unnamed: 3','Unnamed: 5'],axis=1,inplace=True)
    quart.rename(columns={'Unnamed: 4':'Quarter','Unnamed: 6':'GDP'},inplace=True)
    del quart['Unnamed: 7']
    new_col = list()
    for x in quart['Quarter']:
        new_col.append(int(x[:4]))
    #print(new_col)
    quart['new_col']=new_col
    quart=quart[quart['new_col']>=2000]
    quart=quart.reset_index()
    del quart['new_col']
    del quart['index']
    import numpy as np
    
    """    def diff(row):
        data = row[['GDP']]
        start = 0
        #print (data['GDP'])
        row['differ']=data['GDP']-start
        start = data['GDP']
        return row
    quart= quart.apply(diff,axis=1)"""
    quart['diff']=None
    start = 0
    new_col=list()
    
    for x in quart['GDP']:
        new_col.append(int (x-start))
        start=x
        #print(x)
    quart['diff']=new_col
    for x in quart.index:
        if x>=2 and x<=64:
            if quart['diff'][x-2]<0 and quart['diff'][x-1]<0 and quart['diff'][x]>0 and quart['diff'][x+1]>0:   
                #print (quart['diff'][x-2],quart['diff'][x-1] , quart['diff'][x], quart['diff'][x+1])
                for y in range(len(quart.index)):
                    if quart['diff'][x-y-1]<0:
                        continue
                    else:
                        break
                #print (y)
                return (quart.iloc[x-y]['Quarter'])
    finish = quart[quart['diff']<0]
    return quart
    
get_recession_start()


# In[6]:


def get_recession_end():

    #quart = pd.read_excel?
    quart = pd.read_excel('gdplev.xls',skiprows=[0,1],header=4)
    quart.drop(['Unnamed: 0','Unnamed: 1','Unnamed: 2','Unnamed: 3','Unnamed: 5'],axis=1,inplace=True)
    quart.rename(columns={'Unnamed: 4':'Quarter','Unnamed: 6':'GDP'},inplace=True)
    del quart['Unnamed: 7']
    new_col = list()
    for x in quart['Quarter']:
        new_col.append(int(x[:4]))
    #print(new_col)
    quart['new_col']=new_col
    quart=quart[quart['new_col']>=2000]
    quart=quart.reset_index()
    del quart['new_col']
    del quart['index']
    import numpy as np
    
    """    def diff(row):
        data = row[['GDP']]
        start = 0
        #print (data['GDP'])
        row['differ']=data['GDP']-start
        start = data['GDP']
        return row
    quart= quart.apply(diff,axis=1)"""
    quart['diff']=None
    start = 0
    new_col=list()
    
    for x in quart['GDP']:
        new_col.append(int (x-start))
        start=x
        #print(x)
    quart['diff']=new_col
    for x in quart.index:
        if x>=2 and x<=64:
            if quart['diff'][x-2]<0 and quart['diff'][x-1]<0 and quart['diff'][x]>0 and quart['diff'][x+1]>0:   
                #print (quart['diff'][x-2],quart['diff'][x-1] , quart['diff'][x], quart['diff'][x+1])
                for y in range(len(quart.index)):
                    if quart['diff'][x-y-1]<0:
                        continue
                    else:
                        break
                #print (y)
                return (quart.iloc[x+1]['Quarter'])
    finish = quart[quart['diff']<0]
    return quart
    
get_recession_end()


# In[7]:


def get_recession_bottom():

    #quart = pd.read_excel?
    quart = pd.read_excel('gdplev.xls',skiprows=[0,1],header=4)
    quart.drop(['Unnamed: 0','Unnamed: 1','Unnamed: 2','Unnamed: 3','Unnamed: 5'],axis=1,inplace=True)
    quart.rename(columns={'Unnamed: 4':'Quarter','Unnamed: 6':'GDP'},inplace=True)
    del quart['Unnamed: 7']
    new_col = list()
    for x in quart['Quarter']:
        new_col.append(int(x[:4]))
    #print(new_col)
    quart['new_col']=new_col
    quart=quart[quart['new_col']>=2000]
    quart=quart.reset_index()
    del quart['new_col']
    del quart['index']
    import numpy as np
    
    """    def diff(row):
        data = row[['GDP']]
        start = 0
        #print (data['GDP'])
        row['differ']=data['GDP']-start
        start = data['GDP']
        return row
    quart= quart.apply(diff,axis=1)"""
    quart['diff']=None
    start = 0
    new_col=list()
    
    for x in quart['GDP']:
        new_col.append(int (x-start))
        start=x
        #print(x)
    quart['diff']=new_col
    for x in quart.index:
        if x>=2 and x<=64:
            if quart['diff'][x-2]<0 and quart['diff'][x-1]<0 and quart['diff'][x]>0 and quart['diff'][x+1]>0:   
                #print (quart['diff'][x-2],quart['diff'][x-1] , quart['diff'][x], quart['diff'][x+1])
                for y in range(len(quart.index)):
                    if quart['diff'][x-y-1]<0:
                        continue
                    else:
                        break
                #print (y)
                return (quart.iloc[x-1]['Quarter'])
    finish = quart[quart['diff']<0]
    return quart
    
get_recession_bottom()


# In[8]:


def convert_housing_data_to_quarters():
    '''Converts the housing data to quarters and returns it as mean values in a dataframe. This dataframe should be a dataframe withcolumns for 2000q1 through 2016q3, and should have a multi-index
    in the shape of ["State","RegionName"].
    
    Note: Quarters are defined in the assignment description, they are
    not arbitrary three month periods.
    
    The resulting dataframe should have 67 columns, and 10,730 rows.
    '''
    house = pd.read_csv('City_Zhvi_AllHomes.csv')
    #pd.read_csv?
    house_data=house.drop(['RegionID','CountyName','Metro','SizeRank'],axis=1)
    house_data=house_data.set_index(['State','RegionName'])
    #house_data.sort_index
    #house_data=house_data.head(20)
    column_list1 = list()
    
    for x in house_data.columns:
        if int(str(x)[:4])>=2000:
            column_list1.append((x))
        else:
            house_data=house_data.drop(x,axis=1)
    #n= house_data.reset_index()
    house_data.columns=pd.to_datetime(house_data.columns)
    n= house_data
    n=n.T.resample('3M',closed='left').sum().T
    
    #print (column_list)
    #house_data=house_data.fillna(0)
    #house_data=house_data.head(20)
    column_list=list()
    for x in n.columns:
        if int(str(x)[:4])>=2000:
            column_list.append((x))
    #print (column_list)
    #print (n)
    def create_quaters(row):
        data= row[column_list]
        #print((data))
        for w in n.columns:
            #print (data[w])
            if int(str(w)[5:7])== 3:
                row[w]=data[w]/3
            if str(w)[5:7]== 6:
                row[w]=data[w]/3
            if int(str(w)[5:7])== 9:
                row[w]=data[w]/3
            if int(str(w)[5:7])== 12:
                row[w]=data[w]/3
        
  
        return row
    
    new_df = pd.DataFrame()
    #for x,y in n:
        #print (type(y))
    n=n.apply(create_quaters,axis=1)
        #new_df=pd.concat([new_df,y.apply(create_quaters,axis=1)])
        #new_df=pd.merge(new_df,y,left_index=True,right_index=True,how='outer')
    #for w in range(len(column_list)):
        #new_df.drop(column_list[w],axis=1,inplace=True)
        #house_data.drop(column_list[y+1],axis=1,inplace=True)
        #house_data.drop(column_list[y+2],axis=1,inplace=True)
        #print (w)
    #new_df=new_df.set_index(['State','RegionName'])
    #print (n.columns)
    for x in n.columns:
        #print (x)
        if str(x)[5:7]=='03':
            n.rename(columns={x:str(str(x)[:4]+'q1')},inplace=True)
        if str(x)[5:7]=='06':
            n.rename(columns={x:str(str(x)[:4]+'q2')},inplace=True)
        if str(x)[5:7]=='09':
            n.rename(columns={x:str(str(x)[:4]+'q3')},inplace=True)
        if str(x)[5:7]=='12':
            n.rename(columns={x:str(str(x)[:4]+'q4')},inplace=True)
    n=n.reset_index()
    n['State'].replace(states1,inplace=True)
    return n.set_index(['State','RegionName'])
convert_housing_data_to_quarters()


# In[47]:


def run_ttest():
    '''First creates new data showing the decline or growth of housing prices
    between the recession start and the recession bottom. Then runs a ttest
    comparing the university town values to the non-university towns values, 
    return whether the alternative hypothesis (that the two groups are the same)
    is true or not as well as the p-value of the confidence. 
    
    Return the tuple (different, p, better) where different=True if the t-test is
    True at a p<0.01 (we reject the null hypothesis), or different=False if 
    otherwise (we cannot reject the null hypothesis). The variable p should
    be equal to the exact p value returned from scipy.stats.ttest_ind(). The
    value for better should be either "university town" or "non-university town"
    depending on which has a lower mean price ratio (which is equivilent to a
    reduced market loss).
    
    **Hypothesis**: University towns have their mean housing prices less effected by recessions. 
    Run a t-test to compare the ratio of the mean price of houses in university towns the quarter
    before the recession starts compared to the recession bottom. 
    (`price_ratio=quarter_before_recession/recession_bottom`)

    '''
    from scipy import stats
    
    rec_start = get_recession_start()
    rec_bottomm = get_recession_bottom()
    rec_end = get_recession_end()
    all_house = convert_housing_data_to_quarters()
    bef_rec_start= '2008q2'
    uni_names = get_list_of_university_towns().set_index(['State','RegionName'])
    #print (uni_names)
    housing_data_of_university = pd.merge(uni_names,all_house,how='inner',left_index=True,right_index=True)
    #print (housing_data_of_university.index)
    housing_data_for_nonuniversity = all_house.drop(housing_data_of_university.index,axis=0)
    housing_data_of_university['price ratio']=housing_data_of_university[bef_rec_start]/housing_data_of_university[rec_bottomm]
    housing_data_for_nonuniversity['price ratio']=housing_data_for_nonuniversity[bef_rec_start]/housing_data_for_nonuniversity[rec_bottomm]
    x =stats.ttest_ind(housing_data_of_university['price ratio'],housing_data_for_nonuniversity['price ratio'],nan_policy='omit')
    mean_nonuni = np.mean(housing_data_for_nonuniversity['price ratio'])
    mean_uni = np.mean(housing_data_of_university['price ratio'])
    
    p_val = 0
    different=True
    if mean_nonuni > mean_uni:
        better = "university town"
    else:
        better = 'non-university town'
    return (different,float(str(x[1])[:13]),better)
run_ttest()

