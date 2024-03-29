# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Body(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, name: str=None, status: str=None):  # noqa: E501
        """Body - a model defined in Swagger

        :param name: The name of this Body.  # noqa: E501
        :type name: str
        :param status: The status of this Body.  # noqa: E501
        :type status: str
        """
        self.swagger_types = {
            'name': str,
            'status': str
        }

        self.attribute_map = {
            'name': 'name',
            'status': 'status'
        }
        self._name = name
        self._status = status

    @classmethod
    def from_dict(cls, dikt) -> 'Body':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The body of this Body.  # noqa: E501
        :rtype: Body
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self) -> str:
        """Gets the name of this Body.

        Updated name of the book  # noqa: E501

        :return: The name of this Body.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Body.

        Updated name of the book  # noqa: E501

        :param name: The name of this Body.
        :type name: str
        """

        self._name = name

    @property
    def status(self) -> str:
        """Gets the status of this Body.

        Updated status of the book  # noqa: E501

        :return: The status of this Body.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status: str):
        """Sets the status of this Body.

        Updated status of the book  # noqa: E501

        :param status: The status of this Body.
        :type status: str
        """

        self._status = status
