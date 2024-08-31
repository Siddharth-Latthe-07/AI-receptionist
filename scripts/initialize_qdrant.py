from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams
import numpy as np

client = QdrantClient("http://localhost:6333")

# Initialize the collection with vector size and distance metric
client.create_collection(
    collection_name="emergencies",
    vectors_config=VectorParams(size=3, distance=Distance.EUCLID)
)

# Retrieve and print collection information
collection_info = client.get_collection(collection_name="emergencies")

# Define emergencies and their corresponding vectors
emergencies = {
    1: "Perform CPR immediately. Push hard and fast in the center of the chest and provide rescue breaths every 30 compressions.",
    2: "Chew and swallow an aspirin unless allergic. Call emergency services immediately.",
}

embeddings = {
    1: np.array([1.0, 0.0, 0.0]),
    2: np.array([0.0, 1.0, 0.0]),
}

# Insert data into the Qdrant collection
for key, vector in embeddings.items():
    client.upsert(
        collection_name="emergencies",
        points=[
            {
                "id": key,  # Use an integer as the ID
                "vector": vector,
                "payload": {"response": emergencies[key]},
            }
        ],
    )

print("Qdrant initialization complete.")
print("Collection Name:", collection_info)
