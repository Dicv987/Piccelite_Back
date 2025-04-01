from ..db import supabase
from ..models.inventory_models import VentaDetalleModel

# Disminuir inventario de un producto
def disminuir_inventario(producto_id: int, sucursal_id: int, cantidad: int):
    inventario = supabase.table("inventario").select("cantidad").eq("producto_id", producto_id).eq("sucursal_id", sucursal_id).execute().data
    if inventario:
        cantidad_actual = inventario[0]["cantidad"] - cantidad
        cantidad_actual = max(0, cantidad_actual)  # No permitir negativos
        supabase.table("inventario").update({"cantidad": cantidad_actual}).eq("producto_id", producto_id).eq("sucursal_id", sucursal_id).execute()

# Crear un detalle de venta y actualizar inventario
def create_venta_detalle(detalle: VentaDetalleModel):
    supabase.table("venta_detalle").insert(detalle.dict()).execute()
    disminuir_inventario(detalle.producto_id, detalle.venta_id, detalle.cantidad)
    return {"message": "Detalle creado y stock reducido"}

# Obtener detalles por ID de venta
def get_detalles_by_venta(venta_id: int):
    return supabase.table("venta_detalle").select("*").eq("venta_id", venta_id).execute().data
