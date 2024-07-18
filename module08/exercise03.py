"""
mysql> create database banking;
Query OK, 1 row affected (0.00 sec)

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| banking            |
| bookshelf          |
| hrdb               |
| imdb               |
| information_schema |
| mysql              |
| performance_schema |
| sys                |
| test               |
| work               |
| world              |
+--------------------+
11 rows in set (0.00 sec)

mysql> use banking;
Database changed
mysql> show tables;
Empty set (0.00 sec)
"""
from mysql import connector

mysql_connection = connector.connect(
    host='localhost',
    user='root',
    password='Secret_123',
    database='banking'
)

cursor = mysql_connection.cursor()
cursor.execute("""
create table accounts(
    iban varchar(52) primary key,
    balance float default 10000.0,
    status enum('ACTIVE','BLOCKED','CLOSED') default 'ACTIVE'
)
""")

"""
mysql> show tables;
+-------------------+
| Tables_in_banking |
+-------------------+
| accounts          |
+-------------------+
1 row in set (0.00 sec)

mysql> desc accounts;
+---------+-----------------------------------+------+-----+---------+-------+
| Field   | Type                              | Null | Key | Default | Extra |
+---------+-----------------------------------+------+-----+---------+-------+
| iban    | varchar(52)                       | NO   | PRI | NULL    |       |
| balance | float                             | YES  |     | 10000   |       |
| status  | enum('ACTIVE','BLOCKED','CLOSED') | YES  |     | ACTIVE  |       |
+---------+-----------------------------------+------+-----+---------+-------+
3 rows in set (0.00 sec)
"""
