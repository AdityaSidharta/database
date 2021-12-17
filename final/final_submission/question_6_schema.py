import mysql_check


def schema_operation_1():
    """
    This is an example of what your answers should look like.
    :param country:
    :return:
    """
    res = None

    # You may need to set the connection info. I do just to be safe.
    mysql_check.set_connect_info("dbuser", "dbuserdbuser", "localhost")

    q = """
    """

    conn = mysql_check.get_connection()
    cur = conn.cursor()
    # res = cur.execute(q)

    return res


def schema_operation_2():
    """
    This is an example of what your answers should look like.
    :param country:
    :return:
    """

    res = None

    # You may need to set the connection info. I do just to be safe.
    mysql_check.set_connect_info("dbuser", "dbuserdbuser", "localhost")

    q = """

    """

    conn = mysql_check.get_connection()
    cur = conn.cursor()
    #res = cur.execute(q)

    return res


