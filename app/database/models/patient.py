from sqlmodel import Field, Relationship, SQLModel
from pydantic import EmailStr

class PatientModel(SQLModel, table=True):
    __tablename__="patients"
    
    id: int = Field(default=None, primary_key=True)
    name: str
    email: EmailStr
    hashed_password: str
    
    appointments: list["AppointmentModel"] = Relationship(
        back_populates="appointments",
        sa_relationship_kwargs={"lazy":"selectin"}
    )
    
    consultations: list["ConsultationModel"] = Relationship(
        back_populates="patient",
        sa_relationship_kwargs={"lazy":"selectin"}
    )