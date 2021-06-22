import time

import os
from configparser import ConfigParser

import pyodbc

def getDBConnection():
    
    configParse = ConfigParser()
    configParse.read("config.ini")
    
    # Define the Driver
    __driver = configParse.get("database", "driver") #'{ODBC Driver 17 for SQL Server}'

    #Define Connect String 
    __connectionString = configParse.get("database", "connectionstring") #"Driver={driver};Server=CHANDRADEEP;Database=ContactDB;Integrated Security=True;Trusted_Connection=yes;".format(driver=__driver)
    __connectionString = __connectionString.format(driver=__driver).replace('"', '')
    
    try:
        cnxn: pyodbc.Connection = pyodbc.connect(__connectionString)
    except:
        time.sleep(2)
        cnxn: pyodbc.Connection = pyodbc.connect(__connectionString)

    return cnxn