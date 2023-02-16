-- script creates DB and Table 
-- id: int attribute unique, auto-generated, not null and PK
-- name: varchar(256) not null

CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS `hbtn_0d_usa`.`states`(
	id INT NOT NULL AUTO_INCREMENT,
	name VARCHAR(256),
	PRIMARY KEY(id)
	);

	
