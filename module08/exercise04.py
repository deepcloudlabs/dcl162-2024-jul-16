from mysql import connector

mysql_connection = connector.connect(
    host='localhost',
    user='root',
    password='Secret_123',
    database='banking'
)

cursor = mysql_connection.cursor()
accounts = [
    ("tr1",10_000,'ACTIVE')
]