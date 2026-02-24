from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.models.specialization import SpecializationModel
from app.services.schemas.specializationSchema import SpecializationSchema

class SpecializationService:
    def __init__(self,session: AsyncSession):
        self.session = session
        
    async def get_specialization_by_id(self,id:int) -> SpecializationSchema:
        specialization = await self.session.get(SpecializationModel,id)
        
        if specialization is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Specialization not found"
            )
        
        return    SpecializationSchema.model_validate(specialization)
    
    async def create_new_specialization(self, specialization: SpecializationSchema) -> SpecializationSchema:
        new_specialization = SpecializationModel(
            **specialization.model_dump()
        )
        
        self.session.add(new_specialization)
        await self.session.commit()
        await self.session.refresh(new_specialization)
        
        return SpecializationSchema.model_validate(new_specialization) 
    
    
    async def update_specialization_by_id(self, id: int, new_data: SpecializationSchema) -> SpecializationSchema:
        specialization = await self.session.get(SpecializationModel, id)
        
        if specialization is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Specialization not found"
            )
            
        specialization.sqlmodel_update(new_data)
        
        self.session.add(specialization)
        await self.session.commit()
        await self.session.refresh(specialization)
        
        return SpecializationSchema.model_validate(specialization)
        
    
    async def delete_specialization_by_id(self, id:int) -> dict:
        specialization = await self.session.get(SpecializationModel, id)
        
        if specialization is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Specialization not found"
            )
            
        await self.session.delete( specialization)
        await self.session.commit()
        
        return {
            "detail": "Specialization deleted succesfully"
        }
        