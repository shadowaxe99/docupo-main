from fastapi import APIRouter

router = APIRouter()

# Define your API routes here

from fastapi import Depends
from app.api import router

from app.auth import get_current_user

router = APIRouter(dependencies=[Depends(get_current_user)])