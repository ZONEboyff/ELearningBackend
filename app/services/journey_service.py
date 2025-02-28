from app.database.firebase import FirebaseDB
from app.models.schemas import JourneySchema

class JourneyService:

    def __init__(self, db: FirebaseDB):
        self.db = db

    async def get_all_journeys(self) -> list:
        return await self.db.get_all_documents("journey")

    async def create_journey(self, journey: JourneySchema) -> JourneySchema:
        await self.db.create_document("journey", journey.dict()["name"], journey.dict())
        return {"message": "Journey created successfully"}
    

    
    