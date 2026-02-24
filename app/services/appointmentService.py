from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.models.apointment import AppointmentModel
from app.services.schemas.appointmentSchema import AppointmentCreate, AppointmentRead

class AppointmentService:
    def __init__(self, session:AsyncSession ):
        self.session = session
        
    
    async def get_appointment_by_id(self, id:int) -> AppointmentRead:
        appointment = await self.session.get(AppointmentModel,id)
        if appointment is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Appointment not found"
            )   
        return AppointmentRead.model_validate(appointment)
    
    
    async def create_new_appointment(self, appointment: AppointmentCreate) -> AppointmentRead:
        appointment = AppointmentModel(
            **appointment.model_dump()
        )
        
        self.session.add(appointment)
        await self.session.commit()
        await self.session.refresh(appointment)
        
        return AppointmentRead.model_validate(appointment)
    
    async def update_appointment_by_id(self, id: int, new_data: dict) -> AppointmentRead:
        appointment = await self.session.get(AppointmentModel,id)
        if appointment is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Appointment not found"
            )
            
        appointment_dict = {
            **appointment.model_dump()
        } 
        
        appointment_dict.update(new_data)
        
        appointment.sqlmodel_update(appointment_dict)
        
        self.session.add(appointment)
        await self.session.commit()
        await self.session.refresh(appointment)
        
        return AppointmentRead.model_validate(appointment)
    
    
    async def delete_appointment_by_id(self, id: int) -> dict:
        appointment = await self.session.get(AppointmentModel,id)
        if appointment is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Appointment not found"
            )
        
        await self.session.delete(appointment)
        await self.session.commit()
        
        return {
            "detail": "Appointement delted succesfully"
        }