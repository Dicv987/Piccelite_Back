from fastapi import APIRouter
from ..controllers import sucursal_controller
from ..models.inventory_models import SucursalModel

router = APIRouter()

@router.get("/sucursales")
def read_sucursales():
    return sucursal_controller.get_sucursales()

@router.get("/sucursales/{sucursal_id}")
def read_sucursal_by_id(sucursal_id: int):
    return sucursal_controller.get_sucursal_by_id(sucursal_id)

@router.post("/sucursales")
def create_sucursal(sucursal: SucursalModel):
    return sucursal_controller.create_sucursal(sucursal)

@router.put("/sucursales/{sucursal_id}")
def update_sucursal(sucursal_id: int, sucursal: SucursalModel):
    return sucursal_controller.update_sucursal(sucursal_id, sucursal)

@router.delete("/sucursales/{sucursal_id}")
def delete_sucursal(sucursal_id: int):
    return sucursal_controller.delete_sucursal(sucursal_id)
