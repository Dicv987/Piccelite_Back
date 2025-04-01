from ..db import supabase
from ..models.inventory_models import OrdenCompraDetalleModel

# Aumentar inventario de un producto
def aumentar_inventario(producto_id: int, sucursal_id: int, cantidad: int):
    inventario = supabase.table("inventario").select("cantidad").eq("producto_id", producto_id).eq("sucursal_id", sucursal_id).execute().data
    if inventario:
        cantidad_actual = inventario[0]["cantidad"] + cantidad
        supabase.table("inventario").update({"cantidad": cantidad_actual}).eq("producto_id", producto_id).eq("sucursal_id", sucursal_id).execute()
    else:
        supabase.table("inventario").insert({
            "producto_id": producto_id,
            "sucursal_id": sucursal_id,
            "cantidad": cantidad
        }).execute()

# Crear un detalle de orden de compra y actualizar inventario
def create_orden_compra_detalle(detalle: OrdenCompraDetalleModel):
    supabase.table("orden_compra_detalle").insert(detalle.dict()).execute()
    aumentar_inventario(detalle.producto_id, detalle.orden_compra_id, detalle.cantidad)
    return {"message": "Detalle creado y stock actualizado"}

# Obtener detalles por ID de orden
def get_detalles_by_orden(orden_id: int):
    return supabase.table("orden_compra_detalle").select("*").eq("orden_compra_id", orden_id).execute().data
