# utils.py
import openai
import random
from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct, Filter, FieldCondition, MatchValue
from app.config import QDRANT_HOST, QDRANT_PORT, OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def process_emergency(emergency):
    client = QdrantClient(QDRANT_HOST, port=QDRANT_PORT)
    vector = vectorize_emergency(emergency.description)
    response_point = search_emergency(client, vector)
    return response_point.payload["response"]

def vectorize_emergency(description: str):
    return [ord(c) / 100 for c in description.lower()]

def search_emergency(client, vector):
    search_result = client.search(
        collection_name="emergencies",
        query_vector=vector,
        limit=1,
    )
    return search_result[0] if search_result else None

def generate_dynamic_response(prompt: str):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=50,
    )
    return response.choices[0].text.strip()

def store_message(message):
    with open("messages.txt", "a") as f:
        f.write(f"{message.content}\n")

def get_estimated_time(area: str):
    return random.randint(5, 20)
