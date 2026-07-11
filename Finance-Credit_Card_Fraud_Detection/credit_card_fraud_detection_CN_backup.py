#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#信用卡交易欺诈检测" data-toc-modified-id="信用卡交易欺诈检测-1">信用卡交易欺诈检测</a></span></li><li><span><a href="#EDA-数据探索" data-toc-modified-id="EDA-数据探索-2">EDA 数据探索</a></span><ul class="toc-item"><li><ul class="toc-item"><li><ul class="toc-item"><li><span><a href="#缺失值检查" data-toc-modified-id="缺失值检查-2.0.0.1">缺失值检查</a></span></li></ul></li><li><span><a href="#交易类别分布" data-toc-modified-id="交易类别分布-2.0.1">交易类别分布</a></span></li></ul></li><li><span><a href="#探索交易时间分布" data-toc-modified-id="探索交易时间分布-2.1">探索交易时间分布</a></span></li><li><span><a href="#探索交易金额分布" data-toc-modified-id="探索交易金额分布-2.2">探索交易金额分布</a></span></li><li><span><a href="#探索交易时间与金额之间的分布关系" data-toc-modified-id="探索交易时间与金额之间的分布关系-2.3">探索交易时间与金额之间的分布关系</a></span></li></ul></li><li><span><a href="#数据预处理" data-toc-modified-id="数据预处理-3">数据预处理</a></span><ul class="toc-item"><li><span><a href="#数据缩放（标准化）" data-toc-modified-id="数据缩放（标准化）-3.1">数据缩放（标准化）</a></span></li><li><span><a href="#平衡样本" data-toc-modified-id="平衡样本-3.2">平衡样本</a></span><ul class="toc-item"><li><span><a href="#不平衡样本" data-toc-modified-id="不平衡样本-3.2.1">不平衡样本</a></span></li></ul></li><li><span><a href="#3种方式平衡样本" data-toc-modified-id="3种方式平衡样本-3.3">3种方式平衡样本</a></span><ul class="toc-item"><li><span><a href="#Step-1.-训练集与测试集切分" data-toc-modified-id="Step-1.-训练集与测试集切分-3.3.1">Step 1. 训练集与测试集切分</a></span></li><li><span><a href="#Step-2.-对训练数据进行样本平衡" data-toc-modified-id="Step-2.-对训练数据进行样本平衡-3.3.2">Step 2. 对训练数据进行样本平衡</a></span></li></ul></li></ul></li><li><span><a href="#建模与模型评估" data-toc-modified-id="建模与模型评估-4">建模与模型评估</a></span><ul class="toc-item"><li><span><a href="#LR建模" data-toc-modified-id="LR建模-4.1">LR建模</a></span><ul class="toc-item"><li><span><a href="#原始训练集-vs-过采样训练集-建模效果" data-toc-modified-id="原始训练集-vs-过采样训练集-建模效果-4.1.1">原始训练集 vs 过采样训练集 建模效果</a></span></li><li><span><a href="#原始数据集调整类别权重参数后建模效果" data-toc-modified-id="原始数据集调整类别权重参数后建模效果-4.1.2">原始数据集调整类别权重参数后建模效果</a></span></li><li><span><a href="#绘制混淆矩阵" data-toc-modified-id="绘制混淆矩阵-4.1.3">绘制混淆矩阵</a></span></li></ul></li><li><span><a href="#决策树建模" data-toc-modified-id="决策树建模-4.2">决策树建模</a></span><ul class="toc-item"><li><span><a href="#绘制决策树" data-toc-modified-id="绘制决策树-4.2.1">绘制决策树</a></span></li></ul></li></ul></li><li><span><a href="#可视化模型效果" data-toc-modified-id="可视化模型效果-5">可视化模型效果</a></span><ul class="toc-item"><li><span><a href="#分类器效果对比" data-toc-modified-id="分类器效果对比-5.1">分类器效果对比</a></span><ul class="toc-item"><li><span><a href="#绘制ROC曲线" data-toc-modified-id="绘制ROC曲线-5.1.1">绘制ROC曲线</a></span></li></ul></li></ul></li></ul></div>

# # 信用卡交易欺诈检测
# 
# 该项目使用的数据集是脱敏过且经过PCA处理的数据，每行记录代表一条交易记录。
# v1-v28代表的是经过PCA降维获取到的28个主成成分变量，但是由于经过了脱敏处理，所以并不了解这个28个特征具体指代什么，如果可以了解到的话会更有助于分析。

