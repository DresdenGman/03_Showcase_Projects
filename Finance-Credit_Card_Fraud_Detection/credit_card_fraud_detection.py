#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Credit CardTransactionFraud" data-toc-modified-id="Credit CardTransactionFraud-1">Credit CardTransactionFraud</a></span></li><li><span><a href="#EDA-Data Exploration" data-toc-modified-id="EDA-Data Exploration-2">EDA Data Exploration</a></span><ul class="toc-item"><li><ul class="toc-item"><li><ul class="toc-item"><li><span><a href="#missing values" data-toc-modified-id="missing values-2.0.0.1">missing values</a></span></li></ul></li><li><span><a href="#TransactionDistribution" data-toc-modified-id="TransactionDistribution-2.0.1">TransactionDistribution</a></span></li></ul></li><li><span><a href="#TransactiontimeDistribution" data-toc-modified-id="TransactiontimeDistribution-2.1">TransactiontimeDistribution</a></span></li><li><span><a href="#TransactionAmountDistribution" data-toc-modified-id="TransactionAmountDistribution-2.2">TransactionAmountDistribution</a></span></li><li><span><a href="#TransactiontimeAmountDistribution" data-toc-modified-id="TransactiontimeAmountDistribution-2.3">TransactiontimeAmountDistribution</a></span></li></ul></li><li><span><a href="#Data Preprocessing" data-toc-modified-id="Data Preprocessing-3">Data Preprocessing</a></span><ul class="toc-item"><li><span><a href="#data（）" data-toc-modified-id="data（）-3.1">data（）</a></span></li><li><span><a href="#sample" data-toc-modified-id="sample-3.2">sample</a></span><ul class="toc-item"><li><span><a href="#sample" data-toc-modified-id="sample-3.2.1">sample</a></span></li></ul></li><li><span><a href="#3sample" data-toc-modified-id="3sample-3.3">3sample</a></span><ul class="toc-item"><li><span><a href="#Step-1.-training settest setminute" data-toc-modified-id="Step-1.-training settest setminute-3.3.1">Step 1. training settest setminute</a></span></li><li><span><a href="#Step-2.-trainingdatasample" data-toc-modified-id="Step-2.-trainingdatasample-3.3.2">Step 2. trainingdatasample</a></span></li></ul></li></ul></li><li><span><a href="#ModelingModel Evaluation" data-toc-modified-id="ModelingModel Evaluation-4">ModelingModel Evaluation</a></span><ul class="toc-item"><li><span><a href="#LRModeling" data-toc-modified-id="LRModeling-4.1">LRModeling</a></span><ul class="toc-item"><li><span><a href="#training set-vs-training set-Modeling" data-toc-modified-id="training set-vs-training set-Modeling-4.1.1">training set vs training set Modeling</a></span></li><li><span><a href="#datasetparameterModeling" data-toc-modified-id="datasetparameterModeling-4.1.2">datasetparameterModeling</a></span></li><li><span><a href="#Confusion Matrix" data-toc-modified-id="Confusion Matrix-4.1.3">Confusion Matrix</a></span></li></ul></li><li><span><a href="#Modeling" data-toc-modified-id="Modeling-4.2">Modeling</a></span><ul class="toc-item"><li><span><a href="#" data-toc-modified-id="-4.2.1"></a></span></li></ul></li></ul></li><li><span><a href="#visualizationmodel" data-toc-modified-id="visualizationmodel-5">visualizationmodel</a></span><ul class="toc-item"><li><span><a href="#classification" data-toc-modified-id="classification-5.1">classification</a></span><ul class="toc-item"><li><span><a href="#ROC" data-toc-modified-id="ROC-5.1.1">ROC</a></span></li></ul></li></ul></li></ul></div>

# # Credit CardTransactionFraud
# 
# using datasetPCAprocessingdata，recordTransactionrecord。
# v1-v28PCA28minutevariable，processing， so 28featurespecific ，analysis。

# In[1]:


