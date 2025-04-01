from fastapi import APIRouter
from ..controllers import orden_compra_detalle_controller
from ..models.inventory_models import OrdenCompraDetalleModel

router = APIRouter()

@router.post("/ordenes-compra-detalle")
def create_detalle(detalle: OrdenCompraDetalleModel):
    return orden_compra_detalle_controller.create_orden_compra_detalle(detalle)

@router.get("/ordenes-compra-detalle/{orden_id}")
def get_detalles_por_orden(orden_id: int):
    return orden_compra_detalle_controller.get_detalles_by_orden(orden_id)