# In[1]:


# 使用前卸载旧版本plotly，安装新版本
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


# # EDA 数据探索

# In[3]:


data = pd.read_csv('./creditcardfraud.csv')
data.shape


# In[4]:


data.head(3)


# #### 缺失值检查

# In[5]:


data.isnull().values.sum()


# ### 交易类别分布

# In[6]:


tran_class = data.Class.value_counts().reset_index()
print(tran_class.columns)
tran_class = tran_class.rename(columns={'Class':'交易类别', 'count':'频数'})
tran_class['交易类别'] = tran_class['交易类别'].map({0:'正常',1:'欺诈'})
tran_class['占比'] = tran_class['频数']/tran_class['频数'].sum()


# 绘制柱状图
tran_class_fig = px.bar(tran_class, y='交易类别', x='频数', height = 300, width = 800, 
    text=['频数:{}<br>占比:{:.2f}%'.format(a,100*b) for a,b in zip(tran_class['频数'],tran_class['占比'])],
    orientation='h'
    )
tran_class_fig.update_layout(title={'text':'交易类别分布', 'y':0.97, 'x':0.5, 'xanchor':'center','yanchor':'top'})


# 如图所示，正常交易记录有284315条，异常交易记录有492条，异常交易记录比率为0.17%。

# In[7]:


all_normal = data[data['Class'] == 0] # 正常交易
all_fraud = data[data['Class'] == 1]  # 欺诈交易


# ## 探索交易时间分布

# 自定义直方图绘制函数

# In[17]:


def draw_hist(dataframe, x_name, x_rename, title, color, nbins_count = 100, height = 400, width = 900, log_y=False):
    fig = px.histogram(dataframe, x=x_name, nbins=nbins_count, labels={x_name:x_rename}, 
                    opacity=0.9, color_discrete_sequence=[color], # color of histogram bars
                    height= height, width = width, log_y = log_y,
                    # range_x = [dataframe[x_name].min(),dataframe[x_name].max()],
                    # marginal='box', # 绘制辅助图：箱线图
    )
    fig.update_layout(title={'text':title, 'y':0.97, 'x':0.5, 'xanchor':'center','yanchor':'top'})
    fig.show()


# In[18]:


draw_hist(all_normal, 'Time', '交易时间', '正常交易时间分布', 'rgb(156,219,165)')
draw_hist(all_fraud, 'Time', '交易时间', '欺诈交易时间分布', 'rgb(214,96,77)')


# 对出现频次`y`取对数Log进行更直观的可视化。

# In[19]:


draw_hist(all_normal, 'Time', '交易时间', '正常交易时间分布', 'rgb(156,219,165)', log_y = True)
draw_hist(all_fraud, 'Time', '交易时间', '欺诈交易时间分布', 'rgb(214,96,77)', log_y = True)


# 显示正常交易记录呈周期性分布，而异常交易分布较平均。在正常交易的交易低频时间段更容易检测到欺诈交易，所以可以从交易周期的低频段入手欺诈交易的检测。

# ## 探索交易金额分布

# In[20]:


normal_amount_box = px.box(all_normal, x='Amount', width = 700, height = 200)
normal_amount_box.update_layout(title={'text':'正常交易金额箱线图', 'y':0.97, 'x':0.5, 'xanchor':'center','yanchor':'top'})
normal_amount_box.show()
fraud_amount_box = px.box(all_fraud, x='Amount', width = 700, height = 200)
fraud_amount_box.update_layout(title={'text':'欺诈交易金额箱线图', 'y':0.97, 'x':0.5, 'xanchor':'center','yanchor':'top'})
fraud_amount_box.show()


# In[21]:


draw_hist(all_normal, 'Amount', '交易金额', '正常交易金额分布', 'rgb(156,219,165)', nbins_count=30, height = 300, width = 700)
draw_hist(all_fraud, 'Amount', '交易金额', '欺诈交易金额分布', 'rgb(214,96,77)', nbins_count=30, height = 300, width = 700)


# 由上图直方图显示欺诈交易和正常交易的金额分布相差很大，欺诈交易最大金额仅为`$2125.87`。辅助箱线图显示75%的欺诈交易记录的金额都不高于`$105.89`，且集中于小额交易。

# ## 探索交易时间与金额之间的分布关系

# In[22]:


