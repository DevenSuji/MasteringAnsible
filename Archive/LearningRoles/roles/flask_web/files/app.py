import os
from flask import Flask
from flaskext.mysql import MySQL      # For newer versions of flask-mysql
# from flask.ext.mysql import MySQL   # For older versions of flask-mysql
app = Flask(__name__)

mysql = MySQL()

mysql_database_host = 'MYSQL_DATABASE_HOST' in os.environ and os.environ[
    'MYSQL_DATABASE_HOST'] or 'localhost'

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'db_user'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Passw0rd'
app.config['MYSQL_DATABASE_DB'] = 'employee_db'
app.config['MYSQL_DATABASE_HOST'] = mysql_database_host
mysql.init_app(app)

conn = mysql.connect()

cursor = conn.cursor()


@app.route("/")
def main():
    return "Keep a constant note of where you were 10 years ago, where you are now, and where you are supposed to be in another 5 years. Learn from your experiences. At one point of time you just had 1 Rupee Note with you. No money to buy food. Imagine where you are now. There is a very long and exciting journey awaiting for you, hence just keep learning"


@app.route('/how are you')
def hello():
    return 'I am good, how about you?'


@app.route('/read from database')
def read():
    cursor.execute("SELECT * FROM employees")
    row = cursor.fetchone()
    result = []
    while row is not None:
        result.append(row[0])
        row = cursor.fetchone()

    return ",".join(result)


if __name__ == "__main__":
    app.run()
