# main.py
from fastapi import FastAPI, BackgroundTasks
from app.models import Message, EmergencyRequest, Location
from app.utils import process_emergency, store_message, get_estimated_time, generate_dynamic_response

app = FastAPI()

@app.post("/start")
async def start_conversation(content: Message):
    if 'emergency' in content.content.lower():
        return {"response": "Would you like to leave a message?"}
    return {"response": "Is this an emergency? Please confirm." }

@app.post("/emergency")
async def handle_emergency(emergency: EmergencyRequest, background_tasks: BackgroundTasks):
    background_tasks.add_task(process_emergency, emergency)
    return {"response": "I am checking what you should do immediately, meanwhile, can you tell me which area are you located right now?"}

@app.post("/location")
async def handle_location(location: Location):
    eta = get_estimated_time(location.area)
    response = generate_dynamic_response(f"Dr. Adrin will be coming to your location immediately. Estimated time of arrival: {eta} minutes.")
    return {"response": response}

@app.post("/message")
async def handle_message(message: Message):
    store_message(message)
    return {"response": "Thanks for the message, we will forward it to Dr. Adrin"}

@app.post("/confirmation")
async def handle_confirmation(confirmation: dict):
    if confirmation.get("is_emergency", False):
        return {"response": "Please follow these steps while the doctor arrives."}
    return {"response": "Thanks for your message, Dr. Adrin will review it shortly."}