# using plotly，
# pip uninstall plotly

# pip install plotly==4.14.3  -i https://pypi.tuna.tsinghua.edu.cn/simple  --trusted-host pypi.tuna.tsinghua.edu.cn


# In[1]:


import numpy as np
import pandas as pd
import time

import plotly.express as px
import matplotlib.pyplot as plt


# In[2]:


import warnings
warnings.filterwarnings("ignore")


# # EDA Data Exploration

# In[3]:


data = pd.read_csv('./creditcardfraud.csv')
data.shape


# In[4]:


data.head(3)


# #### missing values

# In[5]:


data.isnull().values.sum()


# ### TransactionDistribution

# In[6]:


tran_class = data.Class.value_counts().reset_index()
print(tran_class.columns)
tran_class = tran_class.rename(columns={'Class':'Transaction', 'count':''})
tran_class['Transaction'] = tran_class['Transaction'].map({0:'',1:'Fraud'})
tran_class['Share'] = tran_class['']/tran_class[''].sum()


# 
tran_class_fig = px.bar(tran_class, y='Transaction', x='', height = 300, width = 800, 
    text=[':{}<br>Share:{:.2f}%'.format(a,100*b) for a,b in zip(tran_class[''],tran_class['Share'])],
    orientation='h'
    )
tran_class_fig.update_layout(title={'text':'TransactionDistribution', 'y':0.97, 'x':0.5, 'xanchor':'center','yanchor':'top'})


# ，Transactionrecord284315，Transactionrecord492，Transactionrecord0.17%。

# In[7]:


all_normal = data[data['Class'] == 0] # Transaction
all_fraud = data[data['Class'] == 1]  # FraudTransaction


# ## TransactiontimeDistribution

# 

# In[17]:


def draw_hist(dataframe, x_name, x_rename, title, color, nbins_count = 100, height = 400, width = 900, log_y=False):
    fig = px.histogram(dataframe, x=x_name, nbins=nbins_count, labels={x_name:x_rename}, 
                    opacity=0.9, color_discrete_sequence=[color], # color of histogram bars
                    height= height, width = width, log_y = log_y,
                    # range_x = [dataframe[x_name].min(),dataframe[x_name].max()],
                    # marginal='box', # ：
    )
    fig.update_layout(title={'text':title, 'y':0.97, 'x':0.5, 'xanchor':'center','yanchor':'top'})
    fig.show()


# In[18]:


draw_hist(all_normal, 'Time', 'Transactiontime', 'TransactiontimeDistribution', 'rgb(156,219,165)')
draw_hist(all_fraud, 'Time', 'Transactiontime', 'FraudTransactiontimeDistribution', 'rgb(214,96,77)')


# `y`Logvisualization。

# In[19]:


draw_hist(all_normal, 'Time', 'Transactiontime', 'TransactiontimeDistribution', 'rgb(156,219,165)', log_y = True)
draw_hist(all_fraud, 'Time', 'Transactiontime', 'FraudTransactiontimeDistribution', 'rgb(214,96,77)', log_y = True)


# TransactionrecordDistribution，TransactionDistribution。TransactionTransactiontimeFraudTransaction， so TransactionFraudTransaction。

# ## TransactionAmountDistribution

# In[20]:


normal_amount_box = px.box(all_normal, x='Amount', width = 700, height = 200)
normal_amount_box.update_layout(title={'text':'TransactionAmount', 'y':0.97, 'x':0.5, 'xanchor':'center','yanchor':'top'})
normal_amount_box.show()
fraud_amount_box = px.box(all_fraud, x='Amount', width = 700, height = 200)
fraud_amount_box.update_layout(title={'text':'FraudTransactionAmount', 'y':0.97, 'x':0.5, 'xanchor':'center','yanchor':'top'})
fraud_amount_box.show()


# In[21]:


