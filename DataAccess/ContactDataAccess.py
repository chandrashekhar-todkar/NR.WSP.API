import logging
import pyodbc

import datetime

from DataAccess.DBConnection import getDBConnection

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
            #__records = [dict((__cursor.description[i][0], value) \
            #   for i, value in enumerate(row)) for row in __cursor.fetchall()]
            __records = list(__cursor.fetchall())

        finally:    
            #close connection
            __cnxn.close()

        #return (__records[0] if __records else None)
        #clean up the recordset
        __records = [tuple(record) for record in __records]
        
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