#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><ul class="toc-item"><li><span><a href="#analysis" data-toc-modified-id="analysis-0.1">analysis</a></span></li><li><span><a href="#analysis" data-toc-modified-id="analysis-0.2">analysis</a></span></li></ul></li><li><span><a href="#1-dataanalysis" data-toc-modified-id="1-dataanalysis-1">1 dataanalysis</a></span><ul class="toc-item"><li><span><a href="#1.1-data" data-toc-modified-id="1.1-data-1.1">1.1 data</a></span><ul class="toc-item"><li><span><a href="#" data-toc-modified-id="-1.1.1"></a></span></li></ul></li><li><span><a href="#1.2-Data Cleaning" data-toc-modified-id="1.2-Data Cleaning-1.2">1.2 Data Cleaning</a></span><ul class="toc-item"><li><span><a href="#1.2.1-variable" data-toc-modified-id="1.2.1-variable-1.2.1">1.2.1 variable</a></span></li></ul></li></ul></li><li><span><a href="#2-variableanalysis" data-toc-modified-id="2-variableanalysis-2">2 variableanalysis</a></span><ul class="toc-item"><li><span><a href="#2.1-sample0、1" data-toc-modified-id="2.1-sample0、1-2.1">2.1 sample0、1</a></span></li><li><span><a href="#2.2-" data-toc-modified-id="2.2--2.2">2.2 </a></span><ul class="toc-item"><li><span><a href="#data0 and 1variable，analysisvariableflagDistribution：" data-toc-modified-id="data0 and 1variable，analysisvariableflagDistribution：-2.2.1">data0 and 1variable，analysisvariableflagDistribution：</a></span></li></ul></li><li><span><a href="#2.3-visualization" data-toc-modified-id="2.3-visualization-2.3">2.3 visualization</a></span></li></ul></li><li><span><a href="#3-related  and visualization" data-toc-modified-id="3-related  and visualization-3">3 related  and visualization</a></span></li><li><span><a href="#4-regressionmodel and evaluation" data-toc-modified-id="4-regressionmodel and evaluation-4">4 regressionmodel and evaluation</a></span><ul class="toc-item"><li><span><a href="#4.1-model" data-toc-modified-id="4.1-model-4.1">4.1 model</a></span><ul class="toc-item"><li><span><a href="#4.1.1-training set and test set" data-toc-modified-id="4.1.1-training set and test set-4.1.1">4.1.1 training set and test set</a></span></li><li><span><a href="#4.1.2-viewmodelresult" data-toc-modified-id="4.1.2-viewmodelresult-4.1.2">4.1.2 viewmodelresult</a></span></li></ul></li><li><span><a href="#4.2-Model Evaluation" data-toc-modified-id="4.2-Model Evaluation-4.2">4.2 Model Evaluation</a></span><ul class="toc-item"><li><span><a href="#4.2.1-evaluation：calculateAccuracy" data-toc-modified-id="4.2.1-evaluation：calculateAccuracy-4.2.1">4.2.1 evaluation：calculateAccuracy</a></span><ul class="toc-item"><li><span><a href="#comparetraining set and test setaccuracy，info:" data-toc-modified-id="comparetraining set and test setaccuracy，info:-4.2.1.1">comparetraining set and test setaccuracy，info:</a></span></li></ul></li><li><span><a href="#4.2.2-evaluation：ROC and AUC" data-toc-modified-id="4.2.2-evaluation：ROC and AUC-4.2.2">4.2.2 evaluation：ROC and AUC</a></span></li></ul></li><li><span><a href="#4.3-model" data-toc-modified-id="4.3-model-4.3">4.3 model</a></span></li></ul></li><li><span><a href="#5-" data-toc-modified-id="5--5">5 </a></span><ul class="toc-item"><li><span><a href="#5.1-useranalysis" data-toc-modified-id="5.1-useranalysis-5.1">5.1 useranalysis</a></span></li><li><span><a href="#5.2-Couponusing analysis---user" data-toc-modified-id="5.2-Couponusing analysis---user-5.2">5.2 Couponusing analysis - user</a></span></li><li><span><a href="#5.3-" data-toc-modified-id="5.3--5.3">5.3 </a></span></li></ul></li></ul></div>

