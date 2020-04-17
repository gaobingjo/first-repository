import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
# Python实现正态分布
# 绘制正态分布概率密度函数

plt.rcParams['font.sans-serif'] = 'simhei'
plt.rcParams['axes.unicode_minus'] = False
data1 = pd.read_csv('D:\gb\网课\空间数据挖掘与分析\教材使用数据集\datasets\magic04.csv',encoding = 'gb2312')
s0 = data1['1']
s1 = data1['2']
s2 = data1['3']
s3 = data1['4']
s4 = data1['5']
s5 = data1['6']
s6 = data1['7']
s7 = data1['8']
s8 = data1['9']
s9 = data1['10']
μ1=np.mean(s0[1:])
μ2=np.mean(s1[1:])
μ3=np.mean(s2[1:])
μ4=np.mean(s3[1:])
μ5=np.mean(s4[1:])
μ6=np.mean(s5[1:])
μ7=np.mean(s6[1:])
μ8=np.mean(s7[1:])
μ9=np.mean(s8[1:])
μ10=np.mean(s9[1:])
a=[μ1,μ2,μ3,μ4,μ5,μ6,μ7,μ8,μ9,μ10]
print(a)
var1=np.var(s0[1:])
var2=np.var(s1[1:])
var3=np.var(s2[1:])
var4=np.var(s3[1:])
var5=np.var(s4[1:])
var6=np.var(s5[1:])
var7=np.var(s6[1:])
var8=np.var(s7[1:])
var9=np.var(s8[1:])
var10=np.var(s9[1:])
print(var1)
print(var2)
print(var3)
print(var4)
print(var5)
print(var6)
print(var7)
print(var8)
print(var9)
print(var10)
u = np.mean(s0[1:])   # 均值μ
sig1 = np.std(s0[1:],ddof=1) # 标准差δ
max=1/(math.sqrt(2*math.pi)*sig1)
x = np.linspace(u - 5*sig1, u + 5*sig1, 50)
y_sig = np.exp(-(x - u) ** 2 /(2* sig1 **2))/(math.sqrt(2*math.pi)*sig1)
plt.xticks(range(-200,300,30))
plt.xlabel('x' )
plt.ylabel('f(x)')
plt.plot(x, y_sig, linewidth=2)
plt.title("正态分布")
plt.annotate('μ±ε',xy=(u,0),xytext=(u,max),fontsize=16,
    arrowprops=dict(facecolor='black',shrink=0.01))
# plt.plot(x, y, 'r-', x, y, 'go', linewidth=2,markersize=8)
plt.grid(True)
plt.show()