draw_hist(all_normal, 'Amount', 'TransactionAmount', 'TransactionAmountDistribution', 'rgb(156,219,165)', nbins_count=30, height = 300, width = 700)
draw_hist(all_fraud, 'Amount', 'TransactionAmount', 'FraudTransactionAmountDistribution', 'rgb(214,96,77)', nbins_count=30, height = 300, width = 700)


# FraudTransaction and TransactionAmountDistribution，FraudTransactionAmount`$2125.87`。75%FraudTransactionrecordAmount`$105.89`，Transaction。

# ## TransactiontimeAmountDistribution

# In[22]:


normal_time_amount_fig = px.scatter(all_normal, x='Time', y = 'Amount', height = 380, width = 700)
normal_time_amount_fig.update_layout(title={'text':'TransactiontimeAmountDistribution', 'y':0.97, 'x':0.5, 'xanchor':'center','yanchor':'top'})
# normal_time_amount_fig.show()

fraud_time_amount_fig = px.scatter(all_fraud, x='Time', y = 'Amount', height = 380, width = 700)
fraud_time_amount_fig.update_layout(title={'text':'FraudTransactiontimeAmountDistribution', 'y':0.97, 'x':0.5, 'xanchor':'center','yanchor':'top'})
fraud_time_amount_fig.show()


# # Data preprocessing
# **Transactionrecord0.17%，Transactionrecord99.83%**。
# minuteTransactionFraud。Negative，processingusing Modelingmodeloverfitting。
# 
# ## data（）
# 
# dataset`V1``V28`PCAprocessing28minute，Amounttime。
# `Amount` and `Time`featurePCAprocessing28（`V1``V28`）feature，****processing，different result。
# 
# - ？
#     - StandardScaler
#         - ：$(x-mean)/std_dev$datastd
#         - save and using 
#     - RobustScaler
#         - data，data and ，using `RobustScaler`data
#         - data and data

# In[8]:


from sklearn.preprocessing import StandardScaler, RobustScaler

# std_scaler = StandardScaler()
rub_scaler = RobustScaler() # 

# reshape(-1,1) data['Amount']，np.array
data['scaledAmount'] = rub_scaler.fit_transform(data['Amount'].values.reshape(-1,1))
data['scaledTime'] = rub_scaler.fit_transform(data['Time'].values.reshape(-1,1))

print('Amount：',data['Amount'].values.reshape(-1,1))
print('Amount：',rub_scaler.fit_transform(data['Amount'].values.reshape(-1,1)))
print('Time：',data['Time'].values.reshape(-1,1))
print('Time：',rub_scaler.fit_transform(data['Time'].values.reshape(-1,1)))


# dataset：need to using data
new_data = data.drop(['Time','Amount'], axis = 1)
new_data.head()


# 
# ## sample
# 
# sampleData Preprocessing，sampleand sample，。
# 
# ### sample
# 
# samplemodelevaluation，overfittingresult。 so need to Negativetraining。，datasetsample“”（majority class），sample“”（minority class）。
# 
# sampleprocessing[[1]](https://blog.csdn.net/sinat_26917383/article/details/75890859)：
# ![image.png](attachment:image.png)
# 
# 
# 
# ********，（**Undersampling**,），（**Oversampling**，）。。 because ，minute， so sample，overfitting；info。
# 
#  so **info**，**EasyEnsemble**，**BalanceCascade******。
# 
# ****，through **data**based on datasample，**SMOTE**；
# through ****，。
# 
# ，，Negative，****（Outlier Detection）**classification**（One Class Learning）。One-class SVM。
# 
# processingdata，hoursamplemodel e.g., XGBoost 。
# 
# ** so sample，？**[[1]](https://blog.csdn.net/sinat_26917383/article/details/75890859)
# >- **Negative**, using **data**
# - **Negative，Positive**, **classification**
# - **Negative**, ********
# 
# 
# 

# ## 3sample
# 3different sample，PositiveShare0.17%，using sample，modeltraining， so 。
# - ：sample。：sample，classificationoverfitting。
# - SMOTE：based on Distributionsample。：sample，modelinfooverfitting。
# - ：，Distribution and overfitting。 e.g., SMOTE+Tomek，SMOTE+KNN。： and 。

