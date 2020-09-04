CREATE DATABASE testDB;
GO
USE DATABASE testDB;
GO
CREATE TABLE Test
(
Id int,
Data varchar(50)
);
GO
INSERT INTO Test (
Id, Data
)
VALUES (
1, 'A'
);
GO