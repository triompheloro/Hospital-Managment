from fastapi import APIRouter

from app.services.schemas.dependencies import SpecializationDep
from app.services.schemas.specializationSchema import SpecializationSchema

specialization_router = APIRouter(prefix="/specialization", tags=["Specialization endpoints"])


@specialization_router.get("/")
async def get_specialization_by_id(id: int, service: SpecializationDep) -> SpecializationSchema :
    return await service.get_specialization_by_id(id)


@specialization_router.post("/")
async def create_new_specialization(new_specialization: SpecializationSchema, service: SpecializationDep) -> SpecializationSchema:
    return await service.create_new_specialization(new_specialization)

@specialization_router.patch("/")
async def update_specialization_by_id(id: int,new_date: SpecializationSchema, service: SpecializationDep) -> SpecializationSchema:
    return await service.update_specialization_by_id(id, new_date)

@specialization_router.delete("/")
async def delete_specialization_by_id(id: int, service: SpecializationDep) -> dict:
    return await service.delete_specialization_by_id(id)