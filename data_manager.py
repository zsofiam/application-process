from typing import List, Dict

from psycopg2 import sql
from psycopg2.extras import RealDictCursor

import database_common


@database_common.connection_handler
def get_mentors(cursor: RealDictCursor) -> list:
    query = """
        SELECT first_name, last_name, city
        FROM mentor
        ORDER BY first_name"""
    cursor.execute(query)
    return cursor.fetchall()


@database_common.connection_handler
def get_mentors_by_last_name(cursor: RealDictCursor, last_name: str) -> list:
    query = """
        SELECT first_name, last_name, city
        FROM mentor WHERE last_name = '{0!s}'
        ORDER BY first_name""".format(last_name)
    cursor.execute(query)

    # cursor.execute(sql.SQL("select {col1},{col2},{col3} from {table}"
    #                        " where {col2} = '{0!s}' order by {col1}"
    #                .format(col1=sql.Identifier('first_name'),
    #                        col2=sql.Identifier('last_name'),
    #                        col3=sql.Identifier('city'),
    #                        table=sql.Identifier('mentor')).format(last_name)))

    # cursor.execute(
    #     sql.SQL("select {col} from {table} ").
    #         format(col=sql.Identifier('mentor'),
    #                table=sql.Identifier('application_process'))
    # )
    return cursor.fetchall()


@database_common.connection_handler
def get_mentors_by_city(cursor: RealDictCursor, city: str) -> list:
    query = """
        SELECT first_name, last_name, city
        FROM mentor WHERE city = '{0!s}'""".format(city)
    cursor.execute(query)
    return cursor.fetchall()


@database_common.connection_handler
def get_applicant_by_name(cursor: RealDictCursor, applicant_name:str) -> list:
    query = """
        SELECT first_name, last_name, phone_number,
        concat(first_name,' ',last_name) as full_name 
        FROM applicant WHERE first_name = '{0!s}' or last_name = '{0!s}'""".format(applicant_name)
    cursor.execute(query)
    return cursor.fetchall()