import polyskel

import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

import xlrd
import xlwt
import csv

import os

import warnings
warnings.filterwarnings('ignore')

def default_ax(size=8):
    fig, ax = plt.subplots()
    fig.set_size_inches(size, size)
    ax.axison = False
    ax.set_aspect('equal')
    return ax

"""
def show_rooms(df):
    ax = default_ax()
    df.plot(ax=ax, linewidth=0.3, color='#aaaaaa')
    for index in df.index:
        row = df.loc[index]
        plt.annotate(s=index, xy=[row.geometry.centroid.x, row.geometry.centroid.y],
                     horizontalalignment='center', fontsize=6)
    plt.show()

"""

workbook=xlwt.Workbook(encoding='utf-8')
worksheet=workbook.add_sheet('1')
i=0


csvFile = open("Room 1000001.csv", "r")
reader = csv.reader(csvFile)
a=[]

for item in reader:
    a.append((float(item[0]),float(item[1])))

###########################to reverse the list here sometimes do not need###################
b=[]
m=len(a)
for i in range(m):
    b.append(a[m-1-i])
##########################
    
csvFile.close()

csvFile2=open("Room 100000 hole.csv", "r")
reader2=csv.reader(csvFile2)
x=[]

for item in reader2:
    x.append((float(item[0]),float(item[1])))

hole_temp=[]
n=len(x)
for j in range(n):
    hole_temp.append(x[n-1-j])
hole=[]
hole.append(tuple(hole_temp))
"""

b=[(0,0),(0,1),(2,1),(2,3),(2.5,3),(2.5,0)]
"""
#b=[(66.4494289351231, -6.02141163972236), (100.949428935123, -6.02141163972247),(100.949428935123, -31.9337026474633),(66.4494289351231, -31.9337026474632),(66.4494289351231, -6.02141163972236)]
#hole=[((-20.5177767923733,-18.5052392),(-8.517776792,-18.5052392),(-8.517776792,-7.339952647),(21.23222321,-7.339952647),(21.23222321,-30.38118704),(1.232223208,-30.38118704),(-20.51777679,-30.38118704),(-20.51777679,-18.5052392))]
hole2=[(107.112189,1.47498876),(34.5119289,1.47498876),(34.5119289,-18.756619),(107.112189,-18.756619),(107.112189,1.47498876)]

#skeleton=polyskel.skeletonize(b,[((29.5119289,1.47498876),(-6.1547377,1.47498876),(-6.1547377,-18.756619),(29.5119289,-18.756619),(29.5119289,1.47498876)),((107.112189,1.47498876),(34.5119289,1.47498876),(34.5119289,-18.756619),(107.112189,-18.756619),(107.112189,1.47498876))])
#hole=[((91.68001117,20.02983902),(106.5535956,20.02983902),(106.5535956,42.86317235),(91.68001117,42.86317235),(91.68001117,20.02983902))]

##############################################
skeleton=polyskel.skeletonize(b,holes=hole)
##############################################

sg = nx.Graph()
l=0
for edge in skeleton:
        source = edge.source
        for sink in edge.sinks:
            sg.add_edge(source, sink)
            worksheet.write(l,0,source[0])
            worksheet.write(l,1,source[1])
            worksheet.write(l,2,sink[0])
            worksheet.write(l,3,sink[1])
            l=l+1
            print ((source[0],source[1],sink[0],sink[1]))

workbook.save('excel.xls')

pos94 = {}
for node in sg.nodes():
    pos94[node] = (node.x, node.y)
    print ((node.x,node.y))


#sg.add_edge(1,2)
#sg.add_edge(2,3)
#sg.add_edge(3,4)
#b1={1:(0,0),2:(0,1),3:(2,1),4:(2,0)}

ax = default_ax(size=12)
nx.draw(sg, pos94, node_size = 10, ax=ax, edge_color='r')
#nx.draw(sg, pos=b1, ax=ax, edge_color='b')
plt.show()
