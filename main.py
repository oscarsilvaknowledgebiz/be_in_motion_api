import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import routers


app = FastAPI(
    contact=dict(
        email="geral@knowldgzebiz.pt",
        http="https://knowledgebiz.pt"
    ),
    version="1.0.0",
    title="API BE IN MOTION",
    description="This API integrates with BE IN MOTION system"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(routers.user_router.router, prefix="/user", tags=["user"])
app.include_router(routers.user_constitution_router.router, prefix="/user-constitution", tags=["user_constitution"])
app.include_router(routers.user_special_condition_router.router, prefix="/user-special-condition", tags=["user_special_conditions"])
app.include_router(routers.user_physiotherapeut_router.router, prefix="/user-physiotherapeut", tags=["user_physiotherapeut"])
app.include_router(routers.medical_prescription_router.router, prefix="/medical-prescription", tags=["medicalPrescription"])
app.include_router(routers.physiotherapeut_info_router.router, prefix="/physiotherapeut-info", tags=["physiotherapeut-info"])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=2828)
