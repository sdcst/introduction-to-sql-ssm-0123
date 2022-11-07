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

cursor.execute()




def display():
    query = "select * from Customers"
    cursor.execute(query)
    result = cursor.fetchall()
    for i in result:
        returnvalue = ""
        for x in i:
            returnvalue = returnvalue +" "+ x
        print(returnvalue)


def createnew():
    a1 = input("PET NAME ")
    a2 = input("PET SPECIES ")
    a3 = input("PET BREED ")
    a4 = input("OWNER ")
    a5 = input("OWNER PHONENUMBER ")
    a6 = input("OWNER EMAIL ")
    a7 = input("BALANCE ")
    a8 = input("FIRST VISIT ")
    query = f"insert into Customers(petname, petspecies, petbreed, owner, ownerphonenumber, owneremail, balance, firstvisit) values ('{a1}','{a2}','{a3}','{a4}','{a5}','{a6}','{a7}','{a8}');"
    cursor.execute(query)

display()