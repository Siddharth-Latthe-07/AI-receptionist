# AI-receptionist
##### Overview:
This project implements an AI-based receptionist using FastAPI for handling various interactions and Qdrant for vector-based emergency response handling. The application provides endpoints to start a conversation, handle emergency requests, store messages, and manage location-based queries. 
##### Features:
1. `/start`: Initiate a conversation and determine if the user needs emergency assistance.
2. `/emergency`: Handle emergency requests and provide instructions based on the user's input.
3. `/location`: Provide the estimated time of arrival for assistance based on the user's location.
4. `/message`: Store a message for further review by a doctor.
5. `/confirmation`: Confirm if the situation is an emergency and provide follow-up steps.

##### Setup:
##### 1. Clone the Repository
##### 2. Build and Run Docker Containers
##### 3. Initialize Qdrant Database
`docker exec -it ai_receptionist_container python scripts/initialize_qdrant.py`
##### 4. To run the main.py:
`pip install -e .`
`uvicorn app.main:app --reload`
##### 4. Access the Application
API Documentation: `http://localhost:8000/docs (Swagger UI)`
Qdrant status check: `http://localhost:6333/collections/emergencies`
##### 5. Swagger UI
Once the application is running, you can interact with it using the Swagger UI at http://localhost:8000/docs. The Swagger UI provides a web-based interface to test all the available endpoints, view the expected inputs and outputs, and see the detailed API documentation.
##### 6. Sample Requests
```/start
Input: {"content": "I need help"}
Response: {"response": "Would you like to leave a message?"}
```
```/emergency
Input: {"description": "Heart attack"}
Response: {"response": "I am checking what you should do immediately, meanwhile, can you tell me which area are you located right now?"}
```
