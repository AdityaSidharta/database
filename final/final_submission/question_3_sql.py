import mysql_check
import pandas as pd


def question_3_example_get_customers(country):
    """
    This is an example of what your answers should look like.
    :param country:
    :return:
    """

    # You may need to set the connection info. I do just to be safe.
    mysql_check.set_connect_info("root", "password", "127.0.0.1")

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
    # You may need to set the connection info. I do just to be safe.
    mysql_check.set_connect_info("root", "password", "127.0.0.1")

    # You will provide your SQL queries in this format. %s is a parameter.
    q = """
        WITH p_ordernumber AS (
        SELECT orderNumber, SUM(orderdetails.quantityOrdered * orderdetails.priceEach) AS revenue
        FROM classicmodels.orderdetails
        GROUP BY orderNumber),

        p_order AS (
            SELECT orderNumber, revenue, customerNumber
            FROM classicmodels.orders
            INNER JOIN p_ordernumber USING(orderNumber)
            WHERE status = "Shipped"
        )

        SELECT country, SUM(revenue)
        FROM p_order
        INNER JOIN classicmodels.customers USING (customerNumber)
        GROUP BY country
    """

    # Connect and run the query
    conn = mysql_check.get_connection()
    cur = conn.cursor()
    res = cur.execute(q, [])
    result = cur.fetchall()

    # Convert to a Data Frame and return
    result = pd.DataFrame(result)

    return result


def question_3_purchases_and_payments():
    # You may need to set the connection info. I do just to be safe.
    mysql_check.set_connect_info("root", "password", "127.0.0.1")

    # You will provide your SQL queries in this format. %s is a parameter.
    q = """
        SELECT customerNumber,
        customerName,
        SUM(revenue)                 AS total_spent,
        total_payment,
        SUM(revenue) - total_payment AS total_unpaid
        FROM (
                SELECT orderNumber, revenue, customerNumber
                FROM classicmodels.orders
                        INNER JOIN (
            SELECT orderNumber, SUM(orderdetails.quantityOrdered * orderdetails.priceEach) AS revenue
            FROM classicmodels.orderdetails
            GROUP BY orderNumber) p_ordernumber USING (orderNumber)
            ) p_order
                INNER JOIN classicmodels.customers USING (customerNumber)
                INNER JOIN (SELECT customerNumber, SUM(amount) as total_payment
                            FROM classicmodels.payments
                            GROUP BY customerNumber) p_payment USING (customerNumber)
        GROUP BY customerNumber, customerName, total_payment
        ORDER BY customerName
    """

    # Connect and run the query
    conn = mysql_check.get_connection()
    cur = conn.cursor()
    res = cur.execute(q, [])
    result = cur.fetchall()

    # Convert to a Data Frame and return
    result = pd.DataFrame(result)

    return result


def question_3_customers_and_lines():
    # You may need to set the connection info. I do just to be safe.
    mysql_check.set_connect_info("root", "password", "127.0.0.1")

    # You will provide your SQL queries in this format. %s is a parameter.
    q = """
        WITH p_orderdetail AS (
        SELECT orderNumber,
            SUM(IF(productLine IN ("Planes", "Trucks and Buses"), 1, 0)) AS sum_planeortruck
        FROM classicmodels.orderdetails
        INNER JOIN classicmodels.products USING (productCode)
        GROUP BY orderNumber
        ),

        p_order AS (
            SELECT customerNumber, SUM(sum_planeortruck) AS sum_planeortruck
            FROM classicmodels.orders
            INNER JOIN p_orderdetail USING (orderNumber)
            GROUP BY customerNumber
        )

        SELECT customerNumber, customerName
        FROM classicmodels.customers
        INNER JOIN p_order USING (customerNumber)
        WHERE sum_planeortruck = 0
        ORDER BY customerName
    """

    # Connect and run the query
    conn = mysql_check.get_connection()
    cur = conn.cursor()
    res = cur.execute(q, [])
    result = cur.fetchall()

    # Convert to a Data Frame and return
    result = pd.DataFrame(result)

    return result


