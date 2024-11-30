from neo4j import GraphDatabase
from config import NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD

class MemoryAgent:
    def __init__(self):
        self.driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
    
    def store_user_preference(self, user_id, user_details):
        session = self.driver.session()
        session.run(
            "MERGE (u:User {id: $user_id}) "
            "SET u.destination = $destination, u.interests = $interests, u.budget = $budget, u.start_location = $start_location",
            user_id=user_id, 
            destination=user_details["destination"],
            interests=", ".join(user_details["interests"]),
            budget=user_details["budget"],
            start_location=user_details["start_location"]
        )
        session.close()

    def get_user_preference(self, user_id):
        session = self.driver.session()
        result = session.run("MATCH (u:User {id: $user_id}) RETURN u", user_id=user_id)
        session.close()
        return result.single() if result.single() else None
