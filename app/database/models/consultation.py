from sqlmodel import Field, Relationship, SQLModel


class ConsultationModel(SQLModel, table=True):
    __tablename__="consultations"
    
    id : int = Field(default=None, primary_key=True)
    description: str = Field (max_length=1500)
    
    doctor_id: int = Field(foreign_key="doctors.id")
    doctor: "DoctorModel" = Relationship(
        back_populates="consultations",
        sa_relationship_kwargs={"lazy":"selectin"}
    )
    
    patient_id: int = Field(foreign_key="patients.id")
    patient: "PatientModel" = Relationship(
        back_populates="consultations",
        sa_relationship_kwargs={"lazy":"selectin"}
    )