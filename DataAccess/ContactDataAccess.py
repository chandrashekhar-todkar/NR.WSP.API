import logging
import pyodbc

import datetime

from DataAccess.DBConnection import getDBConnection
from DataAccess.CursorByName import CursorByName

class ContactDataAccess:
    
    def getContacts(self):

        #get DB connection
        __cnxn = getDBConnection()

        try:
            #Define the select Query
            __selectQuery = "Select * From [dbo].[Contacts]"

            #Create the Cursor object
            __cursor = pyodbc.Cursor = __cnxn.cursor()

            #Execute the Query
            __cursor.execute(__selectQuery)

            #Fetch records
            __records = list()
            for row in CursorByName(__cursor):
                __records.append(row)

        finally:    
            #close connection
            __cnxn.close()

        return __records          

    def addContact(self, contact):
        #get DB connection
        __cnxn = getDBConnection()

        try:
            #Define the Insert Query
            __insertQuery = "INSERT INTO [dbo].[Contacts] ([FirstName], [LastName] ,[Email] ,[PhoneNumber] ,[Status] ,[DateUpdated]) VALUES (?, ?, ?, ?, ?,?)"

            #set Values
            __values = [contact.FirstName, contact.LastName, contact.Email, contact.PhoneNumber, contact.Status, datetime.datetime.now()]  

            #Create the Cursor object
            __cursor = pyodbc.Cursor = __cnxn.cursor()

            #Execute the Query
            __cursor.execute(__insertQuery, __values)
   
            #Commiting any pending transaction to the database.    
            __cnxn.commit()    
            
        finally:    
            #close connection
            __cnxn.close()

        return {
            "success" : True,
            "messages" : [{"type" : "information", "message" : "Contact added successful."}]
        }

    def updateContact(self, contact):
        #get DB connection
        __cnxn = getDBConnection()

        try:
            #Define the Update Query
            __updateQuery = "UPDATE [dbo].[Contacts] SET [FirstName] = ?, [LastName] = ?, [Email] = ?, [PhoneNumber] = ?, [Status] = ?, [DateUpdated] = ? WHERE ID = ?"

            #set Values
            __values = [contact.FirstName, contact.LastName, contact.Email, contact.PhoneNumber, contact.Status, datetime.datetime.now(), contact.Id]  

            #Create the Cursor object
            __cursor = pyodbc.Cursor = __cnxn.cursor()

            #Execute the Query
            __cursor.execute(__updateQuery, __values)

            #Commiting any pending transaction to the database.    
            __cnxn.commit()    
            
        finally:    
            #close connection
            __cnxn.close()

        return {
            "success" : True,
            "messages" : [{"type" : "information", "message" : "Contact updated successful."}]
        }

            
    def deleteContact(self, contactId):
        #get DB connection
        __cnxn = getDBConnection()

        try:
            #Define the Delete Query
            __deleteQuery = "DELETE FROM [dbo].[Contacts]  WHERE ID = ?"

            #set Values
            __values = [contactId]  

            #Create the Cursor object
            __cursor = pyodbc.Cursor = __cnxn.cursor()

            #Execute the Query
            __cursor.execute(__deleteQuery, __values)

            #Commiting any pending transaction to the database.    
            __cnxn.commit()    
            
        finally:    
            #close connection
            __cnxn.close()

        return {
            "success" : True,
            "messages" : [{"type" : "information", "message" : "Contact delete successful."}]
        }