from jinja2 import Template
from pymysql import connect
import os

with open("./create.sql") as create:
    template = Template(create.read())
query = template.render(database='database')

cursor = connect(
    host=os.getenv("MYSQL_HOST"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    db=os.getenv("MYSQL_DATABASE"),
    charset='utf8mb4'
).cursor()

cursor.execute(query)
cursor.close()