from pydantic import BaseModel, EmailStr, ConfigDict

class DoctorCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    specialization_id: int 
    
    model_config = ConfigDict(from_attributes=True)
    
class DoctorRead(BaseModel):
    name: str
    email: EmailStr
    specialization_id: int 
    
    model_config = ConfigDict(from_attributes=True)