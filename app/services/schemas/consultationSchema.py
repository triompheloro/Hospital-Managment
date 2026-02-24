from pydantic import BaseModel, ConfigDict, Field

from app.database.models.doctor import DoctorModel
from app.database.models.patient import PatientModel
from app.services.schemas.doctorSchema import DoctorRead
from app.services.schemas.patientSchema import PatientRead

class ConsultationCreate(BaseModel):
    description: str = Field (max_length=1500)
    doctor_id: int
    patient_id: int 
    
    model_config = ConfigDict(from_attributes=True)

class ConsultationRead(BaseModel):
    description: str = Field (max_length=1500)
    doctor: DoctorRead
    patient: PatientRead 
    
    model_config = ConfigDict(from_attributes=True)