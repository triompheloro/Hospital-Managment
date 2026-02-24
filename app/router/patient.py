from fastapi import APIRouter

from app.services.schemas.dependencies import PatientServiceDep
from app.services.schemas.patientSchema import PatientRead, PantientCreate


patientRouter = APIRouter(prefix="/patient", tags=["Patient endpoints"])


@patientRouter.get("/")
async def get_patient_by_id(id: int, service: PatientServiceDep) -> PatientRead:
    return await service.get_patient_by_id(id)


@patientRouter.post("/")
async def sign_up_new_patient(patient: PantientCreate, service: PatientServiceDep) -> PatientRead:
    return await service.create_new_patient(patient)

@patientRouter.patch("/")
async def update_patient_profile_by_id(id: int, update_info: dict, service: PatientServiceDep) -> PatientRead:
    return await service.update_patient_profile_by_id(id, update_info)

@patientRouter.delete("/")
async def delate_patient_by_id(id: int, service: PatientServiceDep) -> dict:
    return await service.delete_patient_by_id(id)