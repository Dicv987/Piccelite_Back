from fastapi import APIRouter
from ..controllers import venta_detalle_controller
from ..models.inventory_models import VentaDetalleModel

router = APIRouter()

@router.post("/ventas-detalle")
def create_detalle(detalle: VentaDetalleModel):
    return venta_detalle_controller.create_venta_detalle(detalle)

@router.get("/ventas-detalle/{venta_id}")
def get_detalles_por_venta(venta_id: int):
    return venta_detalle_controller.get_detalles_by_venta(venta_id)
