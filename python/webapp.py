from flask import Flask, render_template, redirect
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
    query = "SELECT C.fname, C.lname, C.nobility, C.gender, C.age, H.name AS 'House', R.name AS 'Religion', C.id FROM got_characters C LEFT JOIN got_houses H ON C.house = H.id LEFT JOIN got_religions R ON C.religion = R.id;"
    result = execute_query(db_connection, query).fetchall();

    query = 'SELECT id, name FROM got_houses'
    hresult = execute_query(db_connection, query).fetchall();

    query = 'SELECT id, name FROM got_religions'
    rresult = execute_query(db_connection, query).fetchall();

    return render_template('characters.html', rows=result, houses = hresult, religions = rresult)

@webapp.route('/skills')
#the name of this function is just a cosmetic thing
def browse_skills():
    print("Fetching and rendering skills web page")
    db_connection = connect_to_database()
    query = "SELECT name, battle_utility, acquisition_cost, rarity, value FROM got_skills;"
    result = execute_query(db_connection, query).fetchall();
    return render_template('skills.html', rows=result)

@webapp.route('/houses')
#the name of this function is just a cosmetic thing
def browse_houses():
    print("Fetching and rendering houses web page")
    db_connection = connect_to_database()
    query = "SELECT H.name, H.members, H.motto, H.sigil, CONCAT(C.fname, ' ', C.lname) AS 'Leader' FROM got_houses H LEFT JOIN got_characters C ON H.leader = C.id;"
    result = execute_query(db_connection, query).fetchall();

    query = 'SELECT id, fname, lname FROM got_characters;'
    lresult = execute_query(db_connection, query).fetchall();
    return render_template('houses.html', rows=result, leaders=lresult)

@webapp.route('/religions')
#the name of this function is just a cosmetic thing
def browse_religions():
    print("Fetching and rendering religions web page")
    db_connection = connect_to_database()
    query = "SELECT name, worshipers, theism, age, symbol, id FROM got_religions;"
    result = execute_query(db_connection, query).fetchall();
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
    request.method == 'POST';
    print("Adding Character!");
    fname = request.form['fname']
    lname = request.form['lname']
    nobility = request.form['nobility']
    gender = request.form['gender']
    age = request.form['age']
    house = request.form['house']
    religion = request.form['religion']

    query = 'INSERT INTO got_characters (fname, lname, nobility, gender, age, house, religion) VALUES (%s,%s,%s,%s,%s,%s,%s);'
    data = (fname, lname, nobility, gender, age, house, religion)

    execute_query(db_connection, query, data)
    return redirect ('/characters');

@webapp.route('/add_house', methods=['POST','GET'])
def add_house():
    db_connection = connect_to_database()
    request.method == 'POST';
    print("Adding House!");
    name = request.form['addName']
    members = request.form['addMembers']
    motto = request.form['addMotto']
    sigil = request.form['addSigil']
    leader = request.form['addLeader']

    query = 'INSERT INTO got_houses (name, members, motto, sigil, leader) VALUES (%s, %s, %s, %s, %s);'
    data = (name, members, motto, sigil, leader)

    execute_query(db_connection, query, data)
    return redirect ('/houses');

@webapp.route('/add_skill', methods=['POST','GET'])
def add_skill():
    db_connection = connect_to_database()
    request.method == 'POST';
    print("Adding Skill!");
    name = request.form['addName']
    utility = request.form['addUtility']
    cost = request.form['addCost']
    rarity = request.form['addRarity']
    value = request.form['addValue']

    query = 'INSERT INTO got_skills (name, battle_utility, acquisition_cost, rarity, value) VALUES (%s, %s, %s, %s, %s);'
    data = (name, utility, cost, rarity, value)

    execute_query(db_connection, query, data)
    return redirect ('/skills');

@webapp.route('/add_religion', methods=['POST','GET'])
def add_religion():
    db_connection = connect_to_database()
    request.method == 'POST';
    print("Adding Religion!");
    name = request.form['addName']
    worshipers = request.form['addWorshipers']
    theism = request.form['addTheism']
    age = request.form['addAge']
    symbol = request.form['addSymbol']

    query = 'INSERT INTO got_religions (name, worshipers, theism, age, symbol) VALUES (%s, %s, %s, %s, %s);'
    data = (name, worshipers, theism, age, symbol)

    execute_query(db_connection, query, data)
    return redirect ('/religions');


@webapp.route ('/delete_character/<int:id>')
def delete_characters(id):
    db_connection = connect_to_database()
    query = "DELETE FROM got_characters WHERE id = %s"
    data = (id,)

    result = execute_query(db_connection, query, data)
    return redirect ('/characters');


@webapp.route ('/delete_religions/<int:id>')
def delete_religions(id):
    db_connection = connect_to_database()
    query = "DELETE FROM got_religions WHERE id = %s"
    data = (id,)

    result = execute_query(db_connection, query, data)
    return redirect ('/religions');


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