# ### Step 1. training settest setminute
# 
# minute:
# - `train_test_split`：training settest set，labelDistribution，sample
# - [minute](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedShuffleSplit.html)`StratifiedShuffleSplit`：trainingtest setdifferent labelDistributiondatalabelDistribution，sample
# 
# minute `training set：test set = 7：3`

# In[9]:


from sklearn.model_selection import train_test_split       # 
from sklearn.model_selection import StratifiedShuffleSplit # minute


# minutefeaturedata  and labeldata
X = new_data.iloc[:, new_data.columns != 'Class'] # featuredata
y = new_data.iloc[:, new_data.columns == 'Class'] # label
print('X shape:',X.shape, '\ny shape:',y.shape)


# ：
# X = np.array(new_data.iloc[:, new_data.columns != 'Class']) # featuredata
# y = np.array(new_data.iloc[:, new_data.columns == 'Class']) # label
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1234)

# ：minute
#  cross-validatorminute10
sss = StratifiedShuffleSplit(n_splits=10,test_size=0.3,train_size=None, random_state=12345)


for train_index, test_index in sss.split(X,y):
    print('Train:', train_index, 'Test:', test_index)
    original_Xtrain, original_Xtest = X.iloc[train_index], X.iloc[test_index]
    original_ytrain, original_ytest = y.iloc[train_index], y.iloc[test_index]


# training settest set
original_X_train = np.array(original_Xtrain)
original_X_test = np.array(original_Xtest)
original_y_train = np.array(original_ytrain)
original_y_test = np.array(original_ytest)


# In[10]:


# viewtraining set and test setlabelDistribution
train_unique_label, train_label_count = np.unique(original_y_train, return_counts=True)
test_unique_label, test_label_count = np.unique(original_y_test, return_counts=True)

train_label_rate = train_label_count / len(original_ytrain)
test_label_rate = test_label_count / len(original_ytest)


print("\ntraining setlabel{}:{}, label{}:{}".format(train_unique_label[0],train_label_count[0], train_unique_label[1],train_label_count[1] ))
print("\ntraining setlabelDistribution：")
for label,rate in zip(train_unique_label, train_label_rate):
    print('label{} Share:{:.2f}%'.format(label,100*rate))

print("\ntest setlabel{}:{}, label{}:{}".format(test_unique_label[0],test_label_count[0], test_unique_label[1],test_label_count[1] ))
print("\ntest setlabelDistribution：")
for label,rate in zip(test_unique_label,test_label_rate):
    print('label{} Share:{:.2f}%'.format(label,100*rate))


# ### Step 2. trainingdatasample

# In[ ]:


#pip uninstall imbalanced-learn


# In[ ]:


#  imblearn 0.7.0
get_ipython().system('pip install imbalanced-learn==0.7.0 -i https://pypi.tuna.tsinghua.edu.cn/simple  --trusted-host pypi.tuna.tsinghua.edu.cn')


# In[11]:


from imblearn.over_sampling import RandomOverSampler, SMOTE
from imblearn.combine import SMOTETomek


# In[15]:


ros = RandomOverSampler(random_state=0)
sos = SMOTE(random_state = 0)
kos = SMOTETomek(random_state = 0)

# hour
X_ros, y_ros = ros.fit_sample(original_X_train, original_y_train)
X_sos, y_sos = sos.fit_sample(original_X_train, original_y_train)
X_kos, y_kos = kos.fit_sample(original_X_train, original_y_train)

print('ros:{}, sos:{}, kos:{}'.format(len(y_ros), len(y_sos), len(y_kos)))


# viewNegativeCount

# In[17]:


print('training setPositive，training set:{} \ntraining set:{}, SMOTEtraining set:{}, training set:{}      '.format(original_y_train.sum(), y_ros.sum(), y_sos.sum(), y_kos.sum()))
print('training setShare{:.2f}%, through 3training setNegativeShare：{:.0f}%'.format(100*original_y_train.sum()/len(original_y_train), 100*y_ros.sum()/len(y_ros)))


