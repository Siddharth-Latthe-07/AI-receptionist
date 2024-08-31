# emergency_vectors.py
from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct, Filter
from app.config import QDRANT_HOST, QDRANT_PORT

client = QdrantClient(host=QDRANT_HOST, port=QDRANT_PORT)

def search_emergency(query_vector):
    results = client.search(
        collection_name="emergencies",
        query_vector=query_vector,
        limit=1
    )
    if results:
        return results[0].payload['next_step']
    return "No specific instructions found, please wait for the doctor."

def add_emergency_vectors(vectors):
    points = [
        PointStruct(id=i, vector=vector['vector'], payload=vector['payload'])
        for i, vector in enumerate(vectors)
    ]
    client.upsert(
        collection_name="emergencies",
        points=points
    )
