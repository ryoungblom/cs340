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

    query = 'SELECT id, name FROM got_skills'
    sresult = execute_query(db_connection, query).fetchall();

    return render_template('characters.html', rows=result, houses = hresult, religions = rresult, skillRows = sresult)


@webapp.route('/nobility', methods=['POST','GET'])
#the name of this function is just a cosmetic thing
def nobility():
    print("Fetching and rendering people web page")


    db_connection = connect_to_database()

    request.method == 'POST';

    nbl = request.form['explNob'];

    query = "SELECT C.fname, C.lname, C.nobility, C.gender, C.age, H.name AS 'House', R.name AS 'Religion', C.id FROM got_characters C LEFT JOIN got_houses H ON C.house = H.id LEFT JOIN got_religions R ON C.religion = R.id WHERE C.nobility = %s;"

    data = (nbl,);

    result = execute_query(db_connection, query, data).fetchall();

    query = 'SELECT id, name FROM got_houses'
    hresult = execute_query(db_connection, query).fetchall();

    query = 'SELECT id, name FROM got_religions'
    rresult = execute_query(db_connection, query).fetchall();

    query = 'SELECT id, name FROM got_skills'
    sresult = execute_query(db_connection, query).fetchall();

    return render_template('nobility.html', rows=result, houses = hresult, religions = rresult, skillRows = sresult)


@webapp.route('/gender', methods=['POST','GET'])
#the name of this function is just a cosmetic thing
def gender():
    print("Fetching and rendering people web page")


    db_connection = connect_to_database()

    request.method == 'POST';

    gen = request.form['explGen'];

    query = "SELECT C.fname, C.lname, C.nobility, C.gender, C.age, H.name AS 'House', R.name AS 'Religion', C.id FROM got_characters C LEFT JOIN got_houses H ON C.house = H.id LEFT JOIN got_religions R ON C.religion = R.id WHERE C.gender = %s;"

    data = (gen,);

    result = execute_query(db_connection, query, data).fetchall();

    query = 'SELECT id, name FROM got_houses'
    hresult = execute_query(db_connection, query).fetchall();

    query = 'SELECT id, name FROM got_religions'
    rresult = execute_query(db_connection, query).fetchall();

    query = 'SELECT id, name FROM got_skills'
    sresult = execute_query(db_connection, query).fetchall();

    return render_template('gender.html', rows=result, houses = hresult, religions = rresult, skillRows = sresult)




@webapp.route('/hMember', methods=['POST','GET'])
#the name of this function is just a cosmetic thing
def hMember():
    print("Fetching and rendering people web page")


    db_connection = connect_to_database()

    request.method == 'POST';

    hm = request.form['explH'];

    query = "SELECT C.fname, C.lname, C.nobility, C.gender, C.age, H.name AS 'House', R.name AS 'Religion', C.id FROM got_characters C LEFT JOIN got_houses H ON C.house = H.id LEFT JOIN got_religions R ON C.religion = R.id WHERE H.name = %s;"

    data = (hm,);

    result = execute_query(db_connection, query, data).fetchall();

    query = 'SELECT id, name FROM got_houses'
    hresult = execute_query(db_connection, query).fetchall();

    query = 'SELECT id, name FROM got_religions'
    rresult = execute_query(db_connection, query).fetchall();

    query = 'SELECT id, name FROM got_skills'
    sresult = execute_query(db_connection, query).fetchall();

    return render_template('hmember.html', rows=result, houses = hresult, religions = rresult, skillRows = sresult)


@webapp.route('/skills')
#the name of this function is just a cosmetic thing
def browse_skills():
    print("Fetching and rendering skills web page")
    db_connection = connect_to_database()
    query = "SELECT name, battle_utility, acquisition_cost, rarity, value, id FROM got_skills;"
    result = execute_query(db_connection, query).fetchall();

    query = "SELECT id, fname, lname FROM got_characters;"
    cresult = execute_query(db_connection, query).fetchall();

    return render_template('skills.html', rows=result, characterRows = cresult)

