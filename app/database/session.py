from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlmodel import SQLModel
from ..setting.config import db_settings

from sqlalchemy.orm import sessionmaker

engine = create_async_engine(
    url= db_settings.POSTGRESQL_URL,
    echo=True
)

async def create_db_tables():
    async with engine.begin() as connection:
        from .models.consultation import ConsultationModel
        from .models.apointment import AppointmentModel
        from .models.doctor import DoctorModel
        from .models.patient import PatientModel
        from .models.specialization import SpecializationModel
        
        await connection.run_sync(SQLModel.metadata.create_all)
        
        

async def create_session():
    async_session = sessionmaker(
        bind=engine,
        class_=AsyncSession,
        expire_on_commit=False
    )
    async with async_session() as session:
        yield session
        

        

