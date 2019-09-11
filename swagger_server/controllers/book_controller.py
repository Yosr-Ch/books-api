import connexion
import six
import mysql.connector

from flask import abort
from copy import deepcopy
from swagger_server.models.book import Book  # noqa: E501
from swagger_server import util
from swagger_server import config

def get_author(cursor, body):  # noqa: E501
    author_id = None
    if 'name' in body['author']:
        author_name = body['author']['name']
        cursor.execute("SELECT * FROM authors WHERE name = %s", (author_name,))
        if cursor.rowcount:
            for (id, name) in cursor:
                author_id = id
        else: # add author if doesn't exist
            add_author = ("INSERT INTO authors "
                      "(name)"
                      "VALUES (%s)")
            data_author = (body['author']['name'],)
            try:
                cursor.execute(add_author, data_author)
            except Exception as e:
                print("Error:", e)
            author_id = cursor.lastrowid
    elif 'id' in body['author']:
        try:
            cursor.execute("SELECT * FROM authors WHERE id = %s", (body['author']['id'],))
            if cursor.rowcount:
                author_id = body['author']['id']

        except Exception as e:
            print("Error:", e)

    return author_id


def add_book(body):  # noqa: E501
    """Add a new book to the store

     # noqa: E501

    :param body: Book object that needs to be added to the store
    :type body: dict | bytes

    :rtype: None
    """
    cnx = mysql.connector.connect(**config.DB_CONFIG)
    cursor = cnx.cursor(buffered=True)

    author_id = get_author(cursor, body)
    # insert book
    add_book = ("INSERT INTO books "
               "(isbn, name, price, availability, authorId) "
               "VALUES (%s, %s, %s, %s, %s)")
    data_book = (body.get('isbn', ''), body.get('name', ''), body.get('price', 0), body.get('status', 'pending'), author_id)
    try:
        cursor.execute(add_book, data_book)
        book_id = cursor.lastrowid
    except Exception as e:
        print("Error:", e)
    cursor.close()
    cnx.commit()
    cnx.close()

    return {'book_id': book_id}


def delete_book(book_id):  # noqa: E501
    """Deletes a book

     # noqa: E501

    :param book_id: Book id to delete
    :type book_id: int

    :rtype: None
    """
    cnx = mysql.connector.connect(**config.DB_CONFIG)
    cursor = cnx.cursor()
    query = "DELETE FROM books WHERE bookId = %s"
    try:
        cursor.execute(query, (book_id,))
        cnx.commit()
    except mysql.connector.Error as err:
        print("Error:", err.message)
        cnx.close()
    except:
        print("Unknown error occurred!")
        cnx.close()
    finally:
        cursor.close()
        cnx.close()

    return {'book_id': book_id}


def get_all_books(page=0, per_page=18446744073709551615):  # noqa: E501
    """Get all Books

    # noqa: E501

    :param page:
    :type page: int
    :param per_page:
    :type per_page: int

    :rtype: None
    """
    cnx = mysql.connector.connect(**config.DB_CONFIG)
    cursor = cnx.cursor()
    # query = ("SELECT * FROM books LIMIT %s,%s")
    query = ("""SELECT b.bookId, b.isbn, b.name, b.price, b.availability, a.id as author_id, a.name as author_name
        FROM (SELECT * FROM books LIMIT %s,%s) as b
        Left JOIN authors a
        ON b.authorId = a.id
        ORDER BY bookId """)
    try:
        cursor.execute(query, (page, per_page))
    except Exception as e:
        print('exception:', e)
    results = []
    for (bookId, isbn, name, price, availability, author_id, author_name) in cursor:
        results.append({
            'id': bookId,
            'isbn': isbn,
            'name': name,
            'price': price,
            'availability': availability,
            'author': {
                'id': author_id,
                'name': author_name,
            }
        })
    cursor.close()
    cnx.close()

    return results



def get_book_by_id(book_id):  # noqa: E501
    """Find book by ID

    Returns a single book # noqa: E501

    :param book_id: ID of book to return
    :type book_id: int

    :rtype: Book
    """
    cnx = mysql.connector.connect(**config.DB_CONFIG)
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT * FROM books WHERE bookId = %s ")

    try:
        cursor.execute(query, (book_id,))
    except Exception as e:
        print('Error:', e)
    if cursor.rowcount == 0:
        cursor.close()
        cnx.close()
        abort(404, 'Book not found')
    result={}
    author_id=None
    for (bookId, isbn, name, price, availability, authorId) in cursor:
        result = {
            'id': bookId,
            'isbn': isbn,
            'name': name,
            'price': price,
            'availability': availability,
        }
        author_id = authorId

    book_author = ("SELECT * FROM authors WHERE id = %s ")
    try:
        cursor.execute(book_author, (author_id,))
    except Exception as e:
        print('Error:', e)
    result['author'] = {
        'id': None,
        'name': None,
    }
    for (id, name) in cursor:
        result['author']['id'] = id
        result['author']['name'] = name
    cursor.close()
    cnx.close()
    return result


def update_book_with_id(book_id, body):  # noqa: E501
    """Update an existing book

     # noqa: E501

    :param book_id: ID of book that needs to be updated
    :type book_id: int
    :param body: Book object that needs to be added to the store
    :type body: dict | bytes

    :rtype: None
    """
    cnx = mysql.connector.connect(**config.DB_CONFIG)
    cursor = cnx.cursor(buffered=True)
    author_id = get_author(cursor, body)
    dict = deepcopy(body)
    # delete author object if exists
    dict.pop("author", None)
    # add author id to dict
    dict['authorId'] = author_id
    update_book = ("UPDATE books SET {} WHERE bookId = %s".format(', '.join('{}=%s'.format(k) for k in dict)))
    data = tuple(list(dict.values())+[book_id])
    try:
        cursor.execute(update_book, data)
        cnx.commit()

    except Exception as e:
        print("Error:", e)


    cursor.close()
    cnx.close()
    return {'book_id': book_id}
