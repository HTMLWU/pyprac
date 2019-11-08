# 忽略警告提示
import warnings
warnings.filterwarnings('ignore')

# 导入数据分析包
import pandas as pd
import numpy as np

# 导入数据可视化包
import matplotlib.pyplot as plt
import seaborn as sns

# 导入数据
train_df = pd.read_csv('./titanic/train.csv',encoding='gbk')
test_df = pd.read_csv('./titanic/test.csv',encoding='gbk')
print('训练数据集:',train_df.shape,'测试数据集:',test_df.shape)


# 查看训练数据
print('train data ==============>>>>')
train_df.head()