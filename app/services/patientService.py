from fastapi import HTTPException, status
from passlib.context import CryptContext
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.models.patient import PatientModel
from app.services.schemas.patientSchema import PantientCreate, PatientRead

passwordContext = CryptContext(schemes=["bcrypt"], deprecated='auto')


class PatientService:
    def __init__(self, session: AsyncSession):
        self.session = session
        
    
    async def get_patient_by_id(self, id: int) -> PatientRead:
        patient = await self.session.get(PatientModel, id)
        
        if patient is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Patient not found"
            )
            
        return PatientRead.model_validate(patient)
    
    async def create_new_patient(self, patient: PantientCreate) -> PatientRead:
        new_patient = PatientModel(
            **patient.model_dump(exclude=["password"]),
            hashed_password=passwordContext.hash(patient.password)
        )
        
        self.session.add(new_patient)
        await self.session.commit()
        await self.session.refresh(new_patient)
        
        return PatientRead.model_validate(new_patient)
    
    async def update_patient_profile_by_id(self, id: int, new_data: dict) -> PatientRead:
        patient = await self.session.get(PatientModel,id)
        
        if patient is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Patient not found"
            )
        
        patient_dict = {
            **patient.model_dump()
        }
        patient_dict.update(new_data)
        
        patient.sqlmodel_update(patient_dict)
        
        self.session.add(patient)
        await self.session.commit()
        await self.session.refresh(patient)
        
        return PatientRead.model_validate(patient)
    
    async def delete_patient_by_id(self, id:int) -> dict:
        patient = await self.session.get(PatientModel, id)
        
        if patient is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Patient not found"
            )
            
        await self.session.delete(patient)
        await self.session.commit()
        
        return {
            "detail": "Patient deleted succesfully"
        }