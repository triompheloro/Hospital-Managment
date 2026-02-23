from sqlmodel import Field, Relationship, SQLModel


class SpecializationModel(SQLModel, table=True):
    __tablename__ = "specializations"
    
    id: int = Field(default=None, primary_key=True)
    title: str = Field(max_length=100)
    
    doctors : list["DoctorModel"] = Relationship(
        back_populates="specialization",
        sa_relationship_kwargs={"lazy":"selectin"}
    )