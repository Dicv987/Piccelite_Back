from fastapi import APIRouter
from ..controllers import arqueo_controller
from ..models.inventory_models import ArqueoModel

router = APIRouter()

@router.get("/arqueos")
def read_arqueos():
    return arqueo_controller.get_arqueos()

@router.get("/arqueos/{arqueo_id}")
def read_arqueo_by_id(arqueo_id: int):
    return arqueo_controller.get_arqueo_by_id(arqueo_id)

@router.post("/arqueos")
def create_arqueo(arqueo: ArqueoModel):
    return arqueo_controller.create_arqueo(arqueo)

@router.delete("/arqueos/{arqueo_id}")
def delete_arqueo(arqueo_id: int):
    return arqueo_controller.delete_arqueo(arqueo_id)
