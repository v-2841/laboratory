import datetime
import os
from random import uniform

from datetime import datetime
from dotenv import load_dotenv
import psycopg2


load_dotenv()
host = os.getenv('DB_HOST', 'localhost')
port = os.getenv('DB_PORT', 5432)
user = os.getenv('POSTGRES_USER', 'django_user')
password = os.getenv('POSTGRES_PASSWORD', '')
database = os.getenv('POSTGRES_DB', 'laboratory')
db = psycopg2.connect(
    dbname=database,
    user=user,
    password=password,
    host=host,
    port=port,
)
cursor = db.cursor()
for i in range(20):
    sample_name = f'1/{i}'
    analysis_name = 'Массовая доля йода'
    standard = 'ГОСТ Р 51575'
    measurement_unit = 'г/кг'
    result = str(round(uniform(0.020, 0.050), 3))
    is_processed = 'false'
    pub_date = datetime.now()
    researcher_id = 1
    sql_query = "INSERT INTO results_result (sample_name, analysis_name, standard, measurement_unit, result, is_processed, pub_date, researcher_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"
    values = (sample_name, analysis_name, standard, measurement_unit, result, is_processed, pub_date, researcher_id)
    cursor.execute(sql_query, values)
db.commit()
cursor.close()
db.close()
