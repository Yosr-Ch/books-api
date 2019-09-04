CREATE DATABASE booksdb;
use booksdb;

DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS authors;


CREATE TABLE authors (
  id   INT              NOT NULL AUTO_INCREMENT,
  name VARCHAR (100)     NOT NULL,
  PRIMARY KEY (id)
);

INSERT INTO authors
  (name)
VALUES
  ('George Orwell'),
  ('Harper Lee');

CREATE TABLE books (
    bookId int NOT NULL AUTO_INCREMENT,
    isbn VARCHAR (13) NOT NULL,
    name VARCHAR (200) NOT NULL,
    price DECIMAL(8,2),
    availability VARCHAR (10),
    authorId int DEFAULT NULL,
    PRIMARY KEY (bookId),
    CONSTRAINT FK_AuthorBook FOREIGN KEY (authorId)
    REFERENCES authors(id) ON DELETE SET NULL ON UPDATE CASCADE
);

INSERT INTO books
  (isbn, name, price, availability, authorId)
VALUES
  ('9789630793292', 'Animal farm', 7.19, 'available', 1),
  ('9781428113701', 'To kill a mocking bird', 3.42, 'sold', 2);