normal_time_amount_fig = px.scatter(all_normal, x='Time', y = 'Amount', height = 380, width = 700)
normal_time_amount_fig.update_layout(title={'text':'正常交易时间与金额的分布', 'y':0.97, 'x':0.5, 'xanchor':'center','yanchor':'top'})
# normal_time_amount_fig.show()

fraud_time_amount_fig = px.scatter(all_fraud, x='Time', y = 'Amount', height = 380, width = 700)
fraud_time_amount_fig.update_layout(title={'text':'欺诈交易时间与金额的分布', 'y':0.97, 'x':0.5, 'xanchor':'center','yanchor':'top'})
fraud_time_amount_fig.show()


# # 数据预处理
# **异常交易记录比率为0.17%，正常交易记录比率为99.83%**。
# 大部分交易都是非欺诈的。正负样本是高度不平衡的，如果不做平衡处理直接使用建模会导致模型出现过拟合的问题。
# 
# ## 数据缩放（标准化）
# 
# 数据集的`V1`至`V28`是已经经过PCA处理的28个主成成分，而金额与时间列还未进行相应的缩放。
# `Amount`列和`Time`特征值的取值范围相比于PCA处理过的其他28列（`V1`至`V28`）特征值取值范围相差很大，需统一标准即**标准化**处理，以此来消除内部构成不同造成的对结果的影响。
# 
# - 选择哪种缩放？
#     - StandardScaler
#         - 本质：$(x-mean)/std_dev$数据减去均值除以标准差
#         - 可以保存均值和方差供后续使用
#     - RobustScaler
#         - 这里的数据有离群点，对数据进行均差和方差的标准化效果不好，建议使用`RobustScaler`进行数据缩放
#         - 它对数据中心化和数据的缩放鲁棒性更强

# In[8]:


from sklearn.preprocessing import StandardScaler, RobustScaler

# std_scaler = StandardScaler()
rub_scaler = RobustScaler() # 鲁棒性更强

# reshape(-1,1) 将data['Amount']变成只有一列，行数不限定的np.array
data['scaledAmount'] = rub_scaler.fit_transform(data['Amount'].values.reshape(-1,1))
data['scaledTime'] = rub_scaler.fit_transform(data['Time'].values.reshape(-1,1))

print('未标准化的Amount：',data['Amount'].values.reshape(-1,1))
print('标准化后的Amount：',rub_scaler.fit_transform(data['Amount'].values.reshape(-1,1)))
print('未标准化的Time：',data['Time'].values.reshape(-1,1))
print('标准化后的Time：',rub_scaler.fit_transform(data['Time'].values.reshape(-1,1)))


# 新建子数据集：删除不需要使用到的两列数据
new_data = data.drop(['Time','Amount'], axis = 1)
new_data.head()


# 
# ## 平衡样本
# 
# 在进行平衡样本的数据预处理以前，先来谈谈非平衡样本的影响以及常用的一些平衡样本的方法，及适用场景。
# 
# ### 不平衡样本
# 
# 不平衡的样本会影响模型的评估效果，严重的会带来过拟合的结果。所以我们需要让正负样本在训练过程中拥有相同话语权或权重。在这里，称数据集中样本较多的一类称为“大众类”（majority class），样本较少的一类称为“小众类”（minority class）。
# 
# 对于不平衡样本的处理做法总结如下[[1]](https://blog.csdn.net/sinat_26917383/article/details/75890859)：
# ![image.png](attachment:image.png)
# 
# 
# 
# 常规做法是进行**上采样**与**下采样**，也就是下采样（**Undersampling**,欠采样）大众类，上采样（**Oversampling**，过采样）小众类。但是这样也会有相应的弊端出现。因为上采样是复制多份小众类，也就是下采样是选取部分大众类，所以上采样中小众类会反复出现一些样本，这会导致过拟合；下采样会由于丢失信息而导致欠拟合。
# 
# 所以针对**下采样信息丢失**的问题，有**EasyEnsemble**，与**BalanceCascade**两种**改进**方法。
# 
# 对于**上采样的改进方法**，可以通过**数据合成**方法来基于已有的数据生成更多的样本，其中数**SMOTE**最为常见；
# 或者可以通过**加权**的方式来解决问题，但其难点在于如何合理设置权重。
# 
# 同样的，我们可以换一种角度，对于正负样本极不平衡的情况下，我们也可以视其为**异常值检测**（Outlier Detection）或**一分类**（One Class Learning）问题。经典的工具包有One-class SVM等。
# 
# 以上方法着重于处理数据，但同时也有适用于不平衡样本的模型比如XGBoost 。
# 
# **所以解决不平衡样本的问题有很多种方法，那如何选择？**[[1]](https://blog.csdn.net/sinat_26917383/article/details/75890859)
# >- 在**正负样本都非常之少**的情况下, 采用**数据合成**的方式
# - 在**负样本足够多，正样本非常之少**且比例及其悬殊的情况下, 考虑**一分类**方法
# - 在**正负样本都足够多**且比例不是特别悬殊的情况下, 应该考虑**采样**或者**加权**的方法
# 
# 
# 

