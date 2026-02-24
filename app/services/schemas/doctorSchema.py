from pydantic import BaseModel, EmailStr, ConfigDict

from app.database.models.specialization import SpecializationModel

class DoctorCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    specialization_id: int 
    
    model_config = ConfigDict(from_attributes=True)
    
class DoctorRead(BaseModel):
    name: str
    email: EmailStr
    specialization: SpecializationModel 
    
    model_config = ConfigDict(from_attributes=True)