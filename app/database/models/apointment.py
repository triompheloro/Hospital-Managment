from sqlmodel import Relationship, SQLModel, Field
from datetime import datetime



from enum import Enum

class AppointmentStatus(Enum):
    pending = "Pending"
    confirmed = "Confirmed"
    canceled = "Canceled"
    done = "Done"



class AppointmentModel(SQLModel, table = True):
    __tablename__ = "appointments"
    
    id: int = Field(default=None, primary_key=True)
    date: datetime
    status: AppointmentStatus
    
    doctor_id: int = Field(foreign_key="doctors.id")
    doctor: "DoctorModel" = Relationship(
        back_populates="appointments",
        sa_relationship_kwargs={
            "lazy":"selectin"
        }
    )
    
    patient_id: int =Field(foreign_key="patients.id")
    patient: "PatientModel" = Relationship(
        back_populates="appointments",
        sa_relationship_kwargs={
            "lazy":"selectin"
        }
    )
    