# ## 3种方式平衡样本
# 接下来会尝试3种不同的方式来平衡样本，考虑到正样本量占比仅为0.17%，如果使用欠采样会造成样本大量丢失，且不足以让模型训练学习，所以不考虑欠采样。
# - 随机过采样：按指定比例随机复制少数类样本。缺陷：重复样本过多，分类器过拟合。
# - SMOTE过采样：基于分布线性插值生成合成样本。缺陷：稀有事件样本被重复复制过多次，造成模型过于关注局部信息而造成过拟合。
# - 综合采样法：结合了欠采样与过采样，综合解决类别分布不平衡的和过拟合问题。比如有SMOTE+Tomek，SMOTE+KNN。缺陷：会出现过采样和欠采样的缺点。

# ### Step 1. 训练集与测试集切分
# 
# 两种切分方式:
# - 随机抽样`train_test_split`：随机抽取构建训练集与测试集，标签分布不一定一致，适用于较平衡的样本
# - [分层抽样](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedShuffleSplit.html)`StratifiedShuffleSplit`：可以保证训练与测试集中不同标签的分布与原始数据的标签分布基本一致，适用于不平衡样本
# 
# 这里切分比例为 `训练集：测试集 = 7：3`

# In[9]:


from sklearn.model_selection import train_test_split       # 随机抽样
from sklearn.model_selection import StratifiedShuffleSplit # 分层抽样


# 划分特征数据 和标签数据
X = new_data.iloc[:, new_data.columns != 'Class'] # 选取特征列数据
y = new_data.iloc[:, new_data.columns == 'Class'] # 选取类别label
print('X shape:',X.shape, '\ny shape:',y.shape)


# 方式一：随机抽样
# X = np.array(new_data.iloc[:, new_data.columns != 'Class']) # 选取特征列数据
# y = np.array(new_data.iloc[:, new_data.columns == 'Class']) # 选取类别label
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1234)

# 方式二：按比例分层抽样
#  cross-validator中划分迭代次数设为10
sss = StratifiedShuffleSplit(n_splits=10,test_size=0.3,train_size=None, random_state=12345)


for train_index, test_index in sss.split(X,y):
    print('Train:', train_index, 'Test:', test_index)
    original_Xtrain, original_Xtest = X.iloc[train_index], X.iloc[test_index]
    original_ytrain, original_ytest = y.iloc[train_index], y.iloc[test_index]


# 矩阵化训练集与测试集
original_X_train = np.array(original_Xtrain)
original_X_test = np.array(original_Xtest)
original_y_train = np.array(original_ytrain)
original_y_test = np.array(original_ytest)


# In[10]:


# 查看训练集和测试集标签分布
train_unique_label, train_label_count = np.unique(original_y_train, return_counts=True)
test_unique_label, test_label_count = np.unique(original_y_test, return_counts=True)

train_label_rate = train_label_count / len(original_ytrain)
test_label_rate = test_label_count / len(original_ytest)


print("\n训练集标签{}:{}个, 标签{}:{}个".format(train_unique_label[0],train_label_count[0], train_unique_label[1],train_label_count[1] ))
print("\n训练集标签分布比例：")
for label,rate in zip(train_unique_label, train_label_rate):
    print('标签{} 占比:{:.2f}%'.format(label,100*rate))

print("\n测试集标签{}:{}个, 标签{}:{}个".format(test_unique_label[0],test_label_count[0], test_unique_label[1],test_label_count[1] ))
print("\n测试集标签分布比例：")
for label,rate in zip(test_unique_label,test_label_rate):
    print('标签{} 占比:{:.2f}%'.format(label,100*rate))


# ### Step 2. 对训练数据进行样本平衡

# In[ ]:


#pip uninstall imbalanced-learn


# In[ ]:


# 安装 imblearn 0.7.0
get_ipython().system('pip install imbalanced-learn==0.7.0 -i https://pypi.tuna.tsinghua.edu.cn/simple  --trusted-host pypi.tuna.tsinghua.edu.cn')


