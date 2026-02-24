from typing import Annotated

from fastapi import Depends

from app.database.session import create_session

from sqlalchemy.ext.asyncio import AsyncSession

from app.services import consultationService
from app.services.appointmentService import AppointmentService
from app.services.doctorService import DoctorService
from app.services.patientService import PatientService
from app.services.specializationService import SpecializationService
from app.services.consultationService import ConsulataionService


SessionDep = Annotated[AsyncSession, Depends(create_session)]


# Patient service dependency
def get_patient_service(session: SessionDep):
    return PatientService(session)

PatientServiceDep = Annotated[PatientService,Depends(get_patient_service)]


# Specialization service dependency
def get_specialization_service(session: SessionDep):
    return SpecializationService(session)

SpecializationDep = Annotated[SpecializationService, Depends(get_specialization_service)]


# Doctor Service dependency
def get_doctor_service(session: SessionDep):
    return DoctorService(session)

DoctorDep = Annotated[DoctorService, Depends(get_doctor_service)]

# Appointment Service dependency
def get_appointment_service(session: SessionDep):
    return AppointmentService(session)

AppointmentDep = Annotated[AppointmentService, Depends(get_appointment_service)]


# Consultation service dependenciy
def get_consultation_service(session: SessionDep):
    return ConsulataionService(session)

ConsultationDep = Annotated[ConsulataionService, Depends(get_consultation_service)]