from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
from bcrypt import *
import MySQLdb.cursors
import re


app = Flask(__name__)
app.config['SESSION_TYPE'] = 'memcached'
app.secrete_key = '1l0v3sh3an0r3'
#sess = session(    )

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'faceAuthentication'

mysql = MySQL(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/Login', methods=['GET', 'POST'])
def login():
    msg = ''
    #crete variables if the username, password are in the form and the request is post.
    if request.method == 'POST' and 'Email' in request.form and 'Password' in request.form:
        Email = request.form['Email']
        Password = request.form['Password']
        #check if the username and the password match the details in the msql table
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM Users WHERE Email = %s and Password = %s', (Email, Password))
        #fetch the record and return the results
        account = cursor.fetchone()
        if account:
            return redirect(url_for('home'))

        else:
            msg = 'Incorect email or password'
            return redirect(url_for('login'))

    return render_template('login.html', msg='')

def logout():
    return redirect(url_for('login'))

@app.route('/signup', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        formDetails = request.form
        Email = formDetails['Email']
        Username = formDetails['Username']
        Password = formDetails['Password']
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO Users(Email, Username, Password) VALUES(%s, %s, %s)", (Email, Username, Password))
        mysql.connection.commit()
        cursor.close()
        while True:
            return redirect(url_for('login'))
    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True)
