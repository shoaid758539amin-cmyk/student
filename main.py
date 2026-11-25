from model import student, subjects
from fastapi import FastAPI
from routers import student_controller
from db import engine, base

base.metadata.create_all(bind = engine)

app = FastAPI(title="Recap Project")
app.include_router(student_controller.router)
