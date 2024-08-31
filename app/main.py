from fastapi import FastAPI, BackgroundTasks, Form
from qdrant_client import QdrantClient
from app.models import Message, EmergencyRequest, Location
from app.utils import process_emergency, store_message, get_estimated_time
import time

app = FastAPI()

# Initialize Qdrant client
client = QdrantClient("http://localhost:6333")

@app.post("/start")
async def start_conversation(background_tasks: BackgroundTasks, content: str = Form(...)):
    if 'emergency' in content.lower():
        return {"response": "Would you like to leave a message?"}
    return {"response": "Is this an emergency? Please confirm."}

@app.post("/emergency")
async def handle_emergency(background_tasks: BackgroundTasks, description: str = Form(...)):
    emergency = EmergencyRequest(description=description)
    background_tasks.add_task(slow_process_emergency, emergency)
    return {"response": "I am checking what you should do immediately, meanwhile, can you tell me which area are you located right now?"}

async def slow_process_emergency(emergency: EmergencyRequest):
    time.sleep(5)  # Simulate a delay in processing
    response = process_emergency(emergency, client)  # Interact with Qdrant
    return response

@app.post("/location")
async def handle_location(background_tasks: BackgroundTasks, area: str = Form(...)):
    location = Location(area=area)
    eta = get_estimated_time(location.area)
    return {"response": f"Dr. Adrin will be coming to your location immediately. Estimated time of arrival: {eta} minutes."}

@app.post("/message")
async def handle_message(background_tasks: BackgroundTasks, content: str = Form(...)):
    message = Message(content=content)
    store_message(message)
    return {"response": "Thanks for the message, we will forward it to Dr. Adrin"}

@app.post("/confirmation")
async def handle_confirmation(background_tasks: BackgroundTasks, is_emergency: bool = Form(...)):
    if is_emergency:
        return {"response": "Please follow these steps while the doctor arrives."}
    return {"response": "Thanks for your message, Dr. Adrin will review it shortly."}
