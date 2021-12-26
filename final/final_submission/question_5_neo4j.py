import py2neo
import pandas as pd
import neo4j_check


def directed_tom_hanks():

    neo4j_check.set_neo4j_connect_info("neo4j", "password")

    q = """
    match (n)-[:ACTED_IN]->(m)<-[:DIRECTED]-(n2) where n.name="Tom Hanks" return n.name, m.title, n2.name
    """
    gr = neo4j_check.get_graph()

    result = gr.run(q)
    result = pd.DataFrame(result)

    return result


def directed_themselves():


    neo4j_check.set_neo4j_connect_info("neo4j", "password")

    q = """
    match (n)-[:ACTED_IN]->(m)<-[:DIRECTED]-(n2) where n.name=n2.name return n.name, m.title, n2.name
    """
    gr = neo4j_check.get_graph()

    result = gr.run(q)
    result = pd.DataFrame(result)
    result = result.drop_duplicates()
    return result

def both_reviewed(person_1_name, person_2_name):

    neo4j_check.set_neo4j_connect_info("neo4j", "password")

    q = """
    match (n)-[:REVIEWED]->(m)<-[:REVIEWED]-(n2) where (n.name = "{}" and n2.name = "{}") return n.name, m.title, n2.name
    """.format(person_1_name, person_2_name)
    gr = neo4j_check.get_graph()

    result = gr.run(q)
    result = pd.DataFrame(result)
    result = result.drop_duplicates()
    return result


