import connexion
import mysql.connector

from flask import abort
from copy import deepcopy
from swagger_server.models.author import Author  # noqa: E501
from swagger_server import config


def get_all_authors(page=0, per_page=18446744073709551615):  # noqa: E501
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
    query = ("SELECT * FROM authors LIMIT %s,%s")
    try:
        cursor.execute(query, (page, per_page))
    except Exception as e:
        print('exception:', e)
    results = []
    for (id, name) in cursor:
        results.append({
            'id': id,
            'name': name,
        })
    cursor.close()
    cnx.close()

    return results
