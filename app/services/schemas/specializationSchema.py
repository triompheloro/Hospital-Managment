from pydantic import BaseModel, ConfigDict, Field

class SpecializationSchema(BaseModel):
    title: str = Field(max_length=100)
    
    model_config = ConfigDict(from_attributes=True)