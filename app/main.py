from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference
from contextlib import asynccontextmanager

from app.database.session import create_db_tables


from app.router.patient import patientRouter
from app.router.specialization import specialization_router

@asynccontextmanager
async def lifespan_handler(app: FastAPI):
    await create_db_tables()
    yield

app = FastAPI(lifespan= lifespan_handler)


@app.get("/scalar", include_in_schema=False)
def api_documentation_and_testing():
    """This function aim to test all API endpoints"""
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="API documentation and testing"
    )
    
app.include_router(patientRouter)
app.include_router(specialization_router)