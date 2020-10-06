# -*- codingÑ utf-8 -*-
# -----------------------------
# Name: Login
# Author: Oscar Velasco
# Creation: 18/05/2020
# Modified: 18/05/2020
# ------------------------------

__version__ = "1.0"

"""
Here you will find the design for the login screen
"""

import psycopg2
from psycopg2 import sql


class Database:

    def create(self, table, columns, values):
        postgres_connection = psycopg2.connect("user=postgres password='doctoradO159' dbname=ariadna")
        cursor = postgres_connection.cursor()
        query = sql.SQL('INSERT INTO {} ({}) VALUES ({});').format(
                                                                    sql.Identifier(table),
                                                                    sql.SQL(', ').join(map(sql.Identifier, columns)),
                                                                    sql.SQL(', ').join(map(sql.Literal, values))
                                                                    )
        cursor.execute(query)
        postgres_connection.commit()
        cursor.close()
        postgres_connection.close()

    def get_last_id(self, table):
        postgres_connection = psycopg2.connect("user=postgres password='doctoradO159' dbname=ariadna")
        cursor = postgres_connection.cursor()
        query = sql.SQL('SELECT MAX(id) FROM {};').format(
                                                            sql.Identifier(table)
                                                            )
        cursor.execute(query)
        max_id = cursor.fetchone()
        cursor.close()
        postgres_connection.close()
        return max_id

    def search(self, valid_column, table, column, value, type_condition):
        postgres_connection = psycopg2.connect("user=postgres password='doctoradO159' dbname=ariadna")
        cursor = postgres_connection.cursor()
        if type_condition == "num":
            query = sql.SQL('SELECT {} FROM {} WHERE {} = {};').format(
                                                                    sql.Identifier(valid_column),
                                                                    sql.Identifier(table),
                                                                    sql.SQL(', ').join(map(sql.Identifier, column)),
                                                                    sql.SQL(', ').join(map(sql.Literal, value))
                                                                    )
        else:
            query = sql.SQL('SELECT {} FROM {} WHERE {} ilike {};').format(
                                                                    sql.Identifier(valid_column),
                                                                    sql.Identifier(table),
                                                                    sql.SQL(', ').join(map(sql.Identifier, column)),
                                                                    sql.SQL(', ').join(map(sql.Literal, value))
                                                                    )
        cursor.execute(query)
        search_result = cursor.fetchone()
        cursor.close()
        postgres_connection.close()
        return search_result


Database()
