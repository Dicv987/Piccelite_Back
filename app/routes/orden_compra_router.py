from fastapi import APIRouter
from ..controllers import orden_compra_controller
from ..models.inventory_models import OrdenCompraModel

router = APIRouter()

@router.get("/ordenes-compra")
def read_ordenes():
    return orden_compra_controller.get_ordenes_compra()

@router.get("/ordenes-compra/{orden_id}")
def read_orden_by_id(orden_id: int):
    return orden_compra_controller.get_orden_compra_by_id(orden_id)

@router.post("/ordenes-compra")
def create_orden(orden: OrdenCompraModel):
    return orden_compra_controller.create_orden_compra(orden)

@router.put("/ordenes-compra/{orden_id}")
def update_orden(orden_id: int, orden: OrdenCompraModel):
    return orden_compra_controller.update_orden_compra(orden_id, orden)

@router.delete("/ordenes-compra/{orden_id}")
def delete_orden(orden_id: int):
    return orden_compra_controller.delete_orden_compra(orden_id)
