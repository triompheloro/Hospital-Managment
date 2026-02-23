from sqlmodel import Field, Relationship, SQLModel
from pydantic import EmailStr

class DoctorModel(SQLModel, table=True):
    __tablename__="doctors"
    
    id: int = Field(default=None, primary_key=True)
    name: str
    email: EmailStr
    hashed_password: str
    
    specialization_id: int = Field(foreign_key="specializations.id") 
    specialization: "SpecializationModel" = Relationship(
        back_populates="doctors",
        sa_relationship_kwargs={"lazy":"selectin"}
    )
    
    appointments: list["AppointmentModel"] = Relationship(
        back_populates="doctor",
        sa_relationship_kwargs={"lazy":"selectin"}
    )
    
    consultations: list["ConsultationModel"] = Relationship(
        back_populates="doctor",
        sa_relationship_kwargs={"lazy":"selectin"}
    )
    