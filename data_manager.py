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
def get_applicants(cursor: RealDictCursor) -> list:
    query = """
        SELECT first_name, last_name, phone_number, email, application_code 
        FROM applicant
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


@database_common.connection_handler
def get_applicant_data_by_email_ending(cursor: RealDictCursor, applicant_email_ending:str) -> list:
    query = """
        SELECT first_name, last_name, phone_number,
        concat(first_name,' ',last_name) as full_name 
        FROM applicant WHERE email like '%{0!s}'""".format(applicant_email_ending)
    cursor.execute(query)
    return cursor.fetchall()


@database_common.connection_handler
def get_applicant_by_code(cursor: RealDictCursor, code) -> list:
    query = """
        SELECT first_name, last_name, phone_number, email, application_code 
        FROM applicant WHERE application_code = '{0!s}'""".format(code)
    cursor.execute(query)
    return cursor.fetchone()


@database_common.connection_handler
def update_applicant_phone(cursor: RealDictCursor, new_phone, code) -> list:
    query = """
        UPDATE Applicant
        SET phone_number = '{0!s}'
        WHERE application_code = '{1!s}';""".format(new_phone, code)
    cursor.execute(query)


@database_common.connection_handler
def delete_applicant_by_code(cursor: RealDictCursor, code) -> list:
    query = """
        DELETE FROM Applicant *
        WHERE application_code = '{0!s}';""".format(code)
    cursor.execute(query)


@database_common.connection_handler
def delete_applicant_by_email_ending(cursor: RealDictCursor, email_ending) -> list:
    query = """
        DELETE FROM Applicant *
        WHERE email LIKE '%{0!s}'""".format(email_ending)
    cursor.execute(query)


@database_common.connection_handler
def add_applicant(cursor: RealDictCursor, new_applicant) -> list:
    query = """
    INSERT INTO applicant (first_name, last_name, phone_number, email, application_code)
    VALUES('{0!s}', '{1!s}', '{2!s}', '{3!s}', '{4!s}')"""\
        .format(new_applicant["first-name"], new_applicant["last-name"],
                new_applicant["phone-number"], new_applicant["email"],
                new_applicant['application-code'])
    cursor.execute(query)