# ## analysis
# “Tmall”（：Tmail，，Tmall），，B2C(Business-to-Consumer, )。、， and ，100%，7days，and minute

# ## analysis
# based on userdataand data
# - using Pythonclassificationmodel，regression
# - predictionusing Coupon

# # 1 dataanalysis

# ## 1.1 data

# ### 
# - ID	recordencoding
# 
# - age	year
# 
# - job	
# 
# - marital	
# 
# - default	
# 
# - returned	
# 
# - loan	using 
# 
# - coupon_used_in_last6_month	monthusing CouponCount
# 
# - coupon_used_in_last_month	monthusing CouponCount
# 
# - coupon_ind	using Coupon

# In[1]:


#import and data
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')

coupon = pd.read_csv('tianmao.csv')
coupon.head()


# In[2]:


#viewdata
coupon.shape


# In[3]:


#viewdatamissing values
coupon.info()


# viewdata，missing values

# ## 1.2 Data Cleaning

# ### 1.2.1 variable

# In[4]:


#variablevariable，analysis
#，analysis，processingdefault, returned, loanvariable，job, marital 
#default、returned、loanvariablevariableprocessingget_dummies()。
coupon1 = coupon[['default','returned','loan']]
coupon1 = pd.get_dummies(coupon1)
coupon1.head()


# In[5]:


#processing and 
coupon = pd.concat([coupon, coupon1], axis = 1)
coupon.head()


# In[6]:


#containsinfo and infodata
coupon.drop(['ID', 'default', 'default_no', 'returned', 'returned_no', 'loan', 'loan_no'], axis = 1, inplace = True)

#coupon_indflag，analysis
coupon = coupon.rename(columns = {'coupon_ind' : 'flag'})
coupon.info()


# # 2 variableanalysis

# ## 2.1 sample0、1

# In[7]:


#classificationmodel，sample(flag)0,1
coupon['flag'].value_counts(1)


# - classification，0、1Share，0.05，modelprediction
# - dataset0、1Share0.05， therefore Distribution

# ## 2.2 

# In[8]:


#customerusing couponclassification
summary = coupon.groupby(['flag'])
#various Share
summary.mean()


# ### data0 and 1variable，analysisvariableflagDistribution：
# - coupon_used_in_last_month00.26，10.53，descriptionmonthusing couponcustomer，using coupon
# - default_yes and loan_yes0hour1hour，description and customertimeusing coupon
# - age0 and 1respectively40.8 and 41.8，，descriptionyearminute

# ## 2.3 visualization

# In[9]:


#returned_yesflagDistribution
sns.countplot(y = 'returned_yes', hue = 'flag', data = coupon)


# - customer，customerusing coupon

# In[10]:


#maritalflagDistribution
sns.countplot(y = 'marital', hue = 'flag', data = coupon)


# - customerusing coupon and customerusing coupon
# - using couponusing coupon
# - using couponusing coupon

# In[11]:


#jobflagDistribution
sns.countplot(y = 'job', hue = 'flag', data = coupon, order = coupon['job'].value_counts().index)


# - job titlemanagement, technician, blue-collarcustomerusing coupon

# In[12]:


#ageflagDistribution
sns.distplot(coupon['age'])


# In[13]:


#viewagedataDistribution
coupon['age'].describe()


# - data18 - 95customerusing coupon，using coupon40
# - age > 60，dataDistribution，need to minutedataanalysis

# In[15]:


#yearminute，yearusing coupon
age60 = coupon[coupon['age'] < 60]
bins = [0, 20, 40, 60]
labels = ['<20','<40','<60']
age60['age_new'] = pd.cut(age60.age, bins, right=False,labels = labels)
age60.groupby(['age_new'])['age'].describe()


# In[16]:


age60['age_new'].describe()


# In[17]:


#age60['age_new']，data
plt.figure(figsize=[9,7])
age60['age_new'].value_counts().plot.pie()
plt.show()


# - 20 - 40using coupon
# - 18，32，48respectivelyyearusing couponyearmean

# # 3 related  and visualization

# In[18]:


#flagvariable，variable
coupon.corr()[['flag']].sort_values('flag', ascending = False)


# In[19]:


sns.heatmap(coupon.corr(), cmap = 'Blues')


