from fastapi import APIRouter

from app.services.schemas.appointmentSchema import AppointmentCreate, AppointmentRead
from app.services.schemas.dependencies import AppointmentDep


appointmentRouter = APIRouter (prefix="/appointment", tags=["Appointments endpoints"])


@appointmentRouter.get("/")
async def get_appointment_by_id(id: int, service: AppointmentDep) -> AppointmentRead:
    return await service.get_appointment_by_id(id)


@appointmentRouter.post("/")
async def create_new_appointment(new_appointment: AppointmentCreate, service: AppointmentDep) -> AppointmentRead:
    return await service.create_new_appointment(new_appointment)

@appointmentRouter.patch("/")
async def update_appointment_by_id(id: int, new_data: dict, service: AppointmentDep) -> AppointmentRead:
    return await service.update_appointment_by_id(id, new_data)

@appointmentRouter.delete("/")
async def delete_appointment_by_id(id:int, service: AppointmentDep) -> dict:
    return await service.delete_appointment_by_id(id)
    