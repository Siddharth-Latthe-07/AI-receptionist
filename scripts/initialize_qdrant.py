# initialize_qdrant.py
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
import numpy as np

client = QdrantClient("http://localhost:6333")

client.recreate_collection(
    collection_name="emergencies",
    vectors_config=VectorParams(size=256, distance=Distance.COSINE)
)

emergencies = {
    1: "Perform CPR immediately. Push hard and fast in the center of the chest and provide rescue breaths every 30 compressions.",
    2: "Chew and swallow an aspirin unless allergic. Call emergency services immediately.",
}

# Simple vector embeddings for emergencies
embeddings = {
    1: np.random.rand(256),
    2: np.random.rand(256),
}

# Insert data into the Qdrant collection
for key, vector in embeddings.items():
    client.upsert(
        collection_name="emergencies",
        points=[
            PointStruct(
                id=key,
                vector=vector.tolist(),
                payload={"response": emergencies[key]},
            )
        ],
    )

print("Qdrant initialization complete.")
