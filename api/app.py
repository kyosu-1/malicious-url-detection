from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from api.routers import router


app = FastAPI()
# cors
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/api")
