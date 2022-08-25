import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from itertools import chain
from scipy import interpolate
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
points=[]
values=[]
#读取数据
a=pd.read_excel(r"E:\原始\2020\处理\画图\悬沙\南槽外悬沙小潮.xlsx")
a.set_index('date',inplace=True)
x=a.index.values
y=a.columns.values[:-1]
z=a.drop(["水位"],axis=1)
water_level=a["水位"]
X,Y =np.meshgrid(x,y)
for i in x:
	for j in y:
		points.append([i,water_level[i]-j*water_level[i]])
values=list(chain(*(z.values)))
grid_x, grid_y = np.mgrid[0:x.max():200j, 0:water_level.max():400j]
grid_z0 = interpolate.griddata(points, values, (grid_x, grid_y), method='linear')
print(grid_z0)
print(grid_x)
b=plt.plot(x,water_level,linewidth=0.8,c='black')
#chart=plt.pcolor(grid_x, grid_y, grid_z0,cmap='Spectral_r')
lim=np.linspace(0,2,30)
chart=plt.contourf(grid_x, grid_y, grid_z0,lim,cmap='Spectral_r', alpha=1)
a=plt.contour(grid_x, grid_y, grid_z0,[0.1,0.2,0.5,1,1.5,2],colors="black", linewidths=0.8, linestyles='-.')
plt.clabel(a,fontsize=8,colors='k')
plt.fill_between(x,water_level,water_level.max(),facecolor="white",zorder=100)
plt.xlim(2,25)
plt.ylim(0,18)
tuli=plt.colorbar(chart)
tuli.set_label("盐度(psu)",size=15)
tuli.ax.tick_params(labelsize=15)
plt.xlabel("时间t(h)",size=14)
plt.ylabel("水深Z(m)",size=14)
plt.tick_params(labelsize=15)
plt.text(18.5,14, r'A2001小潮', color='black', fontweight=100, fontsize=16,zorder=100)
plt.title("A2001小潮垂向悬沙分布")

plt.show()
