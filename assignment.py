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
DROP TABLE IF EXISTS Customers;

CREATE TABLE Customers(
id INTEGER PRIMARY KEY AUTOINCREMENT,
petname TEXT,
petspecies TEXT, 
pet breed TEXT,
department TEXT,
position TEXT,
hireDate TEXT);

INSERT INTO Customers(name, salary, department, position, hireDate) VALUES('Dave', 300, 'Marketing', 'LV1', '2020-01-01');
INSERT INTO Customers(name, salary, department, position, hireDate) VALUES('Clara', 420, 'Sales', 'LV2', '2018-01-11');
INSERT INTO Customers(id, name, salary, department, position, hireDate) VALUES(3, 'Jane', 620, 'Developer', 'LV4', '2015-11-01');
INSERT INTO Customers VALUES(4, 'Peter', 530, 'Developer', 'LV2', '2020-11-01'); 
"""



cursor.execute('CREATE Customers; pet name, pet species, pet breed, owner name, owner phone number, owner email, owner balance, date of first visit')

