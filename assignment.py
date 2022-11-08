#!python

"""
Create a program that will store the database for a veterinary
Each record needs to have the following information:
id unique integer identifier
pet name
pet species (cat, bird, dog, etc)
pet breed (persian, beagle, canary, etc)
owner name
owner phone number
owner email
owner balance (amount owing)
date of first visit

create a program that will allow the user to:
insert a new record into the database and save it automatically
retrieve a record by their id and display all of the information
retrieve a record by the email and display all of the information
retrieve a record by phone number and display all of the information

You will need to create the table yourself. Consider what data types you will
need to use.
"""

import sqlite3

file = 'dbdb.db'
connection = sqlite3.connect(file)

cursor = connection.cursor()

Tempscript = """

create table if not exists Customers(
id int not null unique,
petname TEXT,
petspecies TEXT, 
petbreed TEXT,
owner TEXT,
ownerphonenumber TEXT,
owneremail TEXT,
balance TEXT,
firstvisit TEXT);
"""

trying = """
INSERT INTO Customers(petname, petspecies, petbreed, owner, ownerphonenumber, owneremail, balance, firstvisit) VALUES('PET1', 'CAT', 'PERSIAN', 'YANG', '778-220-2300', 'YANG@GMAIL.COM', '$292', '2022-03-01');
"""

cursor.execute(Tempscript)



def display():
    query = "select * from Customers"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.execute(query)
    result = cursor.fetchall()
    returnvalue = ""
    for i in result:
        for x in i:
            if type(x) == int:
                x = str(x)
            returnvalue = returnvalue +" "+ x
        print(returnvalue)

def findbyid():
    keyword = input("Find by id")
    query = f"""
    SELECT * FROM Customers
    WHERE id LIKE {keyword}
    
    """     
    cursor.execute(query)
    result = cursor.fetchall()
    for i in result:
        returnvalue = ""
        for x in i:
            if type(x) == int:
                x = str(x)
            returnvalue = returnvalue +" "+ x
        print(returnvalue)

def findbyemail():
    keyword = input("Find by email")
    query = f"""
    SELECT * FROM Customers
    WHERE owneremail LIKE '{keyword}'
    
    """     
    cursor.execute(query)
    result = cursor.fetchall()
    for i in result:
        returnvalue = ""
        for x in i:
            if type(x) == int:
                x = str(x)
            returnvalue = returnvalue +" "+ x
        print(returnvalue)

def findbyphone():
    keyword = input("Find by phone number")
    query = f"""
    SELECT * FROM Customers
    WHERE ownerphonenumber LIKE {keyword}
    
    """     
    cursor.execute(query)
    result = cursor.fetchall()
    for i in result:
        returnvalue = ""
        for x in i:
            if type(x) == int:
                x = str(x)
            returnvalue = returnvalue +" "+ x
        print(returnvalue)

def createnew():
    query = "select id from Customers"
    cursor.execute(query)
    result = cursor.fetchall()
    idid = len(result) + 1
    a1 = input("PET NAME ")
    a2 = input("PET SPECIES ")
    a3 = input("PET BREED ")
    a4 = input("OWNER ")
    a5 = input("OWNER PHONENUMBER ")
    a6 = input("OWNER EMAIL ")
    a7 = input("BALANCE ")
    a8 = input("FIRST VISIT ")
    query = f"insert into Customers(id, petname, petspecies, petbreed, owner, ownerphonenumber, owneremail, balance, firstvisit) values ({idid},'{a1}','{a2}','{a3}','{a4}','{a5}','{a6}','{a7}','{a8}');"
    cursor.execute(query)
    connection.commit()


