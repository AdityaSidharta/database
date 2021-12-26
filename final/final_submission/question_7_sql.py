import mysql_check
import pandas as pd

def schema_operation_1():
    """
    This is an example of what your answers should look like.
    :param country:
    :return:
    """
    res = None

    # You may need to set the connection info. I do just to be safe.
    mysql_check.set_connect_info("root", "password", "127.0.0.1")

    q = """
    create table classicmodels_star.date
    (
        date_id int not null,
        month   int null,
        quarter int null,
        year    int null,
        constraint date_pk
            primary key (date_id)
    );
    """

    conn = mysql_check.get_connection()
    cur = conn.cursor()
    res = cur.execute(q)

    return res


def schema_operation_2():
    """
    This is an example of what your answers should look like.
    :param country:
    :return:
    """
    res = None

    # You may need to set the connection info. I do just to be safe.
    mysql_check.set_connect_info("root", "password", "127.0.0.1")

    q = """
    create table classicmodels_star.location
    (
    location_id int                       not null,
    city        varchar(255)              null,
    country     varchar(255)              null,
    region      enum ('EMEA', 'NA', 'AP') null,
    constraint location_pk
        primary key (location_id)
    );
    """

    conn = mysql_check.get_connection()
    cur = conn.cursor()
    res = cur.execute(q)

    return res


def schema_operation_3():
    """
    This is an example of what your answers should look like.
    :param country:
    :return:
    """
    res = None

    # You may need to set the connection info. I do just to be safe.
    mysql_check.set_connect_info("root", "password", "127.0.0.1")

    q = """
    create table classicmodels_star.product_type
    (
        product_type_id int          not null,
        scale           varchar(255) null,
        product_line    varchar(255) null,
        constraint product_type_pk
            primary key (product_type_id)
    );
    """

    conn = mysql_check.get_connection()
    cur = conn.cursor()
    res = cur.execute(q)

    return res


def schema_operation_4():
    """
    This is an example of what your answers should look like.
    :param country:
    :return:
    """
    res = None

    # You may need to set the connection info. I do just to be safe.
    mysql_check.set_connect_info("root", "password", "127.0.0.1")

    q = """
    create table classicmodels_star.fact
    (
        order_id        int   not null,
        customerNumber  int   null,
        quantityOrdered int   null,
        priceEach       float null,
        product_type_id int   null,
        location_id     int   null,
        date_id         int   null,
        order_date      date  null,
        order_number    int   null,
        constraint fact_pk
            primary key (order_id),
        constraint fact_date_date_id_fk
            foreign key (date_id) references date (date_id)
                on update cascade on delete cascade,
        constraint fact_location_location_id_fk
            foreign key (location_id) references location (location_id)
                on update cascade on delete cascade,
        constraint fact_product_type_product_type_id_fk
            foreign key (product_type_id) references product_type (product_type_id)
                on update cascade on delete cascade
    );
    """

    conn = mysql_check.get_connection()
    cur = conn.cursor()
    res = cur.execute(q)

    return res

def data_transformation_1():
    res = None

    # You may need to set the connection info. I do just to be safe.
    mysql_check.set_connect_info("root", "password", "127.0.0.1")

    q = """
    INSERT INTO classicmodels_star.date
    SELECT ROW_NUMBER() OVER(ORDER BY dorderDate ASC), MONTH(dorderDate), QUARTER(dorderDate), YEAR(dorderDate)
        FROM (SELECT DISTINCT orderDate AS dorderDate
            FROM classicmodels.orders
            ORDER BY orderDate) x
    """

    conn = mysql_check.get_connection()
    cur = conn.cursor()
    res = cur.execute(q)

    return res


def data_transformation_2():
    res = None

    # You may need to set the connection info. I do just to be safe.
    mysql_check.set_connect_info("root", "password", "127.0.0.1")

    q = """
    INSERT INTO classicmodels_star.location
    SELECT ROW_NUMBER() OVER(ORDER BY city, country), city, country, CASE WHEN country IN ("USA", "Canada") THEN "NA"
        WHEN country IN ("Philippines", "Hong Kong", "Singapore", "Japan", "New Zealand", "Australia")
            THEN "AP" ELSE "EMEA" END
        FROM (SELECT DISTINCT city, country
            FROM classicmodels.customers
            ORDER BY city, country) x
    """

    conn = mysql_check.get_connection()
    cur = conn.cursor()
    res = cur.execute(q)

    return res

