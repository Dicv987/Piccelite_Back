from fastapi import APIRouter

# Importación de routers
from .producto_router import router as producto_router
from .sucursal_router import router as sucursal_router
from .orden_compra_router import router as orden_compra_router
from .orden_compra_detalle_router import router as orden_compra_detalle_router
from .venta_router import router as venta_router
from .venta_detalle_router import router as venta_detalle_router
from .inventario_router import router as inventario_router
from .arqueo_router import router as arqueo_router
from .arqueo_detalle_router import router as arqueo_detalle_router

router = APIRouter()

# ---------------- PRODUCTOS ----------------
router.include_router(producto_router, tags=["Productos"])

# ---------------- SUCURSALES ----------------
router.include_router(sucursal_router, tags=["Sucursales"])

# ---------------- ORDENES DE COMPRA ----------------
router.include_router(orden_compra_router, tags=["OrdenesCompra"])
router.include_router(orden_compra_detalle_router, tags=["OrdenesCompraDetalle"])

# ---------------- VENTAS ----------------
router.include_router(venta_router, tags=["Ventas"])
router.include_router(venta_detalle_router, tags=["VentasDetalle"])

# ---------------- INVENTARIO ----------------
router.include_router(inventario_router, tags=["Inventario"])

# ---------------- ARQUEO ----------------
router.include_router(arqueo_router, tags=["Arqueo"])
router.include_router(arqueo_detalle_router, tags=["ArqueoDetalle"])
