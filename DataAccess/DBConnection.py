import time

from configparser import ConfigParser

import pyodbc

def getDBConnection():
    
    configParse = ConfigParser()
    configParse.read("config.ini")
    
    # Define the Driver
    __driver = configParse.get("database", "driver")

    #Define Connect String 
    __connectionString = configParse.get("database", "connectionstring") 
    __connectionString = __connectionString.format(driver=__driver)
    
    try:
        cnxn: pyodbc.Connection = pyodbc.connect(__connectionString)
    except:
        time.sleep(2)
        cnxn: pyodbc.Connection = pyodbc.connect(__connectionString)

    return cnxn