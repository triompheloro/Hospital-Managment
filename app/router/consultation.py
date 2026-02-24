from fastapi import APIRouter

from app.services.schemas.consultationSchema import ConsultationCreate, ConsultationRead
from app.services.schemas.dependencies import ConsultationDep

consultationRouter = APIRouter(prefix="/consultation", tags=["Consultation endpoints"])


@consultationRouter.get("/")
async def get_consultation_by_id(id: int, service : ConsultationDep) -> ConsultationRead:
    return await service.get_consultation_by_id(id)

@consultationRouter.post("/")
async def create_new_consultation(new_consultation: ConsultationCreate, service: ConsultationDep) -> ConsultationRead:
    return await service.create_new_consultation(new_consultation)

@consultationRouter.patch("/")
async def update_consultation_by_id(id: int, new_data:dict, service: ConsultationDep) -> ConsultationRead:
    return await service.update_consultation_by_id(id, new_data)


@consultationRouter.delete("/")
async def delete_consultation_by_id(id: int, service: ConsultationDep) -> dict:
    return await service.delete_consultation_by_id(id)