# # ModelingModel Evaluation

# In[18]:


from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import confusion_matrix, roc_curve, auc, recall_score, classification_report


# ## LRModeling
# ### training set vs training set Modeling
# - using model`f1-score`， because （FraudTransaction），houraccuracy。
# 
# Tip:CV【day】view

# In[19]:


lr = LogisticRegression(max_iter = 500)

# parameter，overfitting
paramaters = {'C':[0.01,0.1,1,5,10,100]} 
# 10 folds, n jobs run in parallel
lr_cv1 = GridSearchCV(lr, param_grid = paramaters, cv=10, n_jobs=-1, verbose=5, scoring='f1')  # n_jobs=-1


# In[20]:


data = [[original_X_train, original_y_train],
        [X_ros, y_ros],
        [X_sos, y_sos],
        [X_kos, y_kos]]


for features, labels in data:
    lr_cv1.fit(features, labels)
    predict_test = lr_cv1.predict(original_X_test)
    print('AUC:{} Recall:{} Precision:{}'.format(
        metrics.roc_auc_score(original_y_test, predict_test),
        metrics.recall_score(original_y_test, predict_test),
        metrics.precision_score(original_y_test, predict_test)
    ))


# In[21]:


print('parameter：', lr_cv1.best_params_)


# We can see training settrainingmodelprecision:90%,recall(66.9%)。indicatespredictionsample90%Positive，Positive66.9%model。
# 
# processingtraining set and ，precision，6%。modelrecall and precision，model。
# 
# Positive and Negativetrainingmodel。

# ### datasetparameterModeling

# In[24]:


lr = LogisticRegression(max_iter = 500)
param_grid= {'C':[0.01,0.1,1,5,10,100], 
            'class_weight':[{0:1,1:3}, {0:1,1:5},{0:1,1:10}, {0:1,1:15}]
            } 

lr_cv2 = GridSearchCV(lr, param_grid = param_grid, cv=10, n_jobs=-1, verbose=5, scoring='f1')  # n_jobs=-1

# 
lr_cv2.fit(original_X_train, original_y_train)
predict2 = lr_cv2.predict(original_X_test)

print('AUC:{:.3f} Recall:{:.3f} Precision:{:.3f}'.format(
        metrics.roc_auc_score(original_y_test, predict2),
        metrics.recall_score(original_y_test, predict2),
        metrics.precision_score(original_y_test, predict2)
    ))


# ，modelrecallprecision。

# In[26]:


print('modelparameter：',lr_cv2.best_params_)


# ### Confusion Matrix

# In[27]:


import itertools

def plot_confusion_matrix(cm, classes, title='Confusion matrix', cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=0)
    plt.yticks(tick_marks, classes)

    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, cm[i, j],
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    # plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')


# In[28]:


# training setprediction
y_train_pre = lr_cv2.predict(original_X_train)

# training setConfusion Matrix
cnf_matrix_train = confusion_matrix(original_y_train, y_train_pre)

print("training setlabelCount：\nlabel{}:{}, label{}:{}".format(train_unique_label[0],train_label_count[0], train_unique_label[1],train_label_count[1] ))
print("Recall: {:.2f}%".format(100*cnf_matrix_train[1,1]/(cnf_matrix_train[1,0]+cnf_matrix_train[1,1])))

class_names = [0,1]
plt.figure()
plot_confusion_matrix(cnf_matrix_train , classes=class_names, title='Confusion matrix')
plt.show()


# In[29]:


# test setprediction
y_pre = lr_cv2.predict(original_X_test)

# test setConfusion Matrix
cnf_matrix = confusion_matrix(original_y_test, y_pre)

print("test setlabelCount：\nlabel{}:{}, label{}:{}".format(test_unique_label[0],test_label_count[0], test_unique_label[1],test_label_count[1] ))
print("test setRecall: {:.2f}%".format(100*cnf_matrix[1,1]/(cnf_matrix[1,0]+cnf_matrix[1,1])))

