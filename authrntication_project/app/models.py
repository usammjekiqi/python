from pydantic import BaseModel
from typing import Optional

class PatientCreate(BaseModel):
    id: Optional[int] = None
    name: str
    description:  Optional[str] = None