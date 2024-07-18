from mysql import connector

mysql_connection = connector.connect(
    host='localhost',
    user='root',
    password='Secret_123',
    database='banking'
)

cursor = mysql_connection.cursor()
accounts = [
    ("tr1", 10_000, 'ACTIVE'),
    ("tr2", 20_000, 'ACTIVE'),
    ("tr3", 30_000, 'CLOSED'),
    ("tr4", 40_000, 'BLOCKED'),
    ("tr5", 50_000, 'ACTIVE'),
    ("tr6", 60_000, 'CLOSED'),
    ("tr7", 70_000, 'ACTIVE'),
    ("tr8", 90_000, 'BLOCKED')
]
for iban, balance, status in accounts:
    cursor.execute(f"insert into accounts values ('{iban}',{balance},'{status}')")
mysql_connection.commit()
