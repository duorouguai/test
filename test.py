import random

import pandas as pd
import xlrd
import matplotlib
import sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.model_selection import train_test_split
dasa
pandas
pandas
df = pd.read_csv("E:/Download/adult.csv", header=None,
                 names=['年龄', '单位性质', '权重', '学历', '受教育时长', '婚姻状况', '职业', '家庭情况', '种族', '性别', '资产所得', '资产损失', '周工作时长',
                        '原籍', '收入'])
pd.set_option('display.max_columns', None)
pd.set_option('max_colwidth', 100)
print(df)
part_data = df[['年龄', '单位性质', '学历', '性别', '周工作时长', '职业', '收入']]
print(part_data.head())
data_dummies = pd.get_dummies(df)
print(df.columns)
print(data_dummies.columns)
print(data_dummies.head())
feature = data_dummies.loc[:, '单位性质_ Local-gov':'原籍_ Yugoslavia']
X = feature.values
y = data_dummies['收入_ >50K'].values

print('\n\n\n')
print('代码运行结果')
print('====================================\n')
#打印数据形态
print('特征形态:{},标签形态:{}'.format(X.shape,y.shape))
print('\n====================================')
print('\n\n\n')

X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=0)
decision_tree_classifier = ExtraTreesClassifier()
decision_tree_classifier.fit(X_train,y_train)

print("模型得分{:.2f}".format(decision_tree_classifier.score(X_test,y_test)))
ls = []
for i in range(100):
    if i==0 or i==2 or i==3 or i==5:
        ls.append(random.randint(1,100))
    elif i==1:
        ls.append(random.randint(70000,300000))
    else:
        ls.append(random.randint(0,1))

print(len(ls))
ls1=[]
ls1.append(ls)
print(ls1)
res = decision_tree_classifier.predict(ls1)
if res==0:
    print("salary is more than 50K")
else:
    print("GG")