# In[11]:


from imblearn.over_sampling import RandomOverSampler, SMOTE
from imblearn.combine import SMOTETomek


# In[15]:


ros = RandomOverSampler(random_state=0)
sos = SMOTE(random_state = 0)
kos = SMOTETomek(random_state = 0)

# 这一步耗时较长
X_ros, y_ros = ros.fit_sample(original_X_train, original_y_train)
X_sos, y_sos = sos.fit_sample(original_X_train, original_y_train)
X_kos, y_kos = kos.fit_sample(original_X_train, original_y_train)

print('ros:{}, sos:{}, kos:{}'.format(len(y_ros), len(y_sos), len(y_kos)))


# 查看采样后的正负样本数量

# In[17]:


print('训练集正样本数统计，原始训练集:{} \n随机过采样后训练集:{}, SMOTE过采样后训练集:{}, 综合过采样后训练集:{}      '.format(original_y_train.sum(), y_ros.sum(), y_sos.sum(), y_kos.sum()))
print('原始训练集中敷眼部占比为{:.2f}%, 通过3种过采样方式后训练集的负样本占比都提升至：{:.0f}%'.format(100*original_y_train.sum()/len(original_y_train), 100*y_ros.sum()/len(y_ros)))


# # 建模与模型评估

# In[18]:


from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import confusion_matrix, roc_curve, auc, recall_score, classification_report


# ## LR建模
# ### 原始训练集 vs 过采样训练集 建模效果
# - 这里使用的衡量模型表现的标准为`f1-score`，因为想要捕捉更多的少数类（欺诈交易），同时希望维持较高的准确率。
# 
# Tip:CV的运行过程可在页面下方的【日志监控】处查看

# In[19]:


lr = LogisticRegression(max_iter = 500)

# 定义正则化权重参数，用以控制过拟合
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


print('最好的参数：', lr_cv1.best_params_)


# 可以看出用原始训练集训练的模型有很好的precision:90%,但是灵敏度recall(66.9%)并不高。这表示虽然预测为正的样本中有90%的实际也为正样本，但是实际所有的正样本中只有66.9%左右会被模型识别出。
# 
# 经过过采样处理的训练集普遍都和很好的敏感度，但是相应的precision就下降了非常多，仅为6%。模型的recall和precision失衡严重，并不是一个好的模型。
# 
# 接下来会尝试对正样本和负样本类别进行权重设置来训练模型。

# ### 原始数据集调整类别权重参数后建模效果

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


# 这次，模型的敏感度recall与精确度precision取得了较好的平衡。

# In[26]:


print('模型最优参数：',lr_cv2.best_params_)


# ### 绘制混淆矩阵

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


# 对原训练集进行预测
y_train_pre = lr_cv2.predict(original_X_train)

# 训练集的混淆矩阵
cnf_matrix_train = confusion_matrix(original_y_train, y_train_pre)

print("训练集实际标签数量统计：\n标签{}:{}个, 标签{}:{}个".format(train_unique_label[0],train_label_count[0], train_unique_label[1],train_label_count[1] ))
print("Recall: {:.2f}%".format(100*cnf_matrix_train[1,1]/(cnf_matrix_train[1,0]+cnf_matrix_train[1,1])))

class_names = [0,1]
plt.figure()
plot_confusion_matrix(cnf_matrix_train , classes=class_names, title='Confusion matrix')
plt.show()


# In[29]:


# 对测试集进行预测
y_pre = lr_cv2.predict(original_X_test)

# 测试集的混淆矩阵
cnf_matrix = confusion_matrix(original_y_test, y_pre)

print("测试集实际标签数量统计：\n标签{}:{}个, 标签{}:{}个".format(test_unique_label[0],test_label_count[0], test_unique_label[1],test_label_count[1] ))
print("测试集Recall: {:.2f}%".format(100*cnf_matrix[1,1]/(cnf_matrix[1,0]+cnf_matrix[1,1])))

class_names = [0,1]
plt.figure()
plot_confusion_matrix(cnf_matrix , classes=class_names, title='Confusion matrix')
plt.show()


# ## 决策树建模
# 决策树是一种基本的分类和回归方法。它每次选取一个特征，对现有的训练数据集进行划分，使得各个分割后的子集，在当前条件下有最好的分类。
# 决策树对不同量纲的特征不敏感，所以也可以使用未缩放特征的数据进行训练。

