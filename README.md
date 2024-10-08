# AI-receptionist
##### Overview:
This project implements an AI-based receptionist using FastAPI for handling various interactions and Qdrant for vector-based emergency response handling with LLM. The application provides endpoints to start a conversation, handle emergency requests, store messages, and manage location-based queries. 
##### Features:
1. `/start`: Initiate a conversation and determine if the user needs emergency assistance.
2. `/emergency`: Handle emergency requests and provide instructions based on the user's input.
3. `/location`: Provide the estimated time of arrival for assistance based on the user's location.
4. `/message`: Store a message for further review by a doctor.
5. `/confirmation`: Confirm if the situation is an emergency and provide follow-up steps.

##### Setup:
(generate an openai api key, as it would be required to use LLM response. Placed the same in utlis and config.py files)
##### 1. Clone the Repository
##### 2. setup the env:
Create a .env file in the root directory (if not already present) and add your environment variables.

##### 2. Build and Run Docker Containers
`docker run -d -p 8000:8000 --name ai_receptionist_container ai_receptionist`

`docker run -d --name qdrant -p 6333:6333 qdrant/qdrant`
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
