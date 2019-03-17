SET FOREIGN_KEY_CHECKS = 0;
DROP TABLE IF EXISTS `got_characters`;
DROP TABLE IF EXISTS `got_houses`;
DROP TABLE IF EXISTS `got_religions`;
DROP TABLE IF EXISTS `got_skills`;
DROP TABLE IF EXISTS `got_character_skills`;
DROP TABLE IF EXISTS `got_house_loyalties`;
SET FOREIGN_KEY_CHECKS = 1;

-- Create Characters table
CREATE TABLE `got_characters` (
 `id` int(11) NOT NULL AUTO_INCREMENT,
 `fname` varchar(255) DEFAULT NULL,
 `lname` varchar(225) NOT NULL,
 `nobility` varchar(255) DEFAULT NULL,
 `gender` varchar(255) DEFAULT NULL,
 `age` int(11) DEFAULT NULL,
 `house` int(11) DEFAULT NULL,
 `religion` int(11) DEFAULT NULL,
 PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Create Houses table
CREATE TABLE `got_houses` (
 `id` int(11) NOT NULL AUTO_INCREMENT,
 `name` varchar(255) NOT NULL,
 `members` bigint(20) DEFAULT NULL,
 `motto` varchar(255) DEFAULT NULL,
 `sigil` varchar(255) DEFAULT NULL,
 `leader` int(11) DEFAULT NULL,
 PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Create Religions table
CREATE TABLE `got_religions` (
 `id` int(11) NOT NULL AUTO_INCREMENT,
 `name` varchar(255) NOT NULL,
 `worshipers` bigint(20) DEFAULT NULL,
 `theism` varchar(255) DEFAULT NULL,
 `age` bigint(20) DEFAULT NULL,
 `symbol` varchar(255) DEFAULT NULL,
 PRIMARY KEY (`id`),
 UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Create Skills table
CREATE TABLE `got_skills` (
 `id` int(11) NOT NULL AUTO_INCREMENT,
 `name` varchar(255) NOT NULL,
 `battle_utility` varchar(225) DEFAULT NULL,
 `acquisition_cost` varchar(255) DEFAULT NULL,
 `rarity` varchar(255) DEFAULT NULL,
 `value` varchar(255) DEFAULT NULL,
 PRIMARY KEY (`id`),
 UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Create Many-to-Many relationship table between Characters and Skills
CREATE TABLE `got_character_skills` (
 `skill_id` int(11) NOT NULL DEFAULT '0',
 `character_id` int(11) NOT NULL DEFAULT '0',
 PRIMARY KEY (`skill_id`, `character_id`),
 KEY `character_id`(`character_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Create Many-to-Many relationship table for House loyalties to other Houses
CREATE TABLE `got_house_loyalties` (
 `house_receiving` int(11) NOT NULL,
 `house_offering` int(11) NOT NULL,
 PRIMARY KEY (`house_receiving`, `house_offering`),
 KEY `house_offering`(`house_offering`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Populate Characters table with sample data
INSERT INTO `got_characters` (`id`, `fname`, `lname`, `nobility`, `gender`, `age`, `house`, `religion`) VALUES
(1, 'Robert', 'Baratheon', 'Highborn', 'Male', 61, 5, 5),
(2, 'Eddard', 'Stark', 'Highborn', 'Male', 50, 1, 1),
(3, 'Tywin', 'Lannister', 'Highborn', 'Male', 57, 2, 4),
(4, 'Margaery', 'Tyrell', 'Highborn', 'Female', 23, 4, 5),
(5, 'Bran', 'Stark', 'Highborn', 'Male', 12, 1, 1),
(6, 'Daenerys', 'Targaryen', 'Highborn', 'Female', 19, 3, 4),
(7, 'Stannis', 'Baratheon', 'Highborn', 'Male', 48, 5, 2),
(8, 'Viserys', 'Targaryen', 'Highborn', 'Male', 22, 3, 4),
(9, 'Olenna', 'Tyrell', 'Highborn', 'Female', 76, 4, 5);

-- Populate Houses table with sample data
INSERT INTO `got_houses` (`id`, `name`, `members`, `motto`, `sigil`, `leader`) VALUES
(1, 'Stark', 45, 'Winter is Coming', 'Direwolf', 2),
(2, 'Lannister', 126, 'Hear Me Roar', 'Lion', 3),
(3, 'Targaryen', 20, 'Fire and Blood', 'Dragon', 8),
(4, 'Tyrell', 553, 'Growing Strong', 'Rose', 9),
(5, 'Baratheon', 263, 'Ours is the Fury', 'Stag', 1);

-- Populate Religions table with sample data
INSERT INTO `got_religions` (`id`, `name`, `worshipers`, `theism`, `age`, `symbol`) VALUES
(1, 'Old Gods of the Forest', 24526, 'Polytheistic', 480, 'Wierwood Heart Tree'),
(2, 'Lord of the Light', 99, 'Monotheistic', 5909, 'Firey Heart'),
(3, 'Many-Faced God', 289, 'Monotheistic', 3450, 'None'),
(4, 'Agnosticism', 1232, 'Agnostic', 940, 'None'),
(5, 'Faith of the Seven', 55098, 'Monotheistic', 125, 'Seven Pointed Star');

-- Populate Skills table with sample data
INSERT INTO `got_skills` (`id`, `name`, `battle_utility`, `acquisition_cost`, `rarity`, `value`) VALUES
(1, 'Swordfighting', 'High', 'High', 'Common', 'High'),
(2, 'Warg', 'Low', 'Low', 'Rare', 'Low'),
(3, 'Hunting', 'Medium', 'High', 'Common', 'High'),
(4, 'Negotiation', 'Low', 'Medium', 'Uncommon', 'Medium'),
(5, 'Charisma', 'Low', 'Low', 'Uncommon', 'High');

-- Populate Character's Skills relationship table with sample data
INSERT INTO `got_character_skills` (`skill_id`, `character_id`) VALUES
(1, 1),
(1, 2),
(1, 7),
(1, 8),
(2, 5),
(3, 1),
(3, 2),
(3, 3),
(3, 7),
(3, 8),
(4, 3),
(4, 4),
(4, 9),
(5, 4),
(5, 6),
(5, 9);

-- Populate Loyalties relationship table with sample data
INSERT INTO `got_house_loyalties` (`house_receiving`, `house_offering`) VALUES
(5, 1),
(2, 4),
(5, 4),
(5, 2);

-- Add foreign keys to Characters table
ALTER TABLE `got_characters`
 ADD CONSTRAINT `got_characters_ibfk_1` FOREIGN KEY (`house`) REFERENCES `got_houses`(`id`) ON DELETE SET NULL ON UPDATE CASCADE,
 ADD CONSTRAINT `got_characters_ibfk_2` FOREIGN KEY (`religion`) REFERENCES `got_religions`(`id`) ON DELETE SET NULL ON UPDATE CASCADE;

-- Add foreign key to Houses table
ALTER TABLE `got_houses` 
 ADD CONSTRAINT `got_houses_ibfk_1` FOREIGN KEY (`leader`) REFERENCES `got_characters`(`id`) ON DELETE SET NULL ON UPDATE CASCADE;

-- Add foreign keys to Character Skills table
ALTER TABLE `got_character_skills`
 ADD CONSTRAINT `got_character_skills_ibfk_1` FOREIGN KEY (`skill_id`) REFERENCES `got_skills`(`id`) ON DELETE CASCADE,
 ADD CONSTRAINT `got_character_skills_ibfk_2` FOREIGN KEY (`character_id`) REFERENCES `got_characters`(`id`) ON DELETE CASCADE;

-- Add foreign keys to House Loyalties table
ALTER TABLE `got_house_loyalties`
 ADD CONSTRAINT `got_house_loyalties_ibfk_1` FOREIGN KEY (`house_receiving`) REFERENCES `got_houses`(`id`) ON DELETE CASCADE,
 ADD CONSTRAINT `got_house_loyalties_ibfk_2` FOREIGN KEY (`house_offering`) REFERENCES `got_houses`(`id`) ON DELETE CASCADE;