# In[30]:


from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz


# In[ ]:


tree_params = {
    "criterion": ["gini", "entropy"], # 损失函数：基尼、熵
    "max_depth": list(range(2, 4, 1)), # 最大深度 2、3
    "min_samples_leaf": list(range(5, 7, 1)) # 叶子数需要为奇数
}
dt_cv = GridSearchCV(DecisionTreeClassifier(), tree_params, scoring='f1')
dt_cv.fit(original_X_train, original_y_train.ravel())


# In[ ]:


print('模型最优参数：',dt_cv.best_params_)


# In[ ]:


predict3 = dt_cv.predict(original_X_test)
print('AUC:{:.3f} Recall:{:.3f} Precision:{:.3f}'.format(
        metrics.roc_auc_score(original_y_test, predict3),
        metrics.recall_score(original_y_test, predict3),
        metrics.precision_score(original_y_test, predict3)
    ))


# ### 绘制决策树

# In[30]:


get_ipython().system('pip install pydotplus==2.0.2 -i https://pypi.tuna.tsinghua.edu.cn/simple  --trusted-host pypi.tuna.tsinghua.edu.cn')


# In[42]:


# 基于最优参数构造决策树分类器
dt_clf = DecisionTreeClassifier(criterion='entropy', max_depth=3, min_samples_leaf=5) 
dt_clf.fit(original_X_train, original_y_train.ravel())


# In[55]:


import pydotplus
from IPython.display import display, Image

dot_data = export_graphviz(dt_clf,  # 决策树模型
                            out_file=None, # 输出文件格式
                            feature_names=X.columns, # 特征矩阵
                            class_names = ['normal', 'fraud'], # 标签，按数字升序
                            filled = True, # 由颜色标识不纯度
                            rounded =True  # 树节点为圆角矩形
                        )
                               
graph = pydotplus.graph_from_dot_data(dot_data)
display(Image(graph.create_png()))


# # 可视化模型效果

# ## 分类器效果对比
# ### 绘制ROC曲线
# FPR（False Positive Rate，假阳性率）, TPR(True Positive Rate，真阳性率)分别对应ROC曲线的横坐标与纵坐标
# 
# - **真阳性率**（灵敏度）= **召回率**（Recall）：
# 
# 	如果一个实例类别是positive，分类器预测结果的类别也是positive的比例。这个指标也叫敏感度（sensitivity）或召回率（recall），描述了分类器对positive类别的**敏感程度**。
# 
# 	~$TPR = \frac{TP}{TP+FN}~$ 
# 
# - **假阳性率** = **错检率**（fallout）:
# 
# 	如果一个实例类别是negative，分类器预测结果的类别是positive的比例。这个指标也叫错检率（fallout）。
# 
# 	~$FPR = \frac{FP}{FP+TN}~$  

# In[56]:


# 逻辑回归
fpr, tpr, thresholds = roc_curve(original_y_test, predict2)
roc_auc = auc(fpr, tpr)
print('Logistic Regression AUC：{:.2f}%'.format(100*roc_auc))

# 决策树
dt_fpr, dt_tpr, dt_thresholds = roc_curve(original_y_test, predict3)
dt_roc_auc = auc(dt_fpr, dt_tpr)
print('Decision Tree AUC：{:.2f}%'.format(100*dt_roc_auc))

# Plot ROC

plt.title('Receiver Operating Characteristic')
plt.plot(fpr, tpr, 'b',label='Logistic Regression AUC = %0.3f'% roc_auc)
plt.plot(dt_fpr, dt_tpr, 'y', label='Decision Tress AUC = %0.3f'% dt_roc_auc)
plt.legend(loc='lower right') # 设置legend的位置
plt.plot([0,1],[0,1],'r--') # red, --
plt.xlim([-0.1,1.0])
plt.ylim([-0.1,1.01])
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.show()


# 逻辑回归与决策树两个分类器的ROC曲线几乎重叠，两者都接近左上角，即AUC(Area Under Curve)面积到达`0.898`至`0.899`，说明两个模型效果都还不错（`1`最完美）。最靠近左上角的ROC曲线的点是错误最少的最好阈值（thresholds），其假阳性与假阴性的总数最少。

# 虽然进行了平衡样本处理，模型的分类效果有所提高，但是能够获取到更多的欺诈样本数据才是王道！毕竟数据质量决定了模型的上限，再多的优化也只是无限逼近这个上限。
