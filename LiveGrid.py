# !/user
# -*- coding: utf-8 -*-

from __future__ import print_function
import urllib.request
import numpy as np
import mysql.connector as mysql
import time as time

from datetime import date, datetime, timedelta


def _getDemand_():
    #cnx = mysql.connect(user='root', password='girl', database='powergrid')
    cnx = mysql.connect(user="root", password=, host="servername", port=3306, database="powergirddb", ssl_verify_cert=true)

    cursor = cnx.cursor()

    tomorrow = datetime.now().date() + timedelta(days=1)

    url = 'https://api.bmreports.com/BMRS/FUELINST/v1?APIKey=66ky5jo5p5w0vbd&ServiceType=CSV'
    url2 = 'https://api.bmreports.com/BMRS/FUELINSTHHCUR/v1?APIKey=66ky5jo5p5w0vbd&ServiceType=CSV'
    response = urllib.request.urlopen(url2)

    arr = np.genfromtxt(response, delimiter=",", skip_header=1, skip_footer=2, dtype=str, usecols=(1, 2))

    n = 0
    fueltype = []
    gigawatt = []
    m = 0
    x = []
    y = []

    #Clean_table = ("TRUNCATE TABLE fueltype")
    #cursor.execute(Clean_table)

    while n < len(arr) - 1:
        cnx = mysql.connect(user='root', password='Thereoncewasagirl0', database='powergrid')
        cursor = cnx.cursor()

        fueltype.append(arr[m][0])
        gigawatt.append(int(arr[m][1]))


        idfueltype = cursor.lastrowid

        add_fueltype = ("INSERT INTO fueltype"
                        "(idfueltype, fueltypecol, demand)"
                        "VALUES(%s, %s, %s)")

        fueltype_data = (idfueltype, arr[m][0], int(arr[m][1]))
        n = n + 1
        m = m + 1

        cursor.execute(add_fueltype, fueltype_data)

        cnx.commit()

    cursor.close()
    cnx.close()
    print(m)

print(quit)

_getDemand_


