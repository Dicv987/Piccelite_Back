from fastapi import APIRouter
from ..controllers import venta_controller
from ..models.inventory_models import VentaModel

router = APIRouter()

@router.get("/ventas")
def read_ventas():
    return venta_controller.get_ventas()

@router.get("/ventas/{venta_id}")
def read_venta_by_id(venta_id: int):
    return venta_controller.get_venta_by_id(venta_id)

@router.post("/ventas")
def create_venta(venta: VentaModel):
    return venta_controller.create_venta(venta)

@router.put("/ventas/{venta_id}")
def update_venta(venta_id: int, venta: VentaModel):
    return venta_controller.update_venta(venta_id, venta)

@router.delete("/ventas/{venta_id}")
def delete_venta(venta_id: int):
    return venta_controller.delete_venta(venta_id)
