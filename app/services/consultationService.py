from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.models.consultation import ConsultationModel
from app.services.schemas.consultationSchema import ConsultationCreate, ConsultationRead

class ConsulataionService:
    def __init__(self, session: AsyncSession):
        self.session = session
        
        
    async def get_consultation_by_id(self, id: int) -> ConsultationRead:
        consultation = await self.session.get( ConsultationModel,id)
        
        if consultation is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Concultation not found"
            )
            
        return ConsultationRead.model_validate(consultation)
    
    async def create_new_consultation(self, consultation: ConsultationCreate) -> ConsultationRead:
        new_consultation = ConsultationModel(
            **consultation.model_dump()
        )
        
        self.session.add(new_consultation)
        await self.session.commit()
        await self.session.refresh(new_consultation)
        
        return ConsultationRead.model_validate(new_consultation)
    
    
    async def update_consultation_by_id(self, id: int, new_data: dict) -> ConsultationRead:
        consultation = await self.session.get( ConsultationModel,id)
        
        if consultation is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Concultation not found"
            )
            
        consultation_dict = {
            **consultation.model_dump()
        }
        consultation_dict.update(new_data)
        
        consultation.sqlmodel_update(consultation_dict)
        
        self.session.add(consultation)
        await self.session.commit()
        await self.session.refresh(consultation)
        
        return ConsultationRead.model_validate(consultation)
    
    
    async def delete_consultation_by_id(self, id: int) -> dict:
        consultation = await self.session.get( ConsultationModel,id)
        
        if consultation is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Concultation not found"
            )
            
        await self.session.delete(consultation)
        await self.session.commit()
        
        return {
            "detail": "Conssultation deleted successfully"
        }