from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from passlib.context import CryptContext

from app.database.models.doctor import DoctorModel
from app.services.schemas.doctorSchema import DoctorCreate, DoctorRead

passwordContext = CryptContext(schemes=['bcrypt'], deprecated='auto')

class DoctorService:
    def __init__(self, session: AsyncSession):
        self.session = session
        
    
    async def get_doctor_by_id(self,id: int) -> DoctorRead:
        doctor = await self.session.get(DoctorModel,id)
        
        if doctor is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Doctor not found"
            )
        
        return DoctorRead.model_validate(doctor)
    
    async def create_new_doctor(self, doctor : DoctorCreate) -> DoctorRead:
        new_doctor = DoctorModel(
            **doctor.model_dump(exclude=["password"]),
            hashed_password=passwordContext.hash(doctor.password)
        )
        
        self.session.add(new_doctor)
        await self.session.commit()
        await self.session.refresh(new_doctor)
        
        return DoctorRead.model_validate(new_doctor)
    
    async def update_doctor_by_id(self, id: int, new_data: dict) -> DoctorRead:
        doctor = await self.session.get(DoctorModel, id)
        
        if doctor is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Doctor not found"
            )
            
        doctor_dict = {
            **doctor.model_dump()
        }
        doctor_dict.update(new_data)
        
        doctor.sqlmodel_update(doctor_dict)
        
        self.session.add(doctor)
        await self.session.commit()
        await self.session.refresh(doctor)
        
        return DoctorRead.model_validate(doctor)
    
    async def delete_doctor_by_id(self, id: int) ->dict:
        doctor = await self.session.get(DoctorModel,id)
        
        if doctor is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Doctor not found"
            )
        
        await self.session.delete(doctor)
        await self.session.commit()
        
        return {
            "detail": "Doctor deletaed succesfully"
        }
        
        
        
        
    