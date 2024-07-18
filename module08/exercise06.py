from mysql import connector

mysql_connection = connector.connect(
    host='localhost',
    user='root',
    password='Secret_123',
    database='banking'
)

cursor = mysql_connection.cursor()
cursor.execute("""
update accounts 
set balance = balance - 500 
where status = 'ACTIVE'
""")
mysql_connection.commit()
print(f"{cursor.rowcount} rows updated!")