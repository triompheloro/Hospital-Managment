from typing import Annotated

from fastapi import Depends

from app.database.session import create_session

from sqlalchemy.ext.asyncio import AsyncSession

from app.services.patientService import PatientService
from app.services.specializationService import SpecializationService


SessionDep = Annotated[AsyncSession, Depends(create_session)]


# Patient service dependency
def get_patient_service(session: SessionDep):
    return PatientService(session)

PatientServiceDep = Annotated[PatientService,Depends(get_patient_service)]


# Specialization service dependency
def getr_specialization_service(session: SessionDep):
    return SpecializationService(session)

SpecializationDep = Annotated[SpecializationService, Depends(getr_specialization_service)]