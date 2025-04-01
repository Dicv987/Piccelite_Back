from fastapi import APIRouter
from ..controllers import inventario_controller

router = APIRouter()

@router.get("/inventario")
def get_inventario():
    return inventario_controller.get_inventario()

@router.get("/inventario/sucursal/{sucursal_id}")
def get_inventario_by_sucursal(sucursal_id: int):
    return inventario_controller.get_inventario_by_sucursal(sucursal_id)

@router.get("/inventario/producto/{producto_id}/sucursal/{sucursal_id}")
def get_producto_inventario(producto_id: int, sucursal_id: int):
    return inventario_controller.get_producto_inventario(producto_id, sucursal_id)

@router.put("/inventario/producto/{producto_id}/sucursal/{sucursal_id}")
def update_inventario(producto_id: int, sucursal_id: int, cantidad: int):
    return inventario_controller.update_inventario(producto_id, sucursal_id, cantidad)
