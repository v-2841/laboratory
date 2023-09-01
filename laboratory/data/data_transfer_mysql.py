import os

from datetime import datetime
from dotenv import load_dotenv
import MySQLdb


load_dotenv()
host = os.getenv('DB_HOST', 'localhost')
user = os.getenv('USER', 'django_user')
password = os.getenv('PASSWORD', '')
database = os.getenv('DB', 'laboratory')
db = MySQLdb.connect(host=host, user=user, password=password, database=database)
cursor = db.cursor()
with open('reagents.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        data = line.strip().split('\t')
        for i in range(len(data)):
            if data[i] == '-':
                data[i] = None
            elif i == 3 or i == 4:
                data[i] = datetime.strptime(data[i], "%d.%m.%Y")
        sql_query = "INSERT INTO reagents_reagent (`index`, name, amount, manufacture_date, expiration_date) VALUES (%s, %s, %s, %s, %s);"
        values = (data[0], data[1], data[2], data[3], data[4])
        cursor.execute(sql_query, values)
    db.commit()
cursor.close()
db.close()
