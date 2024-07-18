from mysql import connector

mysql_connection = connector.connect(
    host='localhost',
    user='root',
    password='Secret_123',
    database='banking'
)

cursor = mysql_connection.cursor()
cursor.execute("""
delete from accounts
where status = 'CLOSED' or status = 'BLOCKED'
""")
mysql_connection.commit()
print(f"{cursor.rowcount} rows removed!")