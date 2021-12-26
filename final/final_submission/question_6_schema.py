import mysql_check


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
        create table RACI.Project
        (
            project_id   varchar(255) not null,
            project_name varchar(255) not null,
            start_date   date         null,
            end_date     date         null,
            constraint Project_pk
                primary key (project_id)
        );
    """

    conn = mysql_check.get_connection()
    cur = conn.cursor()
    res = cur.execute(q, [])

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
    create table RACI.Person
    (
        UNI        VARCHAR(255) not null,
        last_name  VARCHAR(255) not null,
        first_name VARCHAR(255) not null,
        email      VARCHAR(255) not null,
        constraint Person_pk
            primary key (UNI)
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
    create table RACI.Roles
    (
        role_id          int          not null,
        role_description VARCHAR(255) not null,
        constraint Roles_pk
            primary key (role_id)
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
    create table RACI.Assignment
    (
        UNI        varchar(255) not null,
        project_id varchar(255) not null,
        role_id    int          not null,
        constraint Assignment_pk
            unique (UNI, project_id),
        constraint Assignment_Person_UNI_fk
            foreign key (UNI) references Person (UNI)
                on update cascade on delete cascade,
        constraint Assignment_Project_project_id_fk
            foreign key (project_id) references Project (project_id)
                on update cascade on delete cascade,
        constraint Assignment_Roles_role_id_fk
            foreign key (role_id) references Roles (role_id)
                on update cascade on delete cascade
    );
    """

    conn = mysql_check.get_connection()
    cur = conn.cursor()
    res = cur.execute(q)

    return res


def schema_operation_5():
    """
    This is an example of what your answers should look like.
    :param country:
    :return:
    """

    res = None

    # You may need to set the connection info. I do just to be safe.
    mysql_check.set_connect_info("root", "password", "127.0.0.1")

    q = """
    create table RACI.Accountable
    (
        project_id varchar(255) not null
            primary key,
        UNI        varchar(255) not null,
        constraint Accountable_Person_UNI_fk
            foreign key (UNI) references Person (UNI)
                on update cascade on delete cascade,
        constraint Accountable_Project_project_id_fk
            foreign key (project_id) references Project (project_id)
                on update cascade on delete cascade
    );
    """

    conn = mysql_check.get_connection()
    cur = conn.cursor()
    res = cur.execute(q)

    return res
