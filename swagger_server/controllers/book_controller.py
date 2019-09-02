import connexion
import six

from swagger_server.models.book import Book  # noqa: E501
from swagger_server import util


def add_book(body):  # noqa: E501
    """Add a new book to the store

     # noqa: E501

    :param body: Book object that needs to be added to the store
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Book.from_dict(connexion.request.get_json())  # noqa: E501
    print('body', body)
    return 'do some magic!'


def delete_book(book_id):  # noqa: E501
    """Deletes a book

     # noqa: E501

    :param book_id: Book id to delete
    :type book_id: int

    :rtype: None
    """
    return 'do some magic!'


def get_all_books(page=None, per_page=None):  # noqa: E501
    """Get all Books

    # noqa: E501

    :param page:
    :type page: int
    :param per_page:
    :type per_page: int

    :rtype: None
    """

    return 'do some magic!'


def find_books_by_status(status):  # noqa: E501
    """Finds Books by status

    Multiple status values can be provided with comma separated strings # noqa: E501

    :param status: Status values that need to be considered for filter
    :type status: List[str]

    :rtype: List[Book]
    """
    return 'do some magic!'


def get_book_by_id(book_id):  # noqa: E501
    """Find book by ID

    Returns a single book # noqa: E501

    :param book_id: ID of book to return
    :type book_id: int

    :rtype: Book
    """
    return 'do some magic!'


def update_book_with_id(book_id, body):  # noqa: E501
    """Update an existing book

     # noqa: E501

    :param book_id: ID of book that needs to be updated
    :type book_id: int
    :param body: Book object that needs to be added to the store
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Book.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
