#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><ul class="toc-item"><li><span><a href="#分析背景" data-toc-modified-id="分析背景-0.1">分析背景</a></span></li><li><span><a href="#分析目标" data-toc-modified-id="分析目标-0.2">分析目标</a></span></li></ul></li><li><span><a href="#1-数据概况分析" data-toc-modified-id="1-数据概况分析-1">1 数据概况分析</a></span><ul class="toc-item"><li><span><a href="#1.1-数据预览" data-toc-modified-id="1.1-数据预览-1.1">1.1 数据预览</a></span><ul class="toc-item"><li><span><a href="#指标解释" data-toc-modified-id="指标解释-1.1.1">指标解释</a></span></li></ul></li><li><span><a href="#1.2-数据清洗" data-toc-modified-id="1.2-数据清洗-1.2">1.2 数据清洗</a></span><ul class="toc-item"><li><span><a href="#1.2.1-类别型变量" data-toc-modified-id="1.2.1-类别型变量-1.2.1">1.2.1 类别型变量</a></span></li></ul></li></ul></li><li><span><a href="#2-单变量分析" data-toc-modified-id="2-单变量分析-2">2 单变量分析</a></span><ul class="toc-item"><li><span><a href="#2.1-观察样本0、1的平衡性" data-toc-modified-id="2.1-观察样本0、1的平衡性-2.1">2.1 观察样本0、1的平衡性</a></span></li><li><span><a href="#2.2-观察均值大小" data-toc-modified-id="2.2-观察均值大小-2.2">2.2 观察均值大小</a></span><ul class="toc-item"><li><span><a href="#对于数据类型为0和1的变量，观察均值大小可以帮助我们分析这个变量在flag上的分布：" data-toc-modified-id="对于数据类型为0和1的变量，观察均值大小可以帮助我们分析这个变量在flag上的分布：-2.2.1">对于数据类型为0和1的变量，观察均值大小可以帮助我们分析这个变量在flag上的分布：</a></span></li></ul></li><li><span><a href="#2.3-可视化" data-toc-modified-id="2.3-可视化-2.3">2.3 可视化</a></span></li></ul></li><li><span><a href="#3-相关和可视化" data-toc-modified-id="3-相关和可视化-3">3 相关和可视化</a></span></li><li><span><a href="#4-逻辑回归模型的建立和评估" data-toc-modified-id="4-逻辑回归模型的建立和评估-4">4 逻辑回归模型的建立和评估</a></span><ul class="toc-item"><li><span><a href="#4.1-模型建立" data-toc-modified-id="4.1-模型建立-4.1">4.1 模型建立</a></span><ul class="toc-item"><li><span><a href="#4.1.1-抽取训练集和测试集并进行拟合" data-toc-modified-id="4.1.1-抽取训练集和测试集并进行拟合-4.1.1">4.1.1 抽取训练集和测试集并进行拟合</a></span></li><li><span><a href="#4.1.2-查看模型结果" data-toc-modified-id="4.1.2-查看模型结果-4.1.2">4.1.2 查看模型结果</a></span></li></ul></li><li><span><a href="#4.2-模型评估" data-toc-modified-id="4.2-模型评估-4.2">4.2 模型评估</a></span><ul class="toc-item"><li><span><a href="#4.2.1-评估方法一：计算准确度" data-toc-modified-id="4.2.1-评估方法一：计算准确度-4.2.1">4.2.1 评估方法一：计算准确度</a></span><ul class="toc-item"><li><span><a href="#比较训练集和测试集的准确率，保证内在信息一致性:" data-toc-modified-id="比较训练集和测试集的准确率，保证内在信息一致性:-4.2.1.1">比较训练集和测试集的准确率，保证内在信息一致性:</a></span></li></ul></li><li><span><a href="#4.2.2-评估方法二：ROC和AUC" data-toc-modified-id="4.2.2-评估方法二：ROC和AUC-4.2.2">4.2.2 评估方法二：ROC和AUC</a></span></li></ul></li><li><span><a href="#4.3-模型优化" data-toc-modified-id="4.3-模型优化-4.3">4.3 模型优化</a></span></li></ul></li><li><span><a href="#5-业务建议" data-toc-modified-id="5-业务建议-5">5 业务建议</a></span><ul class="toc-item"><li><span><a href="#5.1-用户分析" data-toc-modified-id="5.1-用户分析-5.1">5.1 用户分析</a></span></li><li><span><a href="#5.2-提高优惠券使用率分析---高价值用户" data-toc-modified-id="5.2-提高优惠券使用率分析---高价值用户-5.2">5.2 提高优惠券使用率分析 - 高价值用户</a></span></li><li><span><a href="#5.3-结论" data-toc-modified-id="5.3-结论-5.3">5.3 结论</a></span></li></ul></li></ul></div>

