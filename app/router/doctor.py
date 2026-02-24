from fastapi import APIRouter

from app.services.schemas.dependencies import DoctorDep
from app.services.schemas.doctorSchema import DoctorCreate, DoctorRead

doctorRouter = APIRouter(prefix="/doctor", tags=["Doctor endpoints"])

@doctorRouter.get("/")
async def get_doctor_by_id(id:int, service:DoctorDep) -> DoctorRead:
    return await service.get_doctor_by_id(id)


@doctorRouter.post("/")
async def create_new_doctor(new_doctor: DoctorCreate, service: DoctorDep) ->DoctorRead:
    return await service.create_new_doctor(new_doctor)

@doctorRouter.patch("/")
async def update_doctor_by_id(id:int, new_data:dict, service: DoctorDep)-> DoctorRead:
    return await service.update_doctor_by_id(id)


@doctorRouter.delete("/")
async def delete_doctor_by_id(id:int, service: DoctorDep) -> dict:
    return await service.delete_doctor_by_id(id)