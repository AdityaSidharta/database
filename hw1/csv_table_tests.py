"""

csv_table_tests.py

"""

from src.CSVDataTable import CSVDataTable

import os
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
data_dir = os.path.abspath("../data/Baseball")


def tests_people():
    connect_info = {
        "directory": data_dir,
        "file_name": "People.csv"
    }
    people = CSVDataTable("People", connect_info, ["playerID"])
    try:

        print()
        print("find_by_primary_key(): Known Record")
        print(people.find_by_primary_key(["aardsda01"]))

        print()
        print("find_by_primary_key(): Unknown Record")
        print(people.find_by_primary_key((["cah2251"])))

        print()
        print("find_by_template(): Known Template")
        template = {"nameFirst": "David", "nameLast": "Aardsma", "nameGiven": "David Allan"}
        print(people.find_by_template(template))

        print()
        print("find_by_template(): Unknown Template")
        template = {"nameFirst": "Fake", "nameLast": "Fake", "nameGiven": "Fake Fake"}
        print(people.find_by_template(template))

        print()
        print("delete_by_key(): Known Record")
        print(people.delete_by_key(["aardsda01"]))

        print()
        print("delete_by_key(): Unknown Record")
        print(people.delete_by_key("cah2251"))

        print()
        print("delete_by_template(): Known Template")
        template = {"nameFirst": "Jonah", "nameLast": "Bayliss", "nameGiven": "Jonah James"}
        print(people.delete_by_template(template))

        print()
        print("delete_by_template(): Unknown Template")
        template = {"nameFirst": "Fake", "nameLast": "Fake", "nameGiven": "Fake Fake"}
        print(people.delete_by_template(template))

        print()
        print("update_by_key(): Known Record - Change nameGiven to add Dr.")
        print(people.find_by_primary_key(['aaronha01']))
        print(people.update_by_key(['aaronha01'], {
            'nameGiven': 'Dr. Henry Louis'
        }))
        print(people.find_by_primary_key(['aaronha01']))

        print()
        print("update_by_key(): Unknown Record")
        print(people.update_by_key(['fake01'], {
            'nameGiven': 'Dr. Henry Louis'
        }))

        print()
        print("update_by_key(): Known Record, Problematic Primary Key")
        print(people.find_by_primary_key(['aaronha01']))
        print(people.update_by_key(['aaronha01'], {
            'playerID': 'aaronto01'
        }))
        print(people.find_by_primary_key(['aaronha01']))

        print()
        print("update_by_template(): Known Record - Change nameGiven to add Dr.")
        template = {"nameFirst": "Tommie", "nameLast": "Aaron"}
        print(people.find_by_template(template))
        print(people.update_by_template(template, {
            'nameGiven': 'Dr. Tommie Lee'
        }))
        print(people.find_by_template(template))

        print()
        print("update_by_template(): Unknown Record")
        template = {"nameFirst": "Fake", "nameLast": "Fake", "nameGiven": "Fake Fake"}
        print(people.update_by_template(template, {
            'nameGiven': 'Dr. Henry Louis'
        }))

        print()
        print("update_by_template(): Known Record, Problematic Primary Key")
        template = {"nameFirst": "Tommie", "nameLast": "Aaron"}
        print(people.find_by_template(template))
        print(people.update_by_template(template, {
            'playerID': 'aaronha01'
        }))
        print(people.find_by_template(template))

        print()
        print("insert(): Success")
        print(len(people._rows))
        print(people.insert({'playerID': 'aaronto02',
                             'birthYear': '1939',
                             'birthMonth': '8',
                             'birthDay': '5',
                             'birthCountry': 'USA',
                             'birthState': 'AL',
                             'birthCity': 'Mobile',
                             'deathYear': '1984',
                             'deathMonth': '8',
                             'deathDay': '16',
                             'deathCountry': 'USA',
                             'deathState': 'GA',
                             'deathCity': 'Atlanta',
                             'nameFirst': 'Tommie',
                             'nameLast': 'Aaron',
                             'nameGiven': 'Tommie Lee II',
                             'weight': '190',
                             'height': '75',
                             'bats': 'R',
                             'throws': 'R',
                             'debut': '1962-04-10',
                             'finalGame': '1971-09-26',
                             'retroID': 'aarot101',
                             'bbrefID': 'aaronto01'}))

        print(len(people._rows))

        print()
        print("insert(): Duplicate Primary Key")
        print(len(people._rows))
        print(people.insert({'playerID': 'aaronto01',
                             'birthYear': '1939',
                             'birthMonth': '8',
                             'birthDay': '5',
                             'birthCountry': 'USA',
                             'birthState': 'AL',
                             'birthCity': 'Mobile',
                             'deathYear': '1984',
                             'deathMonth': '8',
                             'deathDay': '16',
                             'deathCountry': 'USA',
                             'deathState': 'GA',
                             'deathCity': 'Atlanta',
                             'nameFirst': 'Tommie',
                             'nameLast': 'Aaron',
                             'nameGiven': 'Tommie Lee II',
                             'weight': '190',
                             'height': '75',
                             'bats': 'R',
                             'throws': 'R',
                             'debut': '1962-04-10',
                             'finalGame': '1971-09-26',
                             'retroID': 'aarot101',
                             'bbrefID': 'aaronto01'}))

    except Exception as e:
        print("An error occurred:", e)
        print(len(people._rows))


def tests_batting():
    connect_info = {
        "directory": data_dir,
        "file_name": "Batting.csv"
    }
    people = CSVDataTable("Batting", connect_info, ["playerID", 'yearID', 'stint'])
    try:

        print()
        print("find_by_primary_key(): Known Record")
        print(people.find_by_primary_key(['abercda01','1871','1']))

        print()
        print("find_by_primary_key(): Unknown Record")
        print(people.find_by_primary_key((["fake", 'fake', 'fake'])))

        print()
        print("find_by_template(): Known Template")
        template = {"playerID": "abercda01", "yearID": "1871", "stint": "1"}
        print(people.find_by_template(template))

        print()
        print("find_by_template(): Unknown Template")
        template = {"playerID": "fake", "yearID": "fake", "stint": "fake"}
        print(people.find_by_template(template))

        print()
        print("delete_by_key(): Known Record")
        print(people.delete_by_key(['abercda01','1871','1']))

        print()
        print("delete_by_key(): Unknown Record")
        print(people.delete_by_key([['fake','fake','fake']]))

        print()
        print("delete_by_template(): Known Template")
        template = {"playerID": "addybo01", "yearID": "1871", "stint": "1"}
        print(people.delete_by_template(template))

        print()
        print("delete_by_template(): Unknown Template")
        template = {"playerID": "fake", "yearID": "fake", "stint": "fake"}
        print(people.delete_by_template(template))

        print()
        print("update_by_key(): Known Record - Change teamID to Columbia")
        print(people.find_by_primary_key(['allisar01','1871','1']))
        print(people.update_by_key(['allisar01','1871','1'], {
            'teamID': 'COLUMBIA'
        }))
        print(people.find_by_primary_key(['allisar01','1871','1']))

        print()
        print("update_by_key(): Unknown Record")
        print(people.update_by_key(['fake','fake','fake'], {
            'teamID': 'COLUMBIA'
        }))

        print()
        print("update_by_key(): Known Record, Problematic Primary Key")
        print(people.find_by_primary_key(['allisar01','1871','1']))
        print(people.update_by_key(['allisar01','1871','1'], {
            'playerID': 'allisdo01'
        }))
        print(people.find_by_primary_key(['allisar01','1871','1']))

        print()
        print("update_by_template(): Known Record - Change teamID to Columbia")
        template = {"playerID": "allisdo01", "yearID": "1871", "stint": "1"}
        print(people.find_by_template(template))
        print(people.update_by_template(template, {
            'teamID': 'COLUMBIA'
        }))
        print(people.find_by_template(template))

        print()
        print("update_by_template(): Unknown Record")
        template = {"playerID": "fake", "yearID": "fake", "stint": "fake"}
        print(people.update_by_template(template, {
            'teamID': 'COLUMBIA'
        }))

        print()
        print("update_by_template(): Known Record, Problematic Primary Key")
        template = {"playerID": "allisdo01", "yearID": "1871", "stint": "1"}
        print(people.find_by_template(template))
        print(people.update_by_template(template, {
            'playerID': 'allisar01'
        }))
        print(people.find_by_template(template))

        print()
        print("insert(): Success")
        print(len(people._rows))
        print(people.insert({'playerID': 'zuninmi02',
                             'yearID': '2018',
                             'stint': '1',
                             'teamID': 'SEA',
                             'lgID': 'AL',
                             'G': '113',
                             'AB': '373',
                             'R': '37',
                             'H': '75',
                             '2B': '18',
                             '3B': '0',
                             'HR': '20',
                             'RBI': '44',
                             'SB': '0',
                             'CS': '0',
                             'BB': '24',
                             'SO': '150',
                             'IBB': '0',
                             'HBP': '6',
                             'SH': '0',
                             'SF': '2',
                             'GIDP': '7'}))

        print(len(people._rows))

        print()
        print("insert(): Duplicate Primary Key")
        print(len(people._rows))
        print(people.insert({'playerID': 'zuninmi01',
                             'yearID': '2018',
                             'stint': '1',
                             'teamID': 'SEA',
                             'lgID': 'AL',
                             'G': '113',
                             'AB': '373',
                             'R': '37',
                             'H': '75',
                             '2B': '18',
                             '3B': '0',
                             'HR': '20',
                             'RBI': '44',
                             'SB': '0',
                             'CS': '0',
                             'BB': '24',
                             'SO': '150',
                             'IBB': '0',
                             'HBP': '6',
                             'SH': '0',
                             'SF': '2',
                             'GIDP': '7'}))

    except Exception as e:
        print("An error occurred:", e)
        print(len(people._rows))


tests_people()
tests_batting()