# ## 分析背景
# “天猫”（英文：Tmail，亦称淘宝商城，天猫商城）原名淘宝商城，是一个综合性购物网站，也是马云淘宝网打造的B2C(Business-to-Consumer, 商业零售)品牌。其整合数千家品牌商、生产商，为商家和消费者之间提供一站式解决方案，提供100%品质保证的商品，7天无理由退货的售后服务，以及购物积分返现等优质服务

# ## 分析目标
# 根据用户数据以及消费行为数据
# - 使用Python建立分类模型，进行逻辑回归
# - 预测使用优惠券概率较高的客群

# # 1 数据概况分析

# ## 1.1 数据预览

# ### 指标解释
# - ID	记录编码
# 
# - age	年龄
# 
# - job	职业
# 
# - marital	婚姻状态
# 
# - default	花呗是否有违约
# 
# - returned	是否有过退货
# 
# - loan	是否使用花呗结账
# 
# - coupon_used_in_last6_month	过去六个月使用的优惠券数量
# 
# - coupon_used_in_last_month	过去一个月使用的优惠券数量
# 
# - coupon_ind	该次活动中是否有使用优惠券

# In[1]:


#导入模块和数据
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')

coupon = pd.read_csv('tianmao.csv')
coupon.head()


# In[2]:


#查看数据行列总数
coupon.shape


# In[3]:


#查看数据是否有缺失值
coupon.info()


# 查看完数据整体后，发现无缺失值

# ## 1.2 数据清洗

# ### 1.2.1 类别型变量

# In[4]:


#将类别型变量转换为数字型变量，便于之后分析
#但在本案例中，为了后续分析方便，只处理default, returned, loan这三个变量，保留job, marital 
#把default、returned、loan三个变量单独取出来进行哑变量处理get_dummies()。
coupon1 = coupon[['default','returned','loan']]
coupon1 = pd.get_dummies(coupon1)
coupon1.head()


# In[5]:


#把处理后的表格和原表格进行拼接
coupon = pd.concat([coupon, coupon1], axis = 1)
coupon.head()


# In[6]:


#删除包含重复信息和无意义信息的数据
coupon.drop(['ID', 'default', 'default_no', 'returned', 'returned_no', 'loan', 'loan_no'], axis = 1, inplace = True)

#将coupon_ind重新命名为flag，便于之后分析
coupon = coupon.rename(columns = {'coupon_ind' : 'flag'})
coupon.info()


# # 2 单变量分析

# ## 2.1 观察样本0、1的平衡性

# In[7]:


#二分类模型，观察样本(flag)0,1的平衡性
coupon['flag'].value_counts(1)


# - 在二分类问题中，0、1的占比要保持平衡型，实际情况中不低于0.05，否则会影响模型的预测
# - 该数据集0、1占比均高于0.05，因此其分布是合理的

# ## 2.2 观察均值大小

# In[8]:


#先按客户是否使用coupon进行分类聚合
summary = coupon.groupby(['flag'])
#求出各种情况均值的占比情况
summary.mean()


# ### 对于数据类型为0和1的变量，观察均值大小可以帮助我们分析这个变量在flag上的分布：
# - coupon_used_in_last_month在0的均值为0.26，在1的均值为0.53，说明越是在上个月使用了coupon的客户，接下来再使用coupon的概率会越高
# - default_yes和loan_yes在0时的均值均大于在1时的均值，说明花呗违约和用花呗结账的客户在接下来的时间里使用coupon的概率较小
# - age在0和1的均值分别为40.8和41.8，差别不大，说明年龄无太大的区分关系