def data_transformation_3():
    res = None

    # You may need to set the connection info. I do just to be safe.
    mysql_check.set_connect_info("root", "password", "127.0.0.1")

    q = """
    INSERT INTO classicmodels_star.product_type
    SELECT ROW_NUMBER() OVER(ORDER BY scale, product_line), scale, product_line
        FROM (SELECT DISTINCT productScale AS scale, productLine as product_line
            FROM classicmodels.products
            ORDER BY productScale, productLine) x
    """

    conn = mysql_check.get_connection()
    cur = conn.cursor()
    res = cur.execute(q)

    return res

def data_transformation_4():
    res = None

    # You may need to set the connection info. I do just to be safe.
    mysql_check.set_connect_info("root", "password", "127.0.0.1")

    q = """
    INSERT INTO classicmodels_star.fact
    SELECT ROW_NUMBER() OVER(ORDER BY orderNumber, productCode), customerNumber, quantityOrdered, priceEach, product_type_id, location_id, date_id, orderDate AS order_date, orderNumber AS order_number
    FROM (
        SELECT orderNumber, productCode, quantityOrdered, priceEach, customerNumber, orderDate, city, country, productLine AS product_line, productScale AS scale,
            MONTH(orderDate) AS month, QUARTER(orderDate) AS quarter, YEAR(orderDate) AS year
        FROM classicmodels.orderdetails
        LEFT JOIN classicmodels.orders USING (orderNumber)
        LEFT JOIN classicmodels.products USING (productCode)
        LEFT JOIN classicmodels.customers USING (customerNumber)
        ORDER BY orderNumber, productCode
    ) x
    LEFT JOIN classicmodels_star.location USING(city, country)
    LEFT JOIN classicmodels_star.date USING (month, quarter, year)
    LEFT JOIN classicmodels_star.product_type USING (scale, product_line)
    """

    conn = mysql_check.get_connection()
    cur = conn.cursor()
    res = cur.execute(q)

    return res

def sales_by_year_region():
    res = None

    # You may need to set the connection info. I do just to be safe.
    mysql_check.set_connect_info("root", "password", "127.0.0.1")

    q = """
    WITH dfact AS (
        SELECT fact.priceEach * fact.quantityOrdered AS sales, date_id, location_id
        FROM classicmodels_star.fact
    )

    SELECT year, region, SUM(sales)
    FROM dfact
    LEFT JOIN classicmodels_star.date USING (date_id)
    LEFT JOIN classicmodels_star.location USING (location_id)
    GROUP BY year, region
    """

    conn = mysql_check.get_connection()
    cur = conn.cursor()
    res = cur.execute(q)
    result = cur.fetchall()

    # Convert to a Data Frame and return
    result = pd.DataFrame(result)

    return result


def sales_by_quarter_year_county_region():
    res = None

    # You may need to set the connection info. I do just to be safe.
    mysql_check.set_connect_info("root", "password", "127.0.0.1")

    q = """
    WITH dfact AS (
        SELECT fact.priceEach * fact.quantityOrdered AS sales, date_id, location_id
        FROM classicmodels_star.fact
    )

    SELECT quarter, year, country, region, SUM(sales)
    FROM dfact
    LEFT JOIN classicmodels_star.date USING (date_id)
    LEFT JOIN classicmodels_star.location USING (location_id)
    GROUP BY quarter, year, country, region
    """

    conn = mysql_check.get_connection()
    cur = conn.cursor()
    res = cur.execute(q)
    result = cur.fetchall()

    # Convert to a Data Frame and return
    result = pd.DataFrame(result)

    return result


def sales_by_product_line_scale_year():
    res = None

    # You may need to set the connection info. I do just to be safe.
    mysql_check.set_connect_info("root", "password", "127.0.0.1")

    q = """
    WITH dfact AS (
        SELECT fact.priceEach * fact.quantityOrdered AS sales, product_type_id, date_id
        FROM classicmodels_star.fact
    )

    SELECT year, scale, SUM(sales)
    FROM dfact
    LEFT JOIN classicmodels_star.product_type USING (product_type_id)
    LEFT JOIN classicmodels_star.date USING (date_id)
    GROUP BY year, scale
    """

    conn = mysql_check.get_connection()
    cur = conn.cursor()
    res = cur.execute(q)
    result = cur.fetchall()

    # Convert to a Data Frame and return
    result = pd.DataFrame(result)

    return result


