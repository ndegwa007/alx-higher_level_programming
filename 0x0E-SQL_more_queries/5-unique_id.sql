-- scripts that create a table with a unique attribute
CREATE TABLE IF NOT EXISTS `unique_id`(
	id INT DEFAULT 1 UNIQUE,
	name VARCHAR(256)
	);