# - flagcoupon_used_in_last_month, agerelated 
# - flagcoupon_used_in_last6_month, returned_yesrelated 
# - variableflagrelated ，analysis， therefore 

# # 4 regressionmodel and evaluation

# ## 4.1 model
# 

# ### 4.1.1 training set and test set

# In[20]:


#variablex and variabley
x = coupon[['coupon_used_in_last_month', 'returned_yes', 'loan_yes']]
y = coupon['flag']


# In[21]:


#sklearn，training set and test set
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 100) #training set and test set70/30

#sklearnregression
from sklearn import linear_model
lr = linear_model.LogisticRegression()

#
lr.fit(x_train, y_train)


# ### 4.1.2 viewmodelresult

# In[22]:


#view
lr.coef_


# - coupon_used_in_last_month01hour，using couponusing coupone0.38，customer1.46
# - returned_yes10hour，using couponusing couponcustomer0.38
# - loan_yes10hour，using couponusing couponcustomer0.57
# - ，monthusing couponcustomer、customer and using coupon。

# In[23]:


#view
lr.intercept_


# ## 4.2 Model Evaluation

# ### 4.2.1 evaluation：calculateAccuracy

# In[24]:


#through training set and test setvariablex，respectivelycalculateprediction
y_pred_train = lr.predict(x_train)
y_pred_test = lr.predict(x_test)


# In[25]:


#training setConfusion Matrix
from sklearn import metrics
metrics.confusion_matrix(y_train, y_pred_train)


# In[26]:


#viewtraining setaccuracy
metrics.accuracy_score(y_train, y_pred_train)


# In[27]:


#test setConfusion Matrix
metrics.confusion_matrix(y_test, y_pred_test)


# In[28]:


#viewtest setaccuracy
metrics.accuracy_score(y_test, y_pred_test)


# #### comparetraining set and test setaccuracy，info:
# - modeltrain and test。training settest setaccuracy，model
# -  and ，need to 。train and test，modelaccuracy

# ### 4.2.2 evaluation：ROC and AUC

# In[29]:


#using aucevaluationmodel
from sklearn.metrics import roc_curve, auc
fpr,tpr,threshold = roc_curve(y_train, y_pred_train)
roc_auc = auc(fpr,tpr)

print(roc_auc)


# modelminute0.7 - 0.8，modelneed to 

# ## 4.3 model

# In[30]:


#variablereturned_yes
x = coupon[['coupon_used_in_last_month', 'returned_yes', 'loan_yes', 'coupon_used_in_last6_month', 'default_yes', 'age']]
y = coupon['flag']


# In[31]:


#sklearn，training set and test set
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 100) #training set and test set70/30

#sklearnregression
from sklearn import linear_model
lr = linear_model.LogisticRegression()

#
lr.fit(x_train, y_train)


# In[32]:


lr.coef_


# In[33]:


#using aucevaluationmodel
from sklearn.metrics import roc_curve, auc
fpr,tpr,threshold = roc_curve(y_train, y_pred_train)
roc_auc = auc(fpr,tpr)

print(roc_auc)


# - coupon_used_in_last_month, age and flagrelated ，variableflagrelated 
# - modelAUCminute，descriptioncouponusing 

# # 5 

# ## 5.1 useranalysis

# - data18 - 95customerusing coupon，using coupon40
# - 20 - 40using coupon
# - 18，32，48respectivelyyearusing couponyearmean

# ## 5.2 Couponusing analysis - user

# - coupon_used_in_last_month00.26，10.53，descriptionmonthusing couponcustomer，using coupon
# - default_yes and loan_yes0hour1hour，description and customertimeusing coupon
# 
# 
# - customer，customerusing coupon
# - customerusing coupon and customerusing coupon
# - job titlemanagement, technician, blue-collarcustomerusing coupon
# 
# 
# - flagcoupon_used_in_last_month, agerelated 
# - flagcoupon_used_in_last6_month, returned_yesrelated 
# - variableflagCorrelation

# ## 5.3 

# - TmallCouponusing 
# - 20 - 60customer，comparecustomer，modelmodel，customer
# - monthCouponcustomerusing Coupon，modelmodel，
# - customer、customer、 and usercustomermodelcustomermodel，、 and ，customer
# - APPCoupon，banner、；APP、Coupon，customerusing Coupon
