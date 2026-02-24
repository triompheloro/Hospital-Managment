from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.models.doctor import DoctorModel
from app.services.schemas.doctorSchema import DoctorRead

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
        
        
    