--Game of Thrones Database Data Manipulation Query (Dienhart/Youngblom)

--Display Characters table
  SELECT * FROM 'got_characters';

--Display Houses table
  SELECT * FROM 'got_houses';

  --Display Skills table
  SELECT * FROM 'got_skills';

--Display Religions table
  SELECT * FROM 'got_religions';

--Add/modify/delete Character
--add:
  INSERT INTO 'got_characters' ('fname', 'lname', 'nobility', 'gender', 'age', 'house', 'religion')
  VALUES (:fnameIn, :lnameIn, :nobilityIn, :genderIn, :ageIn, :houseIn, :religionIn);
--modify
  UPDATE 'got_characters'
  SET :updateColumn = :updateValue
  WHERE 'fname' = :fnameIn AND 'lname' = :lnameIn;
--Delete
  DELETE FROM 'got_characters' WHERE 'fname' = :fnameIn, 'lname' = :lnameIn;

--Add/modify Houses
--add:
  INSERT INTO 'got_houses' ('name', 'members', 'motto', 'sigel', 'leader')
  VALUES (:nameIn, :membersIn, :mottoIn, :sigelIn, :leaderIn);
--modify
  UPDATE 'got_houses'
  SET :updateColumn = :updateValue
  WHERE 'name' = :houseNameIn;
--Delete
  DELETE FROM 'got_houses' WHERE 'name' = :nameIn;

--Add/modify Skill
--add:
  INSERT INTO 'got_skills' ('name', 'battle_utility', 'acquisition_cost', 'rarity', 'value')
  VALUES (:nameIn, :battle_utilityIn, :acquisition_costIn, :rarityIn, :valueIn);
--modify
  UPDATE 'got_skills'
  SET :updateColumn = :updateValue
  WHERE 'name' = :skillNameIn;
--Delete
  DELETE FROM 'got_skills' WHERE 'name' = :nameIn;

--Add/modify Religion
--add
  INSERT INTO 'got_religions' ('name', 'worshippers', 'theism', 'age', 'symbol')
  VALUES (:nameIn, :worshippersIn, :theismIn, :ageIn, :symbolIn);
--modify
  UPDATE 'got_religions'
  SET :updateColumn = :updateValue
  WHERE 'name' = :religionNameIn;
--Delete
  DELETE FROM 'got_religions' WHERE 'name' = :nameIn;

--Show all Characters allied with a given House
  SELECT 'fname', 'lname' FROM 'got_characters' WHERE 'house' = :houseInput;

--Show the leader of a given House
  SELECT C.fname, C.lname FROM 'got_characters' C
  INNER JOIN 'got_houses' H ON  H.leader = C.id
  WHERE H.name = :houseInput;

--Show all Houses loyal to a given House
  SELECT  HH.name FROM 'got_houses' H
  INNER JOIN 'got_house_loyalties' HL ON HL.house_receiving = H.id
  INNER JOIN 'got_houses' HH ON HH.id = HL.house_offering
  WHERE H.id = :houseInput;

--Show a list of Skills possessed by a given Character
  SELECT  S.name FROM 'got_characters' C
  INNER JOIN 'got_character_skills' CS ON CS.character_id = C.id
  INNER JOIN 'got_skills' S ON S.id = CS.skill_id
  WHERE C.id = :characterInput;

--Show all Characters belonging to a given Religion
  SELECT 'fname', 'lname' FROM 'got_characters' WHERE 'religion' = :religionInput;

--Reassign leadership of a House
  UPDATE 'got_houses'
  SET 'leader' = :updateValue
  WHERE 'name' = :houseNameIn;

--Delete a Religion & cascade to devoted Characters
  UPDATE 'got_characters'
  SET 'religion' = NULL
  WHERE 'religion' = :religionIn;
  DELETE FROM 'got_religions' WHERE 'name' = :religionIn;

--Delete a House & cascade to allied Characters and other loyal Houses
  UPDATE 'got_characters'
  SET 'house' = NULL
  WHERE 'house' = :houseIn;
  DELETE 'house_offering' AND 'house_receiving' FROM 'got_house_loyalties'
  WHERE 'house_receiving' OR 'house_offering' = :houseIn;
  DELETE FROM 'got_houses' WHERE 'name' = :houseIn;

--Delete a Skill & cascade to Characters possessing that Skill
  DELETE 'skill_id' AND 'character_id' FROM 'got_character_skills'
  WHERE 'skill_id' = :skillsIn;
  DELETE FROM 'got_skills' WHERE 'name' = :skillIn;

--Show all characters with a given skill
  SELECT  C.fname, C.lname FROM 'got_skills' S
  INNER JOIN 'got_character_skills' CS ON CS.skill_id = S.id
  INNER JOIN 'got_characters' C ON C.id = CS.character_id;