@webapp.route('/houses')
#the name of this function is just a cosmetic thing
def browse_houses():
    print("Fetching and rendering houses web page")
    db_connection = connect_to_database()
    query = "SELECT H.name, H.members, H.motto, H.sigil, CONCAT(C.fname, ' ', C.lname) AS 'Leader', H.id FROM got_houses H LEFT JOIN got_characters C ON H.leader = C.id;"
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

    #check to see if house or religion inputs contained NULL
    if house == "NULL" and religion == "NULL":
        query = "INSERT INTO got_characters (fname, lname, nobility, gender, age) VALUES (%s,%s,%s,%s,%s);"
        data = (fname, lname, nobility, gender, age)
    elif house == "NULL":
        query = "INSERT INTO got_characters (fname, lname, nobility, gender, age, religion) VALUES (%s,%s,%s,%s,%s,%s);"
        data = (fname, lname, nobility, gender, age, religion)
    elif religion == "NULL":
        query = "INSERT INTO got_characters (fname, lname, nobility, gender, age, house) VALUES (%s,%s,%s,%s,%s,%s);"
        data = (fname, lname, nobility, gender, age, house)
    else:
        query = "INSERT INTO got_characters (fname, lname, nobility, gender, age, house, religion) VALUES (%s,%s,%s,%s,%s,%s,%s);"
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

    #check to see if leader input contains NULL
    if leader == "NULL":
        query = "INSERT INTO got_houses (name, members, motto, sigil) VALUES (%s, %s, %s, %s);"
        data = (name, members, motto, sigil)
    else:
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


@webapp.route ('/edit_character', methods=['POST','GET'])
def edit_characters():

    print("Fetching and rendering characters web page")
    db_connection = connect_to_database()
    query = "SELECT C.fname, C.lname, C.nobility, C.gender, C.age, H.name AS 'House', R.name AS 'Religion', C.id FROM got_characters C LEFT JOIN got_houses H ON C.house = H.id LEFT JOIN got_religions R ON C.religion = R.id;"
    result = execute_query(db_connection, query).fetchall();
    print(result)

    id = request.form['editCharacter']

    query = "SELECT id, fname, lname, nobility, gender, age, house, religion FROM got_characters WHERE id = %s;"
    data = (id,)
    sresult = execute_query(db_connection, query, data).fetchone();
    print(result)

    query = 'SELECT id, name FROM got_houses'
    hresult = execute_query(db_connection, query).fetchall();
    print(result)

    query = 'SELECT id, name FROM got_religions'
    rresult = execute_query(db_connection, query).fetchall();
    print(rresult)


    return render_template('update_characters.html', rows=result, editChar = sresult, houses = hresult, religions = rresult);



@webapp.route('/update_character/<int:id>', methods=['POST'])
def update_character(id):
    db_connection = connect_to_database()
    request.method == 'POST';
    print("Updating Character!");
    fname = request.form['fname']
    lname = request.form['lname']
    nobility = request.form['nobility']
    gender = request.form['gender']
    age = request.form['age']
    house = request.form['house']
    religion = request.form['religion']

    #check if the house or religions input contained NULL
    if house == "NULL" and religion == "NULL":
        query = "UPDATE got_characters SET fname = %s, lname = %s, nobility = %s, gender = %s, age = %s, house = NULL, religion = NULL WHERE id = %s;"
        data = (fname, lname, nobility, gender, age, id)
    elif house == "NULL":
        query = "UPDATE got_characters SET fname = %s, lname = %s, nobility = %s, gender = %s, age = %s, house = NULL, religion = %s WHERE id = %s;"
        data = (fname, lname, nobility, gender, age, religion, id)
    elif religion == "NULL":
        query = "UPDATE got_characters SET fname = %s, lname = %s, nobility = %s, gender = %s, age = %s, house = %s, religion = NULL WHERE id = %s;"
        data = (fname, lname, nobility, gender, age, house, id)
    else:
        query = 'UPDATE got_characters SET fname = %s, lname = %s, nobility = %s, gender = %s, age = %s, house = %s, religion = %s WHERE id = %s'
        data = (fname, lname, nobility, gender, age, house, religion, id)

    execute_query(db_connection, query, data)
    return redirect ('/characters');