# ## 2.3 可视化

# In[9]:


#观察returned_yes在flag上的分布
sns.countplot(y = 'returned_yes', hue = 'flag', data = coupon)


# - 相比起没有退货的客户，退货的客户使用coupon的概率较小

# In[10]:


#观察marital在flag上的分布
sns.countplot(y = 'marital', hue = 'flag', data = coupon)


# - 已婚客户使用coupon的概率比未婚和离婚客户使用coupon的概率略高
# - 已婚人士未使用coupon的概率比未婚人士未使用coupon的概率也要高
# - 但是三者均未使用coupon的概率比使用coupon的概率要高得多

# In[11]:


#观察job在flag上的分布
sns.countplot(y = 'job', hue = 'flag', data = coupon, order = coupon['job'].value_counts().index)


# - job title为management, technician, blue-collar的客户越有可能使用coupon

# In[12]:


#观察age在flag上的分布
sns.distplot(coupon['age'])


# In[13]:


#查看age在整体数据的分布情况
coupon['age'].describe()


# - 数据显示18 - 95岁的客户使用coupon可能性较高，使用coupon概率较高的客群集中在40岁
# - 发现age > 60岁的极端值较少，但它们影响了整体数据分布，需要把这部分数据剔除在分析范围外

# In[15]:


#对于年龄进行快速分组，探究各个年龄段对于是否使用coupon的影响
age60 = coupon[coupon['age'] < 60]
bins = [0, 20, 40, 60]
labels = ['<20','<40','<60']
age60['age_new'] = pd.cut(age60.age, bins, right=False,labels = labels)
age60.groupby(['age_new'])['age'].describe()


# In[16]:


age60['age_new'].describe()


# In[17]:


#绘制age60['age_new']的饼图，使数据更加直观
plt.figure(figsize=[9,7])
age60['age_new'].value_counts().plot.pie()
plt.show()


# - 20 - 40岁的客群使用coupon概率最高
# - 18，32，48岁分别为三个年龄段中使用coupon概率较高的年龄平均值

# # 3 相关和可视化

# In[18]:


#围绕flag变量，观察它与其他变量的关系
coupon.corr()[['flag']].sort_values('flag', ascending = False)


# In[19]:


sns.heatmap(coupon.corr(), cmap = 'Blues')


# - flag与coupon_used_in_last_month, age成强正相关关系
# - flag与coupon_used_in_last6_month, returned_yes成强负相关关系
# - 其他变量与flag的相关不明显，为了分析准确性，因此不做过度解读

# # 4 逻辑回归模型的建立和评估

# ## 4.1 模型建立
# 

# ### 4.1.1 抽取训练集和测试集并进行拟合

# In[20]:


#先设定自变量x和因变量y
x = coupon[['coupon_used_in_last_month', 'returned_yes', 'loan_yes']]
y = coupon['flag']


# In[21]:


#调用sklearn模块，随机抽取训练集和测试集
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 100) #训练集和测试集抽取比例为70/30

#调用sklearn中逻辑回归模块
from sklearn import linear_model
lr = linear_model.LogisticRegression()

#拟合
lr.fit(x_train, y_train)


# ### 4.1.2 查看模型结果

# In[22]:


#查看系数
lr.coef_


# - 当coupon_used_in_last_month从0到1时，不使用coupon到使用coupon的概率提升是e的0.38，即是其他组客户的1.46倍
# - 当returned_yes从1到0时，使用coupon到不使用coupon的概率提升是其他组客户的0.38倍
# - 当loan_yes从1到0时，使用coupon到不使用coupon的概率提升是其他组客户的0.57倍
# - 故从概率来看，上月使用过coupon的客户、未退货客户和未用花呗付款的客群再使用coupon的概率会更高。

# In[23]:


#查看截距
lr.intercept_


# ## 4.2 模型评估

# ### 4.2.1 评估方法一：计算准确度

# In[24]:


#通过训练集和测试集的自变量x，分别计算出对应的预测值
y_pred_train = lr.predict(x_train)
y_pred_test = lr.predict(x_test)


# In[25]:


#搭建训练集混淆矩阵
from sklearn import metrics
metrics.confusion_matrix(y_train, y_pred_train)


# In[26]:


#查看训练集准确率
metrics.accuracy_score(y_train, y_pred_train)


# In[27]:


#搭建测试集混淆矩阵
metrics.confusion_matrix(y_test, y_pred_test)


# In[28]:


#查看测试集准确率
metrics.accuracy_score(y_test, y_pred_test)


# #### 比较训练集和测试集的准确率，保证内在信息一致性:
# - 模型在train和test的表现中不能相差过大。案例中训练集与测试集的准确率相差很小，故该模型是合理的
# - 但是未来客群和特点都可能会发生变化，需要做出自己的平衡。train和test只是帮助建立一个概念，不要为了单独的模型太过追求准确率

# ### 4.2.2 评估方法二：ROC和AUC

# In[29]:


#使用auc评估模型
from sklearn.metrics import roc_curve, auc
fpr,tpr,threshold = roc_curve(y_train, y_pred_train)
roc_auc = auc(fpr,tpr)

print(roc_auc)


# 一般好的模型评分在0.7 - 0.8之间，故此模型需要被调整

# ## 4.3 模型优化

# In[30]:


#新增变量returned_yes
x = coupon[['coupon_used_in_last_month', 'returned_yes', 'loan_yes', 'coupon_used_in_last6_month', 'default_yes', 'age']]
y = coupon['flag']


# In[31]:


#调用sklearn模块，随机抽取训练集和测试集
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 100) #训练集和测试集抽取比例为70/30

#调用sklearn中逻辑回归模块
from sklearn import linear_model
lr = linear_model.LogisticRegression()

#拟合
lr.fit(x_train, y_train)


# In[32]:


lr.coef_


# In[33]:


#使用auc评估模型
from sklearn.metrics import roc_curve, auc
fpr,tpr,threshold = roc_curve(y_train, y_pred_train)
roc_auc = auc(fpr,tpr)

print(roc_auc)


# - 只有coupon_used_in_last_month, age和flag的成正相关关系，其他变量与flag均为反相关关系
# - 模型迭代后AUC评分变化不大，说明coupon的使用率明显较低

# # 5 业务建议

# ## 5.1 用户分析

# - 数据显示18 - 95岁的客户使用coupon可能性较高，使用coupon概率较高的客群集中在40岁
# - 20 - 40岁的客群使用coupon概率最高
# - 18，32，48岁分别为三个年龄段中使用coupon概率较高的年龄平均值

# ## 5.2 提高优惠券使用率分析 - 高价值用户

# - coupon_used_in_last_month在0的均值为0.26，在1的均值为0.53，说明越是在上个月使用了coupon的客户，接下来再使用coupon的概率会越高
# - default_yes和loan_yes在0时的均值均大于在1时的均值，说明花呗违约和用花呗结账的客户在接下来的时间里使用coupon的概率较小
# 
# 
# - 相比起没有退货的客户，退货的客户使用coupon的概率较小
# - 已婚客户使用coupon的概率比未婚和离婚客户使用coupon的概率略高
# - job title为management, technician, blue-collar的客户越有可能使用coupon
# 
# 
# - flag与coupon_used_in_last_month, age成强正相关关系
# - flag与coupon_used_in_last6_month, returned_yes成强负相关关系
# - 其他变量与flag的相关性都不明显

# ## 5.3 结论

# - 天猫优惠券的使用率较低
# - 重点留意20 - 60客户的留存情况，对有购买潜力或者购买种类比较单一的客户，制定向上销售模型或交叉销售模型，提升现有客户价值
# - 鼓励上月用过优惠券的客户再次使用优惠券，制定相应的产品响应模型或活动响应模型，最大化收益
# - 对无退货客户、已婚客户、无花呗违约和未用花呗结账的用户制定客户流失预警模型或者客户赢回模型，其次是管理、技术员和蓝领阶层，尽量挽回客户
# - 加大APP内优惠券的宣传力度，加强banner、广告推送等营销措施；在APP外进行额外推送、第三方优惠券推送，让客户了解并提升使用优惠券的概率
