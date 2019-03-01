from flask import Flask, render_template
from flask import request
from db_connector.db_connector import connect_to_database, execute_query
#create the web application
webapp = Flask(__name__)

#provide a route where requests on the web application can be addressed
@webapp.route('/hello')
#provide a view (fancy name for a function) which responds to any requests on this route
def hello():
    return "Hello World!";

@webapp.route('/characters')
#the name of this function is just a cosmetic thing
def browse_people():
    print("Fetching and rendering people web page")
    db_connection = connect_to_database()
    query = "SELECT fname, lname, nobility, gender, age, house, religion from got_characters;"
    result = execute_query(db_connection, query).fetchall();
    print(result)
    return render_template('characters.html', rows=result)

@webapp.route('/skills')
#the name of this function is just a cosmetic thing
def browse_people():
    print("Fetching and rendering skills web page")
    db_connection = connect_to_database()
    query = "SELECT name, battle_utility, acquisition_cost, rarity, value from got_skills;"
    result = execute_query(db_connection, query).fetchall();
    print(result)
    return render_template('skills.html', rows=result)

@webapp.route('/religions')
#the name of this function is just a cosmetic thing
def browse_people():
    print("Fetching and rendering religions web page")
    db_connection = connect_to_database()
    query = "SELECT name, worshippers, theism, age, symbol from got_religions;"
    result = execute_query(db_connection, query).fetchall();
    print(result)
    return render_template('religions.html', rows=result)

@webapp.route('/')
def home():
    return render_template('index.html')

@webapp.route('/add_new_people', methods=['POST','GET'])
def add_new_people():
    db_connection = connect_to_database()
    if request.method == 'GET':
        query = 'SELECT planet_id, name from bsg_planets'
        result = execute_query(db_connection, query).fetchall();
        print(result)

        return render_template('people_add_new.html', planets = result)
    elif request.method == 'POST':
        print("Add new people!");
        fname = request.form['fname']
        lname = request.form['lname']
        age = request.form['age']
        homeworld = request.form['homeworld']

        query = 'INSERT INTO bsg_people (fname, lname, age, homeworld) VALUES (%s,%s,%s,%s)'
        data = (fname, lname, age, homeworld)
        execute_query(db_connection, query, data)
        return ('Person added!');
