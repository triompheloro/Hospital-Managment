from pydantic import BaseModel, ConfigDict, EmailStr

from app.database.models.patient import Sex
    

class PantientCreate(BaseModel):
    name: str 
    sex: Sex
    age: int 
    email: EmailStr
    phone: str 
    password: str
    
    model_config = ConfigDict(from_attributes=True)

class PatientRead(BaseModel):
    name: str 
    sex: Sex
    age: int 
    email: EmailStr
    phone: str 
    
    model_config = ConfigDict(from_attributes=True)