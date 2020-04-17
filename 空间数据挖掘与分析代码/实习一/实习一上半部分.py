import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
plt.rcParams['font.sans-serif'] = 'simhei'
plt.rcParams['axes.unicode_minus'] = False
data1 = pd.read_csv('D:\gb\网课\空间数据挖掘与分析\教材使用数据集\datasets\magic04.csv',encoding = 'gb2312')
data2 = pd.read_csv('D:\gb\网课\空间数据挖掘与分析\教材使用数据集\datasets\magic04(1).csv',encoding = 'gb2312')
s0 = data1['1']
s1 = data1['2']
p = plt.figure(figsize=(6,4))

def cos_dist(vec1,vec2):
    """
    :param vec1: 向量1
    :param vec2: 向量2
    :return: 返回两个向量的余弦相似度
    """
    dist1=float(np.dot(vec1,vec2)/(np.linalg.norm(vec1)*np.linalg.norm(vec2)))
    return dist1
if __name__ == '__main__':

    dist1 = cos_dist(s0, s1)
    print(dist1)
print(data2.shape)
print(np.cov(data2))


plt.scatter(s0[1:],s1[1:],marker='o',c='black')
plt.scatter(np.mean(s0[1:]),np.mean(s1[1:]),marker='o',c='red')
plt.xticks(range(0,350,30))
plt.xlabel('属性1')
plt.ylabel('属性2')
plt.legend(['两个属性之间的特征点', '特征点的μ值'])
plt.title("前两个属性之间的特征散点图")
plt.show()