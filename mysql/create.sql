CREATE TABLE {{ database }}.books (
    id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name varchar(255) NOT NULL,
    author varchar(255) NOT NULL,
    imageUrl varchar(1000) NOT NULL
);
