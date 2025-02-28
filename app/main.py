from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import journey_routes
from app.config.firebase_config import init_firebase

# Initialize Firebase
init_firebase()

# Create FastAPI app
app = FastAPI(
    title="Ed-Venture API",
    description="API for managing Journeys, Modules and ",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Ed-Venture API"}


# Include routers
app.include_router(journey_routes.router, prefix="/edventure", tags=["journeys"])
