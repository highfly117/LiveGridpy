#!/user
# -*- coding: utf-8 -*-

import csv
import urllib.request
import numpy as np
import matplotlib.pyplot as plt
import plotly as py


py.tools.set_credentials_file(username='highfly117', api_key='2pQvxqeQNhSf07JUc4Nh')


url = 'https://api.bmreports.com/BMRS/FUELINST/v1?APIKey=66ky5jo5p5w0vbd&ServiceType=CSV'
url2 = 'https://api.bmreports.com/BMRS/FUELINSTHHCUR/v1?APIKey=66ky5jo5p5w0vbd&ServiceType=CSV'
response = urllib.request.urlopen(url2)

arr = np.genfromtxt(response,delimiter=",", skip_header=1, skip_footer=2,dtype=str, usecols=(1,2))

n = 0
fueltype = []
gigawatt = []
m = 0
x = []
y = []

while n < len(arr):
    fueltype.append(arr[m][0])
    gigawatt.append(int(arr[m][1]))
    n = n + 1
    m = m + 1

y_pos = np.arange(len(fueltype))

data = [py.graph_objs.Bar(
    x=fueltype,
    y=gigawatt
    )]

plt.bar(y_pos, gigawatt, align='center', alpha=0.5)
plt.xticks(y_pos, fueltype)
plt.ylabel('Gigawatts')
plt.title('fueltype')

plt.show()


