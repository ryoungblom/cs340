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
def browse_char():
    print("Fetching and rendering people web page")
    db_connection = connect_to_database()
    query = "SELECT fname, lname, nobility, gender, age, house, religion from got_characters;"
    result = execute_query(db_connection, query).fetchall();
    print(result)
    return render_template('characters.html', rows=result)

@webapp.route('/skills')
#the name of this function is just a cosmetic thing
def browse_skills():
    print("Fetching and rendering skills web page")
    db_connection = connect_to_database()
    query = "SELECT name, battle_utility, acquisition_cost, rarity, value from got_skills;"
    result = execute_query(db_connection, query).fetchall();
    print(result)
    return render_template('skills.html', rows=result)

@webapp.route('/houses')
#the name of this function is just a cosmetic thing
def browse_houses():
    print("Fetching and rendering houses web page")
    db_connection = connect_to_database()
    query = "SELECT name, members, motto, sigil, leader from got_houses;"
    result = execute_query(db_connection, query).fetchall();
    print(result)
    return render_template('houses.html', rows=result)

@webapp.route('/religions')
#the name of this function is just a cosmetic thing
def browse_religions():
    print("Fetching and rendering religions web page")
    db_connection = connect_to_database()
    query = "SELECT name, worshipers, theism, age, symbol from got_religions;"
    result = execute_query(db_connection, query).fetchall();
    print(result)
    return render_template('religions.html', rows=result)

@webapp.route('/')
def home():
    return render_template('index.html')

@webapp.route('/index.html')
def homIndexe():
    return render_template('index.html')


@webapp.route('/add_character', methods=['POST','GET'])
def add_character():
    db_connection = connect_to_database()

        request.method == 'POST':
        print("Adding Character!");
        fname = request.form['fname']
        lname = request.form['lname']
        nobility = request.form['nobility']
        gender = request.form['gender']
        age = request.form['age']
        house = request.form['house']
        religion = request.form['religion']


        query = 'INSERT INTO got_characters (fname, lname, nobility, gender, age, house, religion) VALUES (%s,%s,%s,%s,%s,%s,%s)'
        data = (fname, lname, nobility, gender, age, house, religion)
        execute_query(db_connection, query, data)
        return ('Character added!');




@webapp.route('/add_character_backup', methods=['POST','GET'])
def add_character_backup():
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
