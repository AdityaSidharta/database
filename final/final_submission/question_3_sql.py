import mysql_check
import pandas as pd


def question_3_example_get_customers(country):
    """
    This is an example of what your answers should look like.
    :param country:
    :return:
    """

    # You may need to set the connection info. I do just to be safe.
    mysql_check.set_connect_info("dbuser", "dbuserdbuser", "localhost")

    # You will provide your SQL queries in this format. %s is a parameter.
    q = """
        select customerNumber, customerName, country
            from classicmodels.customers
            where
            country = %s
    """

    # Connect and run the query
    conn = mysql_check.get_connection()
    cur = conn.cursor()
    res = cur.execute(q, [country])
    result = cur.fetchall()

    # Convert to a Data Frame and return
    result = pd.DataFrame(result)

    return result


def question_3_revenue_by_country():

    result = None
    return result


def question_3_purchases_and_payments():

    result = None
    return result


def question_3_customers_and_lines():

    result = None
    return result


