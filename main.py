from fastapi import FastAPI
from routes.backendapi import router as memory_route
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()
app.include_router(memory_route)