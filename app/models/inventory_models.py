from pydantic import BaseModel
from typing import Optional
from datetime import date

# --------- SUCURSAL ---------
class SucursalModel(BaseModel):
    id: int
    nombre: str
    ubicacion: str
    gerente: str

# --------- PRODUCTO ---------
class ProductoModel(BaseModel):
    id: int
    nombre: str
    descripcion: str
    precio: float
    proveedor: str
    es_critico: bool
    sucursal_id: int

# --------- ORDEN DE COMPRA ---------
class OrdenCompraModel(BaseModel):
    id: int
    sucursal_id: int
    monto_impuesto: float
    estado: str
    fecha: date

# --------- DETALLE ORDEN DE COMPRA ---------
class OrdenCompraDetalleModel(BaseModel):
    id: int
    producto_id: int
    orden_compra_id: int
    nombre_producto: str
    precio: float
    cantidad: int
    total: float
    impuesto: float

# --------- VENTA ---------
class VentaModel(BaseModel):
    id: int
    sucursal_id: int
    monto_impuesto: float
    fecha: date

# --------- DETALLE VENTA ---------
class VentaDetalleModel(BaseModel):
    id: int
    producto_id: int
    venta_id: int
    nombre_producto: str
    precio: float
    cantidad: int
    total: float
    impuesto: float

# --------- INVENTARIO ---------
class InventarioModel(BaseModel):
    producto_id: int
    sucursal_id: int
    nombre: str
    cantidad: int

# --------- ARQUEO ---------
class ArqueoModel(BaseModel):
    id: int
    sucursal_id: int
    inventario_teorico: float
    inventario_fisico: float
    diferencia: float
    fecha: date

# --------- DETALLE ARQUEO ---------
class ArqueoDetalleModel(BaseModel):
    id: int
    arqueo_id: int
    producto_id: int
    nombre: str
    conteo_teorico: int
    conteo_fisico: int
    diferencia: int
