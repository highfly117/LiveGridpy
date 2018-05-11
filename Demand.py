# !/user
# -*- coding: utf-8 -*-

from __future__ import print_function
import urllib.request
import numpy as np
import mysql.connector as mysql
import time as time

from datetime import date, datetime, timedelta


def _getDemand_():
    cnx = mysql.connect(user='root', password='Thereoncewasagirl0', database='powergrid')

    cursor = cnx.cursor()

    tomorrow = datetime.now().date() + timedelta(days=1)

    url = 'https://api.bmreports.com/BMRS/FUELINST/v1?APIKey=66ky5jo5p5w0vbd&ServiceType=CSV'
    url2 = 'https://api.bmreports.com/BMRS/FUELINST/v1?APIKey=66ky5jo5p5w0vbd&FromDateTime=&FromDateTime=2018-05-10 00:00:00&ToDateTime=2018-05-10 023:59:59&ServiceType=CSV'
    response = urllib.request.urlopen(url2)

    arr = np.genfromtxt(response, delimiter=",", skip_header=1, skip_footer=2, dtype=str, usecols=(3,4,5,6,7,8,9,10,11,12,13,14,15,16,17))


    n = 0

    m = 0


    #Clean_table = ("TRUNCATE TABLE fueltypedemand")
    #cursor.execute(Clean_table)
    #cnx.commit()

    while n < len(arr) - 1:
        cnx = mysql.connect(user='root', password='Thereoncewasagirl0', database='powergrid')
        cursor = cnx.cursor()



        idfueltype = cursor.lastrowid

        add_fueltype = ("INSERT INTO fueltypedemand"
                        "(DemandID, Time_Date, CCGT, OIL, COAL, NUCLEAR, WIND, PS, NPSHYDl, OCGT, OTHER, INTFR, INTIRL, INTNED , INTEW, BIOMASS)"
                        "VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")


        fueltype_data = (idfueltype, int(arr[m][0]), int(arr[m][1]), int(arr[m][2]), int(arr[m][3]), int(arr[m][4]), int(arr[m][5]), int(arr[m][6]), int(arr[m][7]), int(arr[m][8]), int(arr[m][9]), int(arr[m][10]), int(arr[m][11]), int(arr[m][12]), int(arr[m][13]), int(arr[m][14]))
        m = m + 1

        cursor.execute(add_fueltype, fueltype_data)

        cnx.commit()

    cursor.close()
    cnx.close()



_getDemand_()

# starttime = time.time()
# while True:
#     _getDemand_()
#     time.sleep(60.0 - ((time.time() - starttime) % 60))