@webapp.route ('/edit_house', methods=['POST', 'GET'])
def edit_houses():

    print("Fetching and rendering houses web page")
    db_connection = connect_to_database()
    query = "SELECT H.name, H.members, H.motto, H.sigil, CONCAT(C.fname, ' ', C.lname) AS 'Leader', H.id FROM got_houses H LEFT JOIN got_characters C ON H.leader = C.id;"
    result = execute_query(db_connection, query).fetchall();
    print(result)

    id = request.form['editHouse']

    query = "SELECT id, name, members, motto, sigil, leader FROM got_houses WHERE id = %s;"
    data = (id,)
    sresult = execute_query(db_connection, query, data).fetchone();
    print(result)

    query = "SELECT id, fname, lname FROM got_characters;"
    cresult = execute_query(db_connection, query).fetchall();
    print(result)

    return render_template('update_houses.html', rows=result, editH = sresult, characters = cresult);

@webapp.route('/update_house/<int:id>', methods=['POST'])
def update_house(id):
    db_connection = connect_to_database()
    request.method == 'POST';
    print("Updating House!");
    name = request.form['upName']
    members = request.form['upMembers']
    motto = request.form['upMotto']
    sigil = request.form['upSigil']
    leader = request.form['upLeader']

    #check if leader input contains NULL
    if leader == "NULL":
        query = "UPDATE got_houses SET name = %s, members = %s, motto = %s, sigil = %s, leader = NULL WHERE id = %s;"
        data = (name, members, motto, sigil, id)
    else:
        query = "UPDATE got_houses SET name = %s, members = %s, motto = %s, sigil = %s, leader = %s WHERE id = %s;"
        data = (name, members, motto, sigil, leader, id)

    execute_query(db_connection, query, data)
    return redirect ('/houses');

@webapp.route('/edit_skill', methods=['POST', 'GET'])
def edit_skills():

    print("Fetching and rendering skills web page")
    db_connection = connect_to_database()
    query = "SELECT name, battle_utility, acquisition_cost, rarity, value, id FROM got_skills;"
    result = execute_query(db_connection, query).fetchall();
    print(result)

    id = request.form['editSkill']

    query = "SELECT id, name, battle_utility, acquisition_cost, rarity, value FROM got_skills WHERE id = %s;"
    data = (id,)
    sresult = execute_query(db_connection, query, data).fetchone();
    print(result)

    return render_template('update_skills.html', rows=result, editS = sresult);

@webapp.route('/update_skill/<int:id>', methods=['POST'])
def update_skill(id):
    db_connection = connect_to_database()
    request.method == 'POST';
    print("Updating Skill!");
    name = request.form['upName']
    utility = request.form['upUtility']
    cost = request.form['upCost']
    rarity = request.form['upRarity']
    value = request.form['upValue']

    query = "UPDATE got_skills SET name = %s, battle_utility = %s, acquisition_cost = %s, rarity = %s, value = %s WHERE id = %s;"
    data = (name, utility, cost, rarity, value, id)

    execute_query(db_connection, query, data)
    return redirect ('/skills');

@webapp.route('/edit_religion', methods=['POST', 'GET'])
def edit_religions():

    print("Fetching and rendering religions web page")
    db_connection = connect_to_database()
    query = "SELECT name, worshipers, theism, age, symbol, id FROM got_religions;"
    result = execute_query(db_connection, query).fetchall();
    print(result)

    id = request.form['editReligion']

    query = "SELECT id, name, worshipers, theism, age, symbol FROM got_religions WHERE id = %s;"
    data = (id,)
    sresult = execute_query(db_connection, query, data).fetchone();
    print(result)

    return render_template('update_religions.html', rows=result, editR = sresult);

