-- creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL server
CREATE IF NOT EXISTS `hbtn_0d_usa`;

USE `hbtn_0d_usa`;

CREATE TABLE IF NOT EXISTS `cities` (
  `id` INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
  `name` VARCHAR(256) NOT NULL
);