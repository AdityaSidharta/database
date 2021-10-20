import CSVTable
import CSVCatalog
import json
import csv

#Must clear out all tables in CSV Catalog schema before using if there are any present
#Please change the path name to be whatever the path to the CSV files are
#First methods set up metadata!! Very important that all of these be run properly

# Only need to run these if you made the tables already in your CSV Catalog tests
# You will not need to include the output in your submission as executing this is not required
# Implementation is provided
def drop_tables_for_prep():
    cat = CSVCatalog.CSVCatalog(
        dbhost="127.0.0.1",
        dbport=3306,
        dbuser="root",
        dbpw="password",
        db="CSVCatalog")
    cat.drop_table("people")
    cat.drop_table("batting")
    cat.drop_table("appearances")

#drop_tables_for_prep()

# Implementation is provided
# You will need to update these with the correct path
def create_lahman_tables():
    cat = CSVCatalog.CSVCatalog(
        dbhost="127.0.0.1",
        dbport=3306,
        dbuser="root",
        dbpw="password",
        db="CSVCatalog")
    cat.create_table("people", "People.csv")
    cat.create_table("batting","Batting.csv")
    cat.create_table("appearances", "Appearances.csv")

#create_lahman_tables()

# Note: You can default all column types to text
def update_people_columns():
    cat = CSVCatalog.CSVCatalog(
        dbhost="127.0.0.1",
        dbport=3306,
        dbuser="root",
        dbpw="password",
        db="CSVCatalog")

    t = cat.get_table("people")
    for colname in ['playerID','birthYear','birthMonth','birthDay','birthCountry','birthState','birthCity','deathYear','deathMonth','deathDay','deathCountry','deathState','deathCity','nameFirst','nameLast','nameGiven','weight','height','bats','throws','debut','finalGame','retroID','bbrefID']:
        col = CSVCatalog.ColumnDefinition(colname, "text", False)
        t.add_column_definition(col)
    print("Table = ", t)

#update_people_columns()

def update_appearances_columns():
    # ************************ TO DO ***************************
    cat = CSVCatalog.CSVCatalog(
        dbhost="127.0.0.1",
        dbport=3306,
        dbuser="root",
        dbpw="password",
        db="CSVCatalog")

    t = cat.get_table("appearances")
    for colname in ['yearID','teamID','lgID','playerID','G_all','GS','G_batting','G_defense','G_p','G_c','G_1b','G_2b','G_3b','G_ss','G_lf','G_cf','G_rf','G_of','G_dh','G_ph','G_pr']:
        col = CSVCatalog.ColumnDefinition(colname, "text", False)
        t.add_column_definition(col)
    print("Table = ", t)

#update_appearances_columns()

def update_batting_columns():
    # ************************ TO DO ***************************
    cat = CSVCatalog.CSVCatalog(
        dbhost="127.0.0.1",
        dbport=3306,
        dbuser="root",
        dbpw="password",
        db="CSVCatalog")

    t = cat.get_table("batting")
    for colname in ['playerID','yearID','stint','teamID','lgID','G','AB','R','H','2B','3B','HR','RBI','SB','CS','BB','SO','IBB','HBP','SH','SF','GIDP']:
        col = CSVCatalog.ColumnDefinition(colname, "text", False)
        t.add_column_definition(col)
    print("Table = ", t)

#update_batting_columns()

