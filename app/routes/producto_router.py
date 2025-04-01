from fastapi import APIRouter
from ..controllers import producto_controller
from ..models.inventory_models import ProductoModel

router = APIRouter()

@router.get("/productos")
def read_productos():
    return producto_controller.get_productos()

@router.get("/productos/{producto_id}")
def read_producto_by_id(producto_id: int):
    return producto_controller.get_producto_by_id(producto_id)

@router.post("/productos")
def create_producto(producto: ProductoModel):
    return producto_controller.create_producto(producto)

@router.put("/productos/{producto_id}")
def update_producto(producto_id: int, producto: ProductoModel):
    return producto_controller.update_producto(producto_id, producto)

@router.delete("/productos/{producto_id}")
def delete_producto(producto_id: int):
    return producto_controller.delete_producto(producto_id)
