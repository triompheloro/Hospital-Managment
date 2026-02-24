from sqlmodel import Field, Relationship, SQLModel
from pydantic import EmailStr

from enum import Enum

class Sex(Enum):
    man = "Man"
    woman = "Woman"

class PatientModel(SQLModel, table=True):
    __tablename__="patients"
    
    id: int = Field(default=None, primary_key=True)
    name: str 
    sex: Sex
    age: int 
    email: EmailStr
    phone: str 
    hashed_password: str
    
    appointments: list["AppointmentModel"] = Relationship(
        back_populates="patient",
        sa_relationship_kwargs={"lazy":"selectin"}
    )
    
    consultations: list["ConsultationModel"] = Relationship(
        back_populates="patient",
        sa_relationship_kwargs={"lazy":"selectin"}
    )