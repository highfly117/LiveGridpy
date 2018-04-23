#!/user
# -*- coding: utf-8 -*-

import csv
import urllib2
import numpy as np
import matplotlib.pyplot as plt
import plotly.plotly as py


url = 'https://api.bmreports.com/BMRS/FUELINST/v1?APIKey=66ky5jo5p5w0vbd&ServiceType=CSV'
url2 = 'https://api.bmreports.com/BMRS/FUELINSTHHCUR/v1?APIKey=66ky5jo5p5w0vbd&ServiceType=CSV'
response = urllib2.urlopen(url2)
cr = csv.reader(response)


arr = np.genfromtxt(response,delimiter=",", skip_header=1, skip_footer=2,dtype=None)



y = arr[0][2]
N = 12000
x = range(N)
width = 1/1.5
plt.bar(x, y, width, color="blue")


fig = plt.gcf()
plot_url = py.plot_mpl(fig, filename='mpl-basic-bar')