class_names = [0,1]
plt.figure()
plot_confusion_matrix(cnf_matrix , classes=class_names, title='Confusion matrix')
plt.show()


# ## Modeling
# classification and regression。feature，trainingdatasetminute，minute，classification。
# different feature， so using featuredatatraining。

# In[30]:


from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz


# In[ ]:


tree_params = {
    "criterion": ["gini", "entropy"], # ：、
    "max_depth": list(range(2, 4, 1)), #  2、3
    "min_samples_leaf": list(range(5, 7, 1)) # need to 
}
dt_cv = GridSearchCV(DecisionTreeClassifier(), tree_params, scoring='f1')
dt_cv.fit(original_X_train, original_y_train.ravel())


# In[ ]:


print('modelparameter：',dt_cv.best_params_)


# In[ ]:


predict3 = dt_cv.predict(original_X_test)
print('AUC:{:.3f} Recall:{:.3f} Precision:{:.3f}'.format(
        metrics.roc_auc_score(original_y_test, predict3),
        metrics.recall_score(original_y_test, predict3),
        metrics.precision_score(original_y_test, predict3)
    ))


# ### 

# In[30]:


get_ipython().system('pip install pydotplus==2.0.2 -i https://pypi.tuna.tsinghua.edu.cn/simple  --trusted-host pypi.tuna.tsinghua.edu.cn')


# In[42]:


# based on parameterclassification
dt_clf = DecisionTreeClassifier(criterion='entropy', max_depth=3, min_samples_leaf=5) 
dt_clf.fit(original_X_train, original_y_train.ravel())


# In[55]:


import pydotplus
from IPython.display import display, Image

dot_data = export_graphviz(dt_clf,  # model
                            out_file=None, # file
                            feature_names=X.columns, # feature
                            class_names = ['normal', 'fraud'], # label，
                            filled = True, # 
                            rounded =True  # 
                        )
                               
graph = pydotplus.graph_from_dot_data(dot_data)
display(Image(graph.create_png()))


# # visualizationmodel

# ## classification
# ### ROC
# FPR（False Positive Rate，）, TPR(True Positive Rate，)respectivelyROC
# 
# - ****（）= **Recall**（Recall）：
# 
# 	positive，classificationPrediction Resultspositive。（sensitivity）Recall（recall），classificationpositive****。
# 
# 	~$TPR = \frac{TP}{TP+FN}~$ 
# 
# - **** = ****（fallout）:
# 
# 	negative，classificationPrediction Resultspositive。（fallout）。
# 
# 	~$FPR = \frac{FP}{FP+TN}~$  

# In[56]:


# regression
fpr, tpr, thresholds = roc_curve(original_y_test, predict2)
roc_auc = auc(fpr, tpr)
print('Logistic Regression AUC：{:.2f}%'.format(100*roc_auc))

# 
dt_fpr, dt_tpr, dt_thresholds = roc_curve(original_y_test, predict3)
dt_roc_auc = auc(dt_fpr, dt_tpr)
print('Decision Tree AUC：{:.2f}%'.format(100*dt_roc_auc))

# Plot ROC

plt.title('Receiver Operating Characteristic')
plt.plot(fpr, tpr, 'b',label='Logistic Regression AUC = %0.3f'% roc_auc)
plt.plot(dt_fpr, dt_tpr, 'y', label='Decision Tress AUC = %0.3f'% dt_roc_auc)
plt.legend(loc='lower right') # legend
plt.plot([0,1],[0,1],'r--') # red, --
plt.xlim([-0.1,1.0])
plt.ylim([-0.1,1.01])
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.show()


# regressionclassificationROC，，AUC(Area Under Curve)`0.898``0.899`，descriptionmodel（`1`）。ROC（thresholds），。

# sampleprocessing，modelclassification，Fraudsampledata！datamodel，。