#Add primary key indexes for people, batting, and appearances in this test
def add_index_definitions():
    # ************************ TO DO ***************************
    cat = CSVCatalog.CSVCatalog(
        dbhost="127.0.0.1",
        dbport=3306,
        dbuser="root",
        dbpw="password",
        db="CSVCatalog")

    i = CSVCatalog.IndexDefinition(
        index_name = 'battingprimary',
        index_type = 'PRIMARY',
        column_names = ['playerID','yearID','stint']
    )
    t = cat.get_table("batting")
    t.define_index(i.index_name, i.column_names, i.index_type)
    print("Table = ", t)

    i = CSVCatalog.IndexDefinition(
        index_name = 'appearancesprimary',
        index_type = 'PRIMARY',
        column_names = ['yearID','teamID','playerID']
    )
    t = cat.get_table("appearances")
    t.define_index(i.index_name, i.column_names, i.index_type)
    print("Table = ", t)

    i = CSVCatalog.IndexDefinition(
        index_name = 'peopleprimary',
        index_type = 'PRIMARY',
        column_names = ['playerID']
    )
    t = cat.get_table("people")
    t.define_index(i.index_name, i.column_names, i.index_type)
    print("Table = ", t)

#add_index_definitions()


def test_load_info():
    table = CSVTable.CSVTable("people")
    print(table.__description__.file_name)

#test_load_info()

def test_get_col_names():
    table = CSVTable.CSVTable("people")
    names = table.__get_column_names__()
    print(names)

#test_get_col_names()

def add_other_indexes():
    """
    We want to add indexes for common user stories
    People: nameLast, nameFirst
    Batting: teamID
    Appearances: None that are too important right now
    :return:
    """
    # ************************ TO DO ***************************
    cat = CSVCatalog.CSVCatalog(
        dbhost="127.0.0.1",
        dbport=3306,
        dbuser="root",
        dbpw="password",
        db="CSVCatalog")

    i = CSVCatalog.IndexDefinition(
        index_name = 'battingindex',
        index_type = 'INDEX',
        column_names = ['teamID']
    )
    t = cat.get_table("batting")
    t.define_index(i.index_name, i.column_names, i.index_type)
    print("Table = ", t)

    i = CSVCatalog.IndexDefinition(
        index_name = 'peopleindex',
        index_type = 'INDEX',
        column_names = ['nameLast', 'nameFirst']
    )
    t = cat.get_table("people")
    t.define_index(i.index_name, i.column_names, i.index_type)
    print("Table = ", t)


#add_other_indexes()

def load_test():
    batting_table = CSVTable.CSVTable("batting")
    print(batting_table)

#load_test()


def dumb_join_test():
    batting_table = CSVTable.CSVTable("batting")
    appearances_table = CSVTable.CSVTable("appearances")
    result = batting_table.dumb_join(appearances_table, ["playerID", "yearID"], {"playerID": "barrebi01"},
                                     ["playerID", "yearID", "teamID", "AB", "H", "G_all", "G_batting"])
    print(result)


#dumb_join_test()


def get_access_path_test():
    batting_table = CSVTable.CSVTable("batting")
    template = {"stint" : '1',
     "playerID" : 'abercda01',
      "yearID" : '1871'}
    index_result, count = batting_table.__get_access_path__(template)
    print(index_result)
    print(count)

#get_access_path_test()

def sub_where_template_test():
    # ************************ TO DO ***************************
    batting_table = CSVTable.CSVTable("batting")
    result = batting_table.__get_sub_where_template__(where_template={'playerID': 'adi', 'foo': 'bar'})
    print(result)

#sub_where_template_test()


def test_find_by_template_index():
    # ************************ TO DO ***************************
    batting_table = CSVTable.CSVTable("batting")
    template = {"stint" : '1',
     "playerID" : 'abercda01',
      "yearID" : '1871'}
    idx_name = ('battingprimary', 'abercda01_1871_1')
    result = batting_table.__find_by_template_index__(template, idx_name)
    print(result)

#test_find_by_template_index()

def smart_join_test():
    # ************************ TO DO ***************************
    batting_table = CSVTable.CSVTable("batting")
    appearances_table = CSVTable.CSVTable("appearances")
    result = batting_table.__smart_join__(appearances_table, ["playerID", "yearID"], {"playerID": "barrebi01"},
                                     ["playerID", "yearID", "teamID", "AB", "H", "G_all", "G_batting"])
    print(result)

#smart_join_test()
