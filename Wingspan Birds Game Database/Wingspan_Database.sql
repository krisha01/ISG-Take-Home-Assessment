-- Database: Wingspan_Birds_BG

-- DROP DATABASE IF EXISTS "Wingspan_Birds_BG";

CREATE DATABASE "Wingspan_Birds_BG"
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'English_United States.1252'
    LC_CTYPE = 'English_United States.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;

CREATE TABLE Birds(
	Bird_ID BIGSERIAL NOT NULL PRIMARY KEY,
	Bird_Name VARCHAR(100) NOT NULL,
	Sci_Bird_Name VARCHAR(100) NOT NULL,
	Points INTEGER NOT NULL,
	Nest_Type VARCHAR(50) NOT NULL,
	No_of_eggs INTEGER NOT NULL,
	Wingspan INTEGER NOT NULL,
	Habitat_count INTEGER NOT NULL,
	Food_count INTEGER NOT NULL,
	Power_type VARCHAR(50) NOT NULL);

CREATE TABLE Habitat(
	Habitat_ID BIGSERIAL NOT NULL PRIMARY KEY,
	Habitat_name VARCHAR(50) NOT NULL);
	
CREATE TABLE Food(
	Food_ID BIGSERIAL NOT NULL PRIMARY KEY,
	Food_name VARCHAR(50) NOT NULL);
	
CREATE TABLE Hab_join(
	Bird_id BIGINT REFERENCES Birds(Bird_ID),
	Habitat_id BIGINT REFERENCES Habitat(Habitat_ID));
	
CREATE TABLE food_join(
	Bird_id BIGINT REFERENCES Birds(Bird_ID),
	Food_id BIGINT REFERENCES Food(Food_ID));
	
CREATE TABLE PLAYERS(
	Player_ID BIGSERIAL NOT NULL PRIMARY KEY,
	Player_name VARCHAR(50) NOT NULL);

CREATE TABLE Points(
	Game_ID INTEGER NOT NULL,
	Player_id BIGINT REFERENCES Players(Player_ID),
	Round_no INTEGER NOT NULL,
	Points INTEGER NOT NULL);

-- Autosum view that will show the sum of points for each player 
CREATE VIEW AUTOSUM_POINTS AS
SELECT Player_id, SUM(Points) FROM Points GROUP BY Player_ID ORDER BY Player_ID ASC;
SELECT * FROM AUTOSUM_POINTS;

