from fastapi import APIRouter
from api.property import get_property
from api.analysis import analyze_property

router = APIRouter()

@router.get("/property/{address}")
def property_lookup(address: str):
    return get_property(address)

@router.get("/analyze/{address}")
def analyze(address: str):
    return analyze_property(address)
