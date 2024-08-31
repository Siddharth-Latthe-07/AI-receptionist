from app.emergency_vectors import search_emergency
from qdrant_client import QdrantClient

def process_emergency(emergency, client: QdrantClient):
    emergency_vector = vectorize_emergency(emergency.description)
    next_step = search_emergency(emergency_vector, client)
    return next_step

def search_emergency(emergency_vector, client: QdrantClient):
    response = client.search(
        collection_name="emergencies",
        query_vector=emergency_vector,
        limit=1,
    )
    return response[0].payload["response"]

def store_message(message):
    with open("messages.txt", "a") as f:
        f.write(f"{message.content}\n")

def get_estimated_time(area):
    import random
    return random.randint(5, 20)

def vectorize_emergency(description):
    return [ord(c) for c in description.lower()]
