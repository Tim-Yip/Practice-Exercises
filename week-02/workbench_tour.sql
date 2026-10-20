/*
Ex1C - Workbench Readiness check table
Name: Timothy Yip Date: 10/20/2026
Q1: MySQL80
Q2: The + next to connections
Q3: 2 Information
Q4: Login User: root, Port: 3306, Version: 8.0.46
Q5: Server Status, Client Connections
Q6: smallint UN AI PK, AI: Auto Increment, PK: Primary Key
Q7: Columns: actor_id, film_id, last_update. 2 Foreign Keys, pointing to actor table. 
Q8: Opened a new query tab selected all columns from film_actor. 
Q9: 200 rows returned, bottom of screen in Action Output
Q10: Everything succeeded, action 6 failed because "actr" doesn't exist.
Q11: Verticle output lists everything by rows with all information in that row before displaying the next row. 
Q12: Akroyk
Q13: 3 actors match with the last name Davis. 
Q14: data type: varchar, max length: 45
*/
USE sakila;
SELECT * FROM actor;
SELECT * FROM sakila.film;
SELECT * FROM actor;