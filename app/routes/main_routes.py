from fastapi import APIRouter
from services.main_services import MainService

router = APIRouter()
main_service = MainService()

@router.get("/main")
def main():
    return main_service.main() 