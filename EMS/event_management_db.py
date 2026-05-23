# Importing module 
import mysql.connector
from flask import Flask, request, render_template

app = Flask(__name__)

# Creating connection object
event_db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "cool",
    port=3307,
    database = "event_db"

)

cursor = event_db.cursor()

# Printing the connection object 
print(event_db)



@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    print('successs')
    username = request.form['username']
    password = request.form['password']
    
    # Add your authentication logic here
    return f'Username: {username}, Password: {password}'

if __name__ == '__main__':
    app.run(debug=True)
