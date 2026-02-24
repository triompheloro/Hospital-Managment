from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from app.database.models.apointment import AppointmentStatus
from app.services.schemas.doctorSchema import DoctorRead
from app.services.schemas.patientSchema import PatientRead


class AppointmentCreate(BaseModel):
    date: datetime
    status: AppointmentStatus
    doctor_id: int 
    patient_id: int 
    
    model_config = ConfigDict(from_attributes=True)
    
class AppointmentRead(BaseModel):
    date: datetime
    status: AppointmentStatus
    doctor : DoctorRead
    patient : PatientRead
    
    model_config = ConfigDict(from_attributes=True)
    