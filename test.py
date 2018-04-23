import csv
import urllib2

url = 'https://api.bmreports.com/BMRS/FUELINST/v1?APIKey=66ky5jo5p5w0vbd&ServiceType=CSV'
url2 = 'https://api.bmreports.com/BMRS/FUELINSTHHCUR/v1?APIKey=66ky5jo5p5w0vbd&ServiceType=CSV'
response = urllib2.urlopen(url)
cr = csv.reader(response)

arr = []

for row in cr:
    arr.append(row)

x = 1

total = 0

while x < (len(arr))-1:
    arrfl = float(arr[x][4])
    total = total + arrfl
    #print 'this is' ,x," ", arrfl
    x = x + 1

print total
print arr[len(arr)-2][4]