from matplotlib.font_manager import FontProperties
font = FontProperties(fname=r"/System/Library/Fonts/PingFang.ttc", size=14)

import csv
import ast
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
map = Basemap(projection='stere',llcrnrlat=21.5, urcrnrlat=26, llcrnrlon=119.5, urcrnrlon=122.5, resolution='i', lat_0 = 22, lon_0=121)




class House:
    def __init__(self, num, x, y):
        self.num = num
        self.x = float(x)
        self.y = float(y)

lons = []
lats = []
color_lst = []


with open('/Users/yan/Downloads/tw-rental-data/2018Q3-raw-01.csv', newline='') as csvfile:
    rows = csv.DictReader(csvfile)

    for row in rows:
        if row['約略地點_x'] != '-' and row['約略地點_y'] != '-' and row['物件類型'] == '1':
            h = House(row['物件編號'], row['約略地點_x'], row['約略地點_y'])
            lons.append(h.y)
            lats.append(h.x)

            if int(row['月租金']) < 4000:
                color_lst.append('lightcyan')
            elif 4000 <= int(row['月租金']) < 5000:
                color_lst.append('powderblue')
            elif 5000 <= int(row['月租金']) < 6000:
                color_lst.append('lightblue')
            elif 6000 <= int(row['月租金']) < 7000:
                color_lst.append('lightskyblue')
            elif 7000 <= int(row['月租金']) < 8000:
                color_lst.append('deepskyblue')
            elif 8000 <= int(row['月租金']) < 9000:
                color_lst.append('royalblue')
            elif 9000 <= int(row['月租金']) < 10000:
                color_lst.append('mediumblue')
            else:
                color_lst.append('midnightblue')

x, y = map(lons, lats)
map.scatter(x, y, 1, marker='o',color=color_lst)
map.readshapefile('/Users/yan/Downloads/gadm36_TWN_shp/gadm36_TWN_2', 'gadm36_TWN_shp', linewidth=0.25 , drawbounds=True)

plt.title('套房租金分佈圖+北部早午餐分佈圖',fontproperties=font)

cafe_lons = []
cafe_lats = []

# cafe
with open('/Users/yan/Downloads/早午餐.csv', newline='') as cafe_csvfile:
    rows = csv.DictReader(cafe_csvfile)

    for row in rows:
        x = ast.literal_eval(row['geometry'])
        cafe_lons.append(x['location']['lng'])
        cafe_lats.append(x['location']['lat'])
x_cafe, y_cafe = map(cafe_lons, cafe_lats)
map.scatter(x_cafe, y_cafe, 1, marker = '^', color = 'salmon')



plt.show()

