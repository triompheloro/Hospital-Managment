from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from app.database.models.apointment import AppointmentStatus
from app.database.models.doctor import DoctorModel
from app.database.models.patient import PatientModel


class AppointmentCreate(BaseModel):
    date: datetime
    status: AppointmentStatus
    doctor_id: int 
    patient_id: int 
    
    model_config = ConfigDict(from_attributes=True)
    
class AppointmentRead(BaseModel):
    date: datetime
    status: AppointmentStatus
    doctor : DoctorModel
    patient : PatientModel
    
    model_config = ConfigDict(from_attributes=True)
    