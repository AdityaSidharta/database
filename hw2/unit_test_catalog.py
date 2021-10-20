import CSVCatalog
import json


# Example test, you will have to update the connection info
# Implementation Provided
def create_table_test():
    cat = CSVCatalog.CSVCatalog(
        dbhost="127.0.0.1",
        dbport=3306,
        dbuser="root",
        dbpw="adit2511",
        db="CSVCatalog")
    cat.create_table("test_table", "file_path_test.woo")
    t = cat.get_table("test_table")
    print("Table = ", t)

#create_table_test()

def drop_table_test():
    # ************************ TO DO ***************************
    cat = CSVCatalog.CSVCatalog(
        dbhost="127.0.0.1",
        dbport=3306,
        dbuser="root",
        dbpw="adit2511",
        db="CSVCatalog")
    cat.drop_table("test_table")
    t = cat.get_table("test_table")
    print("Table = ", t)


#drop_table_test()

def add_column_test():
    # ************************ TO DO ***************************
    cat = CSVCatalog.CSVCatalog(
        dbhost="127.0.0.1",
        dbport=3306,
        dbuser="root",
        dbpw="adit2511",
        db="CSVCatalog")
    col = CSVCatalog.ColumnDefinition("foo", "text", False)
    t = cat.get_table("test_table")
    t.add_column_definition(col)
    print("Table = ", t)


#add_column_test()

# Implementation Provided
# Fails because no name is given
def column_name_failure_test():
    cat = CSVCatalog.CSVCatalog(
        dbhost="127.0.0.1",
        dbport=3306,
        dbuser="root",
        dbpw="adit2511",
        db="CSVCatalog")
    col = CSVCatalog.ColumnDefinition(None, "text", False)
    t = cat.get_table("test_table")
    t.add_column_definition(col)

#column_name_failure_test()

# Implementation Provided
# Fails because "canary" is not a permitted type
def column_type_failure_test():
    cat = CSVCatalog.CSVCatalog(
        dbhost="127.0.0.1",
        dbport=3306,
        dbuser="root",
        dbpw="adit2511",
        db="CSVCatalog")
    col = CSVCatalog.ColumnDefinition("bird", "canary", False)
    t = cat.get_table("test_table")
    t.add_column_definition(col)

#column_type_failure_test()

# Implementation Provided
# Will fail because "happy" is not a boolean
def column_not_null_failure_test():
    cat = CSVCatalog.CSVCatalog(
        dbhost="127.0.0.1",
        dbport=3306,
        dbuser="root",
        dbpw="adit2511",
        db="CSVCatalog")
    col = CSVCatalog.ColumnDefinition("name", "text", "happy")
    t = cat.get_table("test_table")
    t.add_column_definition(col)

#column_not_null_failure_test()


def add_index_test():
    # ************************ TO DO ***************************
    cat = CSVCatalog.CSVCatalog(
        dbhost="127.0.0.1",
        dbport=3306,
        dbuser="root",
        dbpw="adit2511",
        db="CSVCatalog")
    col = CSVCatalog.ColumnDefinition("bar", "text", False)
    i = CSVCatalog.IndexDefinition(
        index_name = 'barunique',
        index_type = 'UNIQUE',
        column_names = ["bar"]
    )
    t = cat.get_table("test_table")
    t.add_column_definition(col)
    t.define_index(i.index_name, i.column_names, i.index_type)
    print("Table = ", t)

#add_index_test()


def col_drop_test():
    # ************************ TO DO ***************************
    cat = CSVCatalog.CSVCatalog(
        dbhost="127.0.0.1",
        dbport=3306,
        dbuser="root",
        dbpw="adit2511",
        db="CSVCatalog")
    col = CSVCatalog.ColumnDefinition("foo", "text", False)
    t = cat.get_table("test_table")
    t.drop_column_definition(col)
    print("Table = ", t)


#col_drop_test()

def index_drop_test():
    # ************************ TO DO ***************************
    cat = CSVCatalog.CSVCatalog(
        dbhost="127.0.0.1",
        dbport=3306,
        dbuser="root",
        dbpw="adit2511",
        db="CSVCatalog")
    i = CSVCatalog.IndexDefinition(
        index_name = 'barunique',
        index_type = 'UNIQUE',
        column_names = ['bar']
    )
    t = cat.get_table("test_table")
    t.drop_index(i.index_name)
    print("Table = ", t)

#index_drop_test()

# Implementation provided
def describe_table_test():
    cat = CSVCatalog.CSVCatalog(
        dbhost="127.0.0.1",
        dbport=3306,
        dbuser="root",
        dbpw="adit2511",
        db="CSVCatalog")
    t = cat.get_table("test_table")
    desc = t.describe_table()
    print("DESCRIBE People = \n", json.dumps(desc, indent = 2))

#describe_table_test()