@webapp.route('/update_religion/<int:id>', methods=['POST'])
def update_religion(id):
    db_connection = connect_to_database()
    request.method == 'POST';
    print("Updating Relgion!");
    name = request.form['upName']
    worshipers = request.form['upWorshipers']
    theism = request.form['upTheism']
    age = request.form['upAge']
    symbol = request.form['upSymbol']

    query = "UPDATE got_religions SET name = %s, worshipers = %s, theism = %s, age = %s, symbol = %s WHERE id = %s;"
    data = (name, worshipers, theism, age, symbol, id)

    execute_query(db_connection, query, data)
    return redirect ('/religions');

@webapp.route ('/delete_character/', methods=['POST'])
def delete_character():
    db_connection = connect_to_database()
    request.method == 'POST';
    id = request.form['deleteCharacter']

    query = "DELETE FROM got_characters WHERE id = %s;"
    data = (id,)

    result = execute_query(db_connection, query, data)
    return redirect ('/characters');

@webapp.route ('/delete_house/', methods=['POST'])
def delete_house():
    db_connection = connect_to_database()
    request.method == 'POST';
    id = request.form['deleteHouse']

    query = "DELETE FROM got_houses WHERE id = %s;"
    data = (id,)

    result = execute_query(db_connection, query, data)
    return redirect ('/houses');


@webapp.route ('/delete_skill/', methods=['POST'])
def delete_skill():
    db_connection = connect_to_database()
    request.method == 'POST';
    id = request.form['deleteSkill']

    query = "DELETE FROM got_skills WHERE id = %s;"
    data = (id,)

    result = execute_query(db_connection, query, data)
    return redirect ('/skills');


@webapp.route ('/delete_religion/', methods=['POST'])
def delete_religions():
    db_connection = connect_to_database()
    request.method == 'POST';
    id = request.form['deleteReligion']

    query = "DELETE FROM got_religions WHERE id = %s;"
    data = (id,)

    result = execute_query(db_connection, query, data)
    return redirect ('/religions');

@webapp.route('/add_character_skill', methods = ['POST'])
def add_character_skill():
    db_connection = connect_to_database()
    request.method == 'POST';

    cid = request.form['addCID']
    sid = request.form['addSID']

    query = "INSERT INTO got_character_skills (character_id, skill_id) VALUES (%s, %s);"
    data = (cid, sid)

    execute_query(db_connection, query, data)
    return redirect ('/skills');

@webapp.route('/remove_character_skill', methods =['POST'])
def delete_character_skill():
    db_connection = connect_to_database()
    request.method == 'POST';
    cid = request.form['possessingCharacter']
    sid = request.form['possessedSkill']

    query = "DELETE FROM got_character_skills WHERE character_id = %s AND skill_id = %s;"
    data = (cid, sid)

    result = execute_query(db_connection, query, data)
    return redirect ('/characters');

@webapp.route('/add_house_loyalty', methods = ['POST'])
def add_house_loyalty():
    db_connection = connect_to_database()
    request.method == 'POST';

    house1 = request.form['addLoyalty1']
    house2 = request.form['addLoyalty2']

    query = "INSERT INTO got_house_loyalties (house_receiving, house_offering) VALUES (%s, %s);"
    data = (house1, house2)

    execute_query(db_connection, query, data)
    return redirect ('/houses');

@webapp.route('/remove_house_loyalty', methods = ['POST'])
def delete_house_loyalty():
    db_connection = connect_to_database()
    request.method == 'POST';
    house1 = request.form['deleteLoyalty1']
    house2 = request.form['deleteLoyalty2']

    query = "DELETE FROM got_house_loyalties WHERE house_receiving = %s AND house_offering = %s;"
    data = (house1, house2)

    result = execute_query(db_connection, query, data)
    return redirect('/houses');
