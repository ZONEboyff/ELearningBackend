from pydantic import BaseModel
from typing import List

class JourneySchema(BaseModel):
    name: str
    difficulty: str
