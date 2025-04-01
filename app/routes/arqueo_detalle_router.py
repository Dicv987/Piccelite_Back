from fastapi import APIRouter
from ..controllers import arqueo_detalle_controller
from ..models.inventory_models import ArqueoDetalleModel

router = APIRouter()

@router.post("/arqueos-detalle")
def create_arqueo_detalle(detalle: ArqueoDetalleModel):
    return arqueo_detalle_controller.create_arqueo_detalle(detalle)

@router.get("/arqueos-detalle/{arqueo_id}")
def get_detalles_by_arqueo(arqueo_id: int):
    return arqueo_detalle_controller.get_detalles_by_arqueo(arqueo